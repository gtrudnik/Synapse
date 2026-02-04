import os

import requests
from sqlalchemy.orm import Session
from .schemas import ZoomMeetingCreate, ZoomMeetingRead
from .repository import ZoomMeetingRepository

ZOOM_API_KEY = os.environ.get("ZOOM_API_KEY")
ZOOM_API_SECRET = os.environ.get("ZOOM_API_SECRET")
ZOOM_USER_ID = os.environ.get("ZOOM_USER_ID")
ZOOM_ACCOUNT_ID = os.environ.get("ZOOM_ACCOUNT_ID")


class ZoomMeetingService:
    def __init__(self, db: Session):
        self.repo = ZoomMeetingRepository(db)

    def create_zoom_meeting(self, meeting_data: ZoomMeetingCreate) -> ZoomMeetingRead:
        data = requests.post(
            url="https://zoom.us/oauth/token",
            data={"grant_type": "account_credentials", "account_id": ZOOM_ACCOUNT_ID},
            headers={"Host": "zoom.us", "Authorization": f"Basic {ZOOM_API_KEY}"},
        ).json()

        token = data.get("access_token")
        url = f"https://api.zoom.us/v2/users/me/meetings"

        headers = {"Authorization": f"Bearer {token}"}
        json_data = {
            "topic": meeting_data.topic,
            "type": 2,
            "start_time": meeting_data.start_time.isoformat(),
            "timezone": "UTC",
        }
        resp = requests.post(url, headers=headers, json=json_data)
        resp.raise_for_status()
        data = resp.json()

        join_url = data["join_url"]

        meeting = self.repo.create(meeting_data, join_url)
        return ZoomMeetingRead.model_validate(meeting)
