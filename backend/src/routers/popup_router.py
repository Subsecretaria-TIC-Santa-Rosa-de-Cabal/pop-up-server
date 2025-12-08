import base64
from datetime import datetime
import json
import os
from pathlib import Path
import tempfile
from typing import List
from uuid import UUID, uuid4

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
import requests

from middlewares.auth_middleware import get_current_user
from schemas.popup_schema import LunchPopupParameters, PopupLunchResponse


popup_router = APIRouter()

@popup_router.get('/', response_model=List[PopupLunchResponse])
async def get_popup(
    current_user = Depends(get_current_user)
):
    popups = []
    with open("popups.json", "r", encoding="utf-8") as f:
        for popup in json.load(f):
            if popup['enabled'] is True:
                popups.append(popup)
    return popups

@popup_router.post('/launch', response_model=PopupLunchResponse)
async def create_popup(
    parameters: LunchPopupParameters,
    current_user = Depends(get_current_user)
):
    devices = []
    with open("devices.json", "r", encoding="utf-8") as f:
        for device in json.load(f):
            if device['enabled'] is True:
                if parameters.dependency_identifier is not None:
                    if device['dependency_identifier'] == str(parameters.dependency_identifier):
                        devices.append(device)
                else:
                    devices.append(device)

    if len(devices) == 0:
        return []
    
    payload = {
        "name": parameters.name,
        "description": parameters.description,
        "date": parameters.date.isoformat(),
        "image_base64": parameters.image_base64
    }
    plain_payload = json.dumps(payload)
    
    popup_devices = []
    for device in devices:
        key = bytes.fromhex(device['key'])
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ct = aesgcm.encrypt(nonce, plain_payload.encode(), associated_data=None)
        token = base64.urlsafe_b64encode(nonce + ct).decode("utf-8")

        url = f"http://{device['IP']}:{device['port']}/launch"
        resp = requests.post(
            url,
            data=token,
            headers={"Content-Type": "text/plain"}
        )
        if resp.status_code == 200:
            popup_devices.append(
                device['identifier']
            )

    os.makedirs(".images", exist_ok=True)
    image_data = base64.b64decode(parameters.image_base64)
    popup_identifier = str(uuid4())

    file_path = os.path.join(".images", f"{popup_identifier}.png")
    with open(file_path, "wb") as f:
        f.write(image_data)

    popup = {
        'identifier': popup_identifier,
        'enabled': True,
        'registration_date': datetime.now().isoformat(),
        'last_update': datetime.now().isoformat(),
        'name': parameters.name,
        'description': parameters.description,
        'date': parameters.date.isoformat(),
        'device_identifiers': popup_devices,
        'image_path': file_path,
        'dependency_identifier': parameters.dependency_identifier
    }

    popups = []
    with open("popups.json", "r", encoding="utf-8") as f:
        popups = json.load(f)
    popups.append(popup)

    dir_temp = os.path.dirname("popups.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(popups, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "popups.json")
    
    return PopupLunchResponse(
        identifier=popup['identifier'],
        enabled=popup['enabled'],
        registration_date=popup['registration_date'],
        last_update=popup['last_update'],
        name=popup['name'],
        description=popup['description'],
        date=popup['date'],
        device_identifiers=popup['device_identifiers'],
        image_path=popup['image_path'],
        dependency_identifier=popup['dependency_identifier']
    )

@popup_router.get("/images/{popup_identifier}")
def get_popup_image(popup_identifier: UUID, current_user = Depends(get_current_user)):
    filename = f"{popup_identifier}.png"
    IMAGES_DIR = Path(".images")
    safe_path = (IMAGES_DIR / Path(filename)).resolve()
    if not str(safe_path).startswith(str(IMAGES_DIR.resolve())):
        raise HTTPException(status_code=400, detail="Invalid filename")
    if not safe_path.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(path=str(safe_path), media_type="image/png")
