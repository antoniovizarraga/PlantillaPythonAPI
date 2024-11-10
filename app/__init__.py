from flask import Flask
from flask_jwt_extended import JWTManager
#from .cities.routes import citiesBP
from .usuarios.routes import usersBP
from .userslog.routes import personasBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave'
jwt = JWTManager(app)

#app.register_blueprint(citiesBP, url_prefix="/cities")
app.register_blueprint(usersBP, url_prefix="/usuarios")
app.register_blueprint(personasBP, url_prefix="/personas")