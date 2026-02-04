import uuid

from sqlalchemy.orm import Session
from .models import ZoomMeeting
from .schemas import ZoomMeetingCreate

class ZoomMeetingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, meeting_data: ZoomMeetingCreate, join_url: str) -> ZoomMeeting:
        meeting = ZoomMeeting(
            host_id=meeting_data.host_id,
            topic=meeting_data.topic,
            start_time=meeting_data.start_time,
            join_url=join_url,
        )
        self.db.add(meeting)
        self.db.commit()
        self.db.refresh(meeting)
        return meeting

    def delete(self, meeting_id: int) -> ZoomMeeting:
        self.db.delete(meeting_id)
        self.db.commit()


    def get_by_id(self, meeting_id: uuid.UUID) -> ZoomMeeting | None:
        return self.db.get(ZoomMeeting, meeting_id)
