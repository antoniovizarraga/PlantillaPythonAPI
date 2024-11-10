from flask import Blueprint, request, jsonify
import bcrypt
from ..ficheros.ficheros import *
from flask_jwt_extended import create_access_token

ficheroUsuarios = "./app/userslog/users.json"

personasBP = Blueprint('personas', __name__)

usersapp = leeArchivo(ficheroUsuarios)


# No sé




# Métodos GET

@personasBP.get('/')
def loginUser():
    usersapp = leeArchivo(ficheroUsuarios)
    if request.is_json:
        user = request.get_json()

        username = user['username']
        password = user['password'].encode('utf-8')

        for userFile in usersapp:
            if userFile['username'] == username:
                passwordFile = userFile['password']

                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=username)
                    return {'token': token}, 200
                else:
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415



# Método POST

@personasBP.post('/')
def registerUser():
    usersapp = leeArchivo(ficheroUsuarios)

    if request.is_json:

        user = request.get_json()


        password = user['password'].encode('UTF-8')

        salt = bcrypt.gensalt()

        hashPassword = bcrypt.hashpw(password, salt).hex()
        user['password'] = hashPassword
        usersapp.append(user)
        escribeArchivo(usersapp, ficheroUsuarios)

        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415





