import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer, ForeignKey
from src.database.core import Base

class ZoomMeeting(Base):
    __tablename__ = "zoom_meetings"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    host_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    topic: Mapped[str] = mapped_column(String(255))
    start_time: Mapped[DateTime] = mapped_column(DateTime)
    join_url: Mapped[str] = mapped_column(String(500))