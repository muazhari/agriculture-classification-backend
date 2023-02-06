from fastapi import APIRouter
from pydantic.types import UUID, List

from app.inner.models.entities.classification import Classification
from app.inner.usecases.classification import crud_usecase
from app.outer.interfaces.controllers.requests.classification_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.classification_controller.patch_one_request import PatchOneRequest
from app.outer.interfaces.controllers.responses.Content import Content

router = APIRouter(
    prefix="/classifications",
    tags=["classifications"]
)


@router.get("/", response_model=Content[List[Classification]])
async def read_all() -> Content[List[Classification]]:
    content = Content[List[Classification]](
        message="Read all classification succeed.",
        data=crud_usecase.read_all()
    )
    return content


@router.get("/{id}", response_model=Content[Classification])
async def read_one_by_id(id: UUID) -> Content[Classification]:
    content = Content[Classification](
        message="Read one classification succeed.",
        data=crud_usecase.read_one_by_id(id)
    )
    return content


@router.post("/", response_model=Content[Classification])
async def create_one(request: CreateOneRequest) -> Content[Classification]:
    content = Content[Classification](
        message="Create one classification succeed.",
        data=crud_usecase.create_one(request)
    )
    return content


@router.post("/many", response_model=Content[List[Classification]])
async def create_many(request: List[CreateOneRequest]) -> Content[List[Classification]]:
    content = Content[List[Classification]](
        message="Create many classification succeed.",
        data=crud_usecase.create_many(request)
    )
    return content


@router.patch("/{id}", response_model=Content[Classification])
async def patch_one_by_id(id: UUID, request: PatchOneRequest) -> Content[Classification]:
    content = Content[Classification](
        message="Patch one classification succeed.",
        data=crud_usecase.patch_one_by_id(id, request)
    )
    return content


@router.delete("/{id}", response_model=Content[Classification])
async def delete_one_by_id(id: UUID) -> Content[Classification]:
    content = Content[Classification](
        message="Delete one classification succeed.",
        data=crud_usecase.delete_one_by_id(id)
    )
    return content
