from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
from Models.DB import db
import Controllers
from Routers.RouterONT import ONTBP
app = Flask(__name__)
app.config.from_object('config')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(ONTBP, url_prefix='/ont')

if __name__ == "__main__":
    app.run(debug=True)