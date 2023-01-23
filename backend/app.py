from flask import Flask
from flask_migrate import Migrate
from Models.DB import db
import Controllers
from Routers.RouterONT import ONTBP
app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(ONTBP, url_prefix='/ont')

if __name__ == "__main__":
    app.run(debug=True)