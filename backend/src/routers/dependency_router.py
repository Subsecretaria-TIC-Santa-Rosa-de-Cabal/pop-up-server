from datetime import datetime
import json
import os
import tempfile
from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from exceptions.fastapi_authentication_exceptions import InvalidUserToken
from exceptions.fastapi_dependency_exceptions import DependencyDeviceCountMustBeZero
from middlewares.auth_middleware import get_current_user
from schemas.dependency_schema import CreateDependencyParameters, DependencyResponse, UpdateDependencyParameters


dependency_router = APIRouter()

@dependency_router.get('/', response_model=List[DependencyResponse])
async def get_dependencies(
    current_user = Depends(get_current_user)
):
    dependencies = []
    with open("dependencies.json", "r", encoding="utf-8") as f:
        for dependency in json.load(f):
            if dependency['enabled'] is True:
                dependencies.append(dependency)
    return dependencies

@dependency_router.post('/', response_model=DependencyResponse)
async def create_dependency(
    parameters: CreateDependencyParameters,
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
    
    new_dependency = {
        "identifier": str(uuid4()),
        "enabled": True,
        "registration_date": datetime.now().isoformat(),
        "last_update": datetime.now().isoformat(),
        "name": parameters.name,
        "devices_count": 0
    }
    
    dependencies = []
    with open("dependencies.json", "r", encoding="utf-8") as f:
        dependencies = json.load(f)
    dependencies.append(new_dependency)

    dir_temp = os.path.dirname("dependencies.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(dependencies, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "dependencies.json")

    return new_dependency

@dependency_router.patch('/', response_model=DependencyResponse)
async def update_dependency(
    parameters: UpdateDependencyParameters,
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
    
    dependencies = []
    with open("dependencies.json", "r", encoding="utf-8") as f:
        dependencies = json.load(f)

    updated_dependency = None
    for dependency in dependencies:
        if dependency['identifier'] == str(parameters.identifier):
            dependency['name'] = parameters.name
            dependency['last_update'] = datetime.now().isoformat()
            updated_dependency = dependency
            break

    dir_temp = os.path.dirname("dependencies.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(dependencies, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "dependencies.json")

    return updated_dependency

@dependency_router.delete("/{identifier}", response_model=DependencyResponse)
def disable_dependency(
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
    
    dependencies = []
    with open("dependencies.json", "r", encoding="utf-8") as f:
        dependencies = json.load(f)

    disabled_dependency = None
    for dependency in dependencies:
        if dependency['identifier'] == str(identifier):
            if dependency['devices_count'] > 0:
                raise DependencyDeviceCountMustBeZero()
            dependency['enabled'] = False
            dependency['last_update'] = datetime.now().isoformat()
            disabled_dependency = dependency
            break

    dir_temp = os.path.dirname("dependencies.json") or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dir_temp, encoding="utf-8") as tf:
        json.dump(dependencies, tf, ensure_ascii=False, indent=2)
        temp_name = tf.name

    os.replace(temp_name, "dependencies.json")

    return disabled_dependency
