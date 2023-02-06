from sqlmodel import create_engine, Session

from app.outer.configs.database_config import database_settings

engine = create_engine(
    database_settings.URL,
    echo=False
)


def create_session():
    with Session(engine) as session:
        return session
