from flask import Blueprint
from Controllers.ControllerONT import store, read

ONTBP = Blueprint('ONTBP', __name__)
ONTBP.route('/', methods=['POST'])(store)
ONTBP.route('/', methods=['GET'])(read)
