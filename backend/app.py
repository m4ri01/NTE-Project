from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
from Models.DB import db
import Controllers
from Routers.RouterONT import ONTBP
from Routers.RouterODP import ODP
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config.from_object('config')
CORS(app,
  resources={r'/*': {"origins": '*'} }
)
app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(ONTBP, url_prefix='/ont')
app.register_blueprint(ODP, url_prefix='/odp')

if __name__ == "__main__":
    app.run(debug=True)