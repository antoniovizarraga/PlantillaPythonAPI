from flask import *
from flask_jwt_extended import JWTManager
from app import app





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)