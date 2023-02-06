import base64
import os
import uuid
from datetime import datetime

from autogluon.multimodal import MultiModalPredictor
from pydantic.types import UUID, List

from app.inner.models.entities.classification import Classification
from app.inner.models.entities.type import Type
from app.inner.usecases.image import crud_usecase as image_crud_usecase
from app.inner.usecases.type import crud_usecase as type_crud_usecase
from app.outer.interfaces.controllers.requests.classification_controller.create_one_request import \
    CreateOneRequest
from app.outer.interfaces.controllers.requests.classification_controller.patch_one_request import PatchOneRequest
from app.outer.repositories import classification_repository


def fix_path(path):
    return os.path.abspath(os.path.expanduser(path))


def read_all() -> List[Classification]:
    return classification_repository.read_all()


def read_one_by_id(id: UUID) -> Classification:
    return classification_repository.read_one_by_id(id)


def get_autogluon_model_path(current_path: str, type_id: UUID):
    found_type: Type = type_crud_usecase.read_one_by_id(type_id)
    if found_type.name == "plant_disease":
        path = fix_path(f"{current_path}/autogluon_models/ag-20230202_111718")
    elif found_type.name == "fruit_quality":
        path = fix_path(f"{current_path}/autogluon_models/ag-20221215_054846")
    else:
        raise ValueError(f"Type {found_type} not supported.")
    return path


def create_one(request: CreateOneRequest) -> Classification:
    created_entity = create_many([request])[0]
    return created_entity


def create_many(request: List[CreateOneRequest]) -> List[Classification]:
    file_paths = []
    entities = []
    current_path = fix_path(f"{os.getcwd()}/app/inner/usecases/classification")
    for one_request in request:
        entity = Classification()
        entity.id = uuid.uuid4()
        entity.type_id = one_request.type_id
        entity.image_id = one_request.image_id
        entity.updated_at = datetime.now()
        entity.created_at = datetime.now()
        entities.append(entity)

        file_path = fix_path(f"{current_path}/image_temp/{str(one_request.image_id)}")
        file_paths.append(file_path)
        with open(file_path, "wb") as file:
            image = image_crud_usecase.read_one_by_id(one_request.image_id)
            decoded_image_file = base64.urlsafe_b64decode(image.file)
            file.write(decoded_image_file)
            file.close()

    predictor = MultiModalPredictor(
        label="label"
    ).load(
        path=get_autogluon_model_path(current_path, request[0].type_id)
    )
    prediction_probability = predictor.predict_proba({'image': file_paths}, as_pandas=True)

    created_entities = []
    for index, value in enumerate(zip(entities, file_paths)):
        entity, file_path = value
        entity.result = prediction_probability.iloc[[index], :].to_json(orient="records")
        created_entity = classification_repository.create_one(entity)
        created_entities.append(created_entity)

        if os.path.exists(file_path):
            os.remove(file_path)

    return created_entities


def patch_one_by_id(id, request: PatchOneRequest) -> Classification:
    entity = classification_repository.read_one_by_id(id)
    entity.image_id = request.image_id
    entity.type_id = request.type_id
    entity.result = request.result
    entity.updated_at = datetime.now()
    return classification_repository.patch_one_by_id(id, entity)


def delete_one_by_id(id) -> Classification:
    return classification_repository.delete_one_by_id(id)
