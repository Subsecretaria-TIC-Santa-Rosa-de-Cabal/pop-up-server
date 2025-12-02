from datetime import datetime
import json
import os
import tempfile
from typing import List
from uuid import UUID, uuid4

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from fastapi import APIRouter, Depends
import requests

from exceptions.fastapi_authentication_exceptions import InvalidUserToken
from exceptions.fastapi_device_exceptions import CorruptedDevice, DeviceAlreadyExists, DeviceDoesNotFound
from middlewares.auth_middleware import get_current_user
from schemas.device_schema import CreateDeviceParameters, DeviceFilterParameters, DeviceResponse, UpdateDeviceParameters


device_router = APIRouter()

@device_router.get('/', response_model=List[DeviceResponse])
async def get_devices(
    parameters: DeviceFilterParameters = Depends(),
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
    return devices

@device_router.post('/', response_model=DeviceResponse)
async def create_device(
    parameters: CreateDeviceParameters,
    current_user = Depends(get_current_user)
):
    with open("roles.json", "r", encoding="utf-8") as f:
        roles = json.load(f)
        current_role = None
        for role in roles:
            if role['identifier'] == current_user['role_identifier']:
                current_role = role
                break
    if current_role['code'] != 'ADMIN':
        raise InvalidUserToken()
    
    with open("devices.json", "r", encoding="utf-8") as f:
        for device in json.load(f):
            if device['IP'] == parameters.IP and device['enabled'] == True:
                raise DeviceAlreadyExists()
    
    try:
        url = f"http://{parameters.IP}:{parameters.port}/check"
        resp = requests.get(url)
        if resp.status_code != 200:
            raise DeviceDoesNotFound()
    
        with open("private_key.pem","rb") as f:
            private_key = load_pem_private_key(f.read(), password=None)
            text = resp.text
            plaintext = private_key.decrypt(
                bytes.fromhex(text.replace('"','')),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            device_data = json.loads(plaintext.decode('utf-8'))
            if 'hostname' not in device_data or 'mac' not in device_data or 'operating_system' not in device_data:
                raise CorruptedDevice()
            
            new_device = {
                "identifier": str(uuid4()),
                "enabled": True,
                "registration_date": datetime.now().isoformat(),
                "last_update": datetime.now().isoformat(),
                "name": parameters.name,
                "IP": parameters.IP,
                "port": parameters.port,
                "dependency_identifier": str(parameters.dependency_identifier),
                "status": "ONLINE",
                "last_connection": datetime.now().isoformat(),
                "hostname": device_data.get('hostname'),
                "mac": device_data.get('mac'),
                "operating_system": device_data.get('operating_system')
            }
            
            devices = []
            with open("devices.json", "r", encoding="utf-8") as f:
                devices = json.load(f)
            devices.append(new_device)

            dir_temp = os.path.dirname("devices.json") or "."
            with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
                json.dump(devices, tf, ensure_ascii=False, indent=2)
                temp_name = tf.name

            os.replace(temp_name, "devices.json")

        dependencies = []
        with open("dependencies.json", "r", encoding="utf-8") as f:
            dependencies = json.load(f)
            for dependency in dependencies:
                if dependency['identifier'] == str(parameters.dependency_identifier):
                    dependency['devices_count'] += 1
                    dependency['last_update'] = datetime.now().isoformat()
                    break
        
        with open("dependencies.json", "w", encoding="utf-8") as tfd:
            json.dump(dependencies, tfd, ensure_ascii=False, indent=2)

        return new_device
    except Exception as e:
        print(e)
        raise CorruptedDevice()

@device_router.patch('/', response_model=DeviceResponse)
async def update_device(
    parameters: UpdateDeviceParameters,
    current_user = Depends(get_current_user)
):
    with open("roles.json", "r", encoding="utf-8") as f:
        roles = json.load(f)
        current_role = None
        for role in roles:
            if role['identifier'] == current_user['role_identifier']:
                current_role = role
                break
    if current_role['code'] != 'ADMIN':
        raise InvalidUserToken()
    
    devices = []
    with open("devices.json", "r", encoding="utf-8") as f:
        devices = json.load(f)

    updated_device = None
    for device in devices:
        if device['identifier'] == str(parameters.identifier):
            if parameters.name is not None:
                device['name'] = parameters.name
            if parameters.dependency_identifier is not None:
                device['dependency_identifier'] = str(parameters.dependency_identifier)
            device['last_update'] = datetime.now().isoformat()
            updated_device = device
            break

    dir_temp = os.path.dirname("devices.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(devices, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "devices.json")

    return updated_device

@device_router.delete("/{identifier}", response_model=DeviceResponse)
def disable_device(
    identifier: UUID,
    current_user = Depends(get_current_user)
):
    with open("roles.json", "r", encoding="utf-8") as f:
        roles = json.load(f)
        current_role = None
        for role in roles:
            if role['identifier'] == current_user['role_identifier']:
                current_role = role
                break
    if current_role['code'] != 'ADMIN':
        raise InvalidUserToken()
    
    devices = []
    with open("devices.json", "r", encoding="utf-8") as f:
        devices = json.load(f)

    disabled_device = None
    for device in devices:
        if device['identifier'] == str(identifier):
            device['enabled'] = False
            device['last_update'] = datetime.now().isoformat()
            disabled_device = device
            break

    dir_temp = os.path.dirname("devices.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(devices, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "devices.json")

    dependencies = []
    with open("dependencies.json", "r", encoding="utf-8") as f:
        dependencies = json.load(f)
        for dependency in dependencies:
            if dependency['identifier'] == disabled_device['dependency_identifier']:
                dependency['devices_count'] -= 1
                dependency['last_update'] = datetime.now().isoformat()
                break

    with open("dependencies.json", "w", encoding="utf-8") as tfd:
        json.dump(dependencies, tfd, ensure_ascii=False, indent=2)

    return disabled_device
