import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")

    SQL_SERVER = os.getenv("SQL_SERVER", "localhost")
    SQL_DATABASE = os.getenv("SQL_DATABASE", "animals")
    SQL_USER_NAME = os.getenv("SQL_USER_NAME", "sa")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD", "password")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure storage
    BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT", "account-name")
    BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY", "storage-key")
    BLOB_CONTAINER = os.getenv("BLOB_CONTAINER", "container-name")
