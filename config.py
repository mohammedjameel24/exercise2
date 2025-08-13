import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "")

    SQL_SERVER = os.getenv("SQL_SERVER", "")
    SQL_DATABASE = os.getenv("SQL_DATABASE", "")
    SQL_USER_NAME = os.getenv("SQL_USER_NAME", "")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD", "")

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
        "Connection Timeout=100;"
    )

    # URL‑encode and pass via odbc_connect
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc:///?odbc_connect=" + urllib.parse.quote_plus(odbc_str)
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure storage
    BLOB_ACCOUNT = os.getenv("BLOB_ACCOUNT", "")
    BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY", "")
    BLOB_CONTAINER = os.getenv("BLOB_CONTAINER", "")
