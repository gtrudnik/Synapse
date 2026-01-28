import os
import uuid

from fastapi import UploadFile
from src.users.consts import AVATAR_DIR


async def save_avatar(file: UploadFile) -> str:
    os.makedirs(AVATAR_DIR, exist_ok=True)

    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(AVATAR_DIR, filename)

    print(filepath)

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    return filepath
