import os

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DIALECT = os.getenv("APP_DB_DIALECT")
    HOST = os.getenv("APP_DB_HOST")
    PORT = os.getenv("APP_DB_PORT")
    USER = os.getenv("APP_DB_USER")
    PASSWORD = os.getenv("APP_DB_PASSWORD")
    DATABASE = os.getenv("APP_DB_NAME")

    if DIALECT == "sqlite":
        URL = f"{DIALECT}:///{DATABASE}.sqlite3"
    else:
        URL = f"{DIALECT}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    class Config:
        env_file = ".env"


database_settings = DatabaseSettings()
