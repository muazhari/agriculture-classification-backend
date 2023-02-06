from fastapi import APIRouter
from pydantic.types import UUID, List

from app.inner.models.entities.type import Type
from app.inner.usecases.type import crud_usecase
from app.outer.interfaces.controllers.requests.type_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.type_controller.patch_one_request import PatchOneRequest
from app.outer.interfaces.controllers.responses.Content import Content

router = APIRouter(
    prefix="/types",
    tags=["types"]
)


@router.get("/", response_model=Content[List[Type]])
async def read_all() -> Content[List[Type]]:
    content = Content[List[Type]](
        message="Read all type succeed.",
        data=crud_usecase.read_all()
    )
    return content


@router.get("/{id}", response_model=Content[Type])
async def read_one_by_id(id: UUID) -> Content[Type]:
    content = Content[Type](
        message="Read one type succeed.",
        data=crud_usecase.read_one_by_id(id)
    )
    return content


@router.post("/", response_model=Content[Type])
async def create_one(request: CreateOneRequest) -> Content[Type]:
    content = Content[Type](
        message="Create one type succeed.",
        data=crud_usecase.create_one(request)
    )
    return content


@router.post("/many", response_model=Content[List[Type]])
async def create_many(request: List[CreateOneRequest]) -> Content[List[Type]]:
    content = Content[List[Type]](
        message="Create many type succeed.",
        data=crud_usecase.create_many(request)
    )
    return content


@router.patch("/{id}", response_model=Content[Type])
async def patch_one_by_id(id: UUID, request: PatchOneRequest) -> Content[Type]:
    content = Content[Type](
        message="Patch one type succeed.",
        data=crud_usecase.patch_one_by_id(id, request)
    )
    return content


@router.delete("/{id}", response_model=Content[Type])
async def delete_one_by_id(id: UUID) -> Content[Type]:
    content = Content[Type](
        message="Delete one type succeed.",
        data=crud_usecase.delete_one_by_id(id)
    )
    return content
