import os
from urllib.parse import quote
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql://root:%s@dbService:3306/telkom" % quote("P@ssw0rd")
SQLALCHEMY_TRACK_MODIFICATIONS = False