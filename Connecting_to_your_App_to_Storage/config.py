import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "1749a1aee826464b0aac8da8ee758df044af78b586320eedd72c9c2cb276c886")

    SQL_SERVER = os.getenv("SQL_SERVER", "exercise2server.database.windows.net")
    SQL_DATABASE = os.getenv("SQL_DATABASE", "exercise2")
    SQL_USER_NAME = os.getenv("SQL_USER_NAME", "exercise2")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD", "Mohdjamil$123")

    DRIVER = os.getenv("ODBC_DRIVER", "ODBC Driver 18 for SQL Server")

    # Build full ODBC connection string
    odbc_str = (
        f"Driver={{{DRIVER}}};"
        f"Server=tcp:{SQL_SERVER},1433;"
        f"Database={SQL_DATABASE};"
        f"Uid={SQL_USER_NAME};"
        f"Pwd={SQL_PASSWORD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    # URL‑encode and pass via odbc_connect
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(odbc_str)
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure storage
    BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT", "exercise2storageaccount")
    BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY", "Kt99b08PC3U66phkHQ+nRoExgmb2X59qwV4GGvlkI/Lda2Kyb7AAKorw6omepw9TFiVcEjg8KWAa+AStFZz5hg==")
    BLOB_CONTAINER = os.getenv("BLOB_CONTAINER", "images")
