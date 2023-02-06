import uuid
from datetime import datetime

from pydantic.types import UUID, List

from app.inner.models.entities.type import Type
from app.outer.interfaces.controllers.requests.type_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.type_controller.patch_one_request import PatchOneRequest
from app.outer.repositories import type_repository


def read_all() -> List[Type]:
    return type_repository.read_all()


def read_one_by_id(id: UUID) -> Type:
    return type_repository.read_one_by_id(id)


def create_one(request: CreateOneRequest) -> Type:
    return create_many([request])[0]


def create_many(request: List[CreateOneRequest]) -> List[Type]:
    created_entities = []
    for one_request in request:
        entity = Type()
        entity.id = uuid.uuid4()
        entity.name = one_request.name
        entity.updated_at = datetime.now()
        entity.created_at = datetime.now()
        created_entity = type_repository.create_one(entity)
        created_entities.append(created_entity)

    return created_entities


def patch_one_by_id(id, request: PatchOneRequest) -> Type:
    entity = read_one_by_id(id)
    entity.name = request.name
    entity.updated_at = datetime.now()
    return type_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Type:
    return type_repository.delete_one_by_id(id)
