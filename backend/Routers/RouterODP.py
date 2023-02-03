from flask import Blueprint
from Controllers.ControllerODP import storeDataFrame

ODP = Blueprint('ODP', __name__)
ODP.route('/', methods=['POST'])(storeDataFrame)
