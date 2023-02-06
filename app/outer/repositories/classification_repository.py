from pydantic.types import UUID
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select

from app.inner.models.entities.classification import Classification
from app.outer.interfaces.databases.db import create_session


def read_all():
    with create_session() as session:
        return session.exec(select(Classification)).all()


def read_one_by_id(id: UUID):
    with create_session() as session:
        found_entity = session.exec(select(Classification).where(Classification.id == id)).first()

        if found_entity is None:
            raise Exception("Entity not found.")

        return found_entity


def create_one(entity: Classification):
    with create_session() as session:
        try:
            session.add(entity)
            session.commit()
            session.refresh(entity)
        except SQLAlchemyError as e:
            raise e
    return entity


def patch_one_by_id(id: UUID, entity: Classification):
    with create_session() as session:
        try:
            found_entity = session.exec(select(Classification).where(Classification.id == id)).first()
        except SQLAlchemyError as e:
            raise e

        if found_entity is None:
            raise Exception("Entity not found.")

        found_entity.id = entity.id
        found_entity.image_id = entity.image_id
        found_entity.result = entity.result
        found_entity.created_at = entity.created_at
        found_entity.updated_at = entity.updated_at

        try:
            session.commit()
            session.refresh(found_entity)
        except SQLAlchemyError as e:
            raise e

        return found_entity


def delete_one_by_id(id: UUID):
    with create_session() as session:
        try:
            found_entity = session.exec(select(Classification).where(Classification.id == id)).first()
        except SQLAlchemyError as e:
            raise e

        if found_entity is None:
            raise Exception("Entity not found.")

        try:
            session.delete(found_entity)
            session.commit()
        except SQLAlchemyError as e:
            raise e

        return found_entity
