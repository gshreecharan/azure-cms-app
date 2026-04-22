import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    #  BLOB STORAGE
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsimagescharan123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'YOUR_STORAGE_KEY'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    #  SQL DATABASE
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-server-12345.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin123'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'YOUR_PASSWORD'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://{}:{}@{}:1433/{}?driver=ODBC+Driver+17+for+SQL+Server'
        .format(SQL_USER_NAME, SQL_PASSWORD, SQL_SERVER, SQL_DATABASE)
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  MICROSOFT AUTH
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'YOUR_CLIENT_SECRET'
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'YOUR_CLIENT_ID'

    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"