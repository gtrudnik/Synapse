from sqlalchemy import event
from sqlalchemy.orm import object_session, Session

from src import ChatConversation
from src.cards.models import Card
from src.matches.models import CardLike, UserMatch
from src.matches.service import MatchService


@event.listens_for(CardLike, "after_insert")
def create_match_if_mutual(mapper, connection, like: CardLike):
    from src.database.core import SessionLocal

    session = SessionLocal()
    match_service = MatchService(session)

    print("EVENT TRIGGERED")
    if not session:
        return

    liked_card = session.get(Card, like.to_card_id)
    if not liked_card:
        session.close()
        return

    target_user_id = liked_card.user_id
    mutual_like = (
        session.query(CardLike)
        .join(Card, Card.id == CardLike.to_card_id)
        .filter(
            CardLike.from_user_id == target_user_id,
            Card.user_id == like.from_user_id,
        )
        .first()
    )
    if not mutual_like:
        session.close()
        return

    exists = match_service.exists(like.from_user_id, target_user_id)

    if not exists:
        match = UserMatch(
            user1_id=like.from_user_id,
            user2_id=target_user_id,
        )
        session.add(match)
        session.flush()

        conversation = ChatConversation(match_id=match.id)
        session.add(conversation)

        session.commit()

    session.close()


@event.listens_for(Session, "after_flush")
def delete_match_if_like_removed(session, flush_context):
    for obj in session.deleted:
        if isinstance(obj, CardLike):
            card_owner_id = (
                session.query(Card.user_id).filter(Card.id == obj.to_card_id).scalar()
            )

            if not card_owner_id:
                continue

            match = (
                session.query(UserMatch)
                .filter(
                    (
                        (UserMatch.user1_id == obj.from_user_id)
                        & (UserMatch.user2_id == card_owner_id)
                    )
                    | (
                        (UserMatch.user2_id == obj.from_user_id)
                        & (UserMatch.user1_id == card_owner_id)
                    )
                )
                .first()
            )
            if match:
                session.delete(match)

                chat = (
                    session.query(ChatConversation).filter_by(match_id=match.id).first()
                )
                if chat:
                    session.delete(chat)
