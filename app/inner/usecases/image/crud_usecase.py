import uuid
from datetime import datetime

from pydantic.types import UUID, List

from app.inner.models.entities.image import Image
from app.outer.interfaces.controllers.requests.image_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.image_controller.patch_one_request import PatchOneRequest
from app.outer.repositories import image_repository


def read_all() -> List[Image]:
    return image_repository.read_all()


def read_one_by_id(id: UUID) -> Image:
    return image_repository.read_one_by_id(id)


def create_one(request: CreateOneRequest) -> Image:
    return create_many([request])[0]


def create_many(request: List[CreateOneRequest]) -> List[Image]:
    created_entities = []
    for one_request in request:
        entity = Image()
        entity.id = uuid.uuid4()
        entity.file_name = one_request.file_name
        entity.file = one_request.file
        entity.updated_at = datetime.now()
        entity.created_at = datetime.now()
        created_entity = image_repository.create_one(entity)
        created_entities.append(created_entity)

    return created_entities


def patch_one_by_id(id, request: PatchOneRequest) -> Image:
    entity = read_one_by_id(id)
    entity.file_name = request.file_name
    entity.file = request.file
    entity.updated_at = datetime.now()
    return image_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Image:
    return image_repository.delete_one_by_id(id)
