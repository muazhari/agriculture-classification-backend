from fastapi import APIRouter
from pydantic.types import UUID, List

from app.inner.models.entities.image import Image
from app.inner.usecases.image import crud_usecase
from app.outer.interfaces.controllers.requests.image_controller.create_one_request import CreateOneRequest
from app.outer.interfaces.controllers.requests.image_controller.patch_one_request import PatchOneRequest
from app.outer.interfaces.controllers.responses.Content import Content

router = APIRouter(
    prefix="/images",
    tags=["images"]
)


@router.get("/", response_model=Content[List[Image]])
async def read_all() -> Content[List[Image]]:
    content = Content[List[Image]](
        message="Read all image succeed.",
        data=crud_usecase.read_all()
    )
    return content


@router.get("/{id}", response_model=Content[Image])
async def read_one_by_id(id: UUID) -> Content[Image]:
    content = Content[Image](
        message="Read one image succeed.",
        data=crud_usecase.read_one_by_id(id)
    )
    return content


@router.post("/", response_model=Content[Image])
async def create_one(request: CreateOneRequest) -> Content[Image]:
    content = Content[Image](
        message="Create one image succeed.",
        data=crud_usecase.create_one(request)
    )
    return content


@router.post("/many", response_model=Content[List[Image]])
async def create_many(request: List[CreateOneRequest]) -> Content[List[Image]]:
    content = Content[List[Image]](
        message="Create one image succeed.",
        data=crud_usecase.create_many(request)
    )
    return content


@router.patch("/{id}", response_model=Content[Image])
async def patch_one_by_id(id: UUID, request: PatchOneRequest) -> Content[Image]:
    content = Content[Image](
        message="Patch one image succeed.",
        data=crud_usecase.patch_one_by_id(id, request)
    )
    return content


@router.delete("/{id}", response_model=Content[Image])
async def delete_one_by_id(id: UUID) -> Content[Image]:
    content = Content[Image](
        message="Delete one image succeed.",
        data=crud_usecase.delete_one_by_id(id)
    )
    return content
