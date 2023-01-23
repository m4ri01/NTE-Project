import os
from urllib.parse import quote
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql://root:%s@db:3306/telkom" % quote("P@ssw0rd")
SQLALCHEMY_TRACK_MODIFICATIONS = False