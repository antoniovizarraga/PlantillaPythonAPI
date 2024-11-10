from flask import Blueprint, jsonify
from ..ficheros.ficheros import *
from flask_jwt_extended import jwt_required

usersBP = Blueprint('usuarios', __name__)

# Funciones extras
rutaFichero = "./app/usuarios/usuarios.json"
usuarios = leeArchivo("./app/usuarios/usuarios.json")

def find_next_id():
    return max(usuario["id"] for usuario in usuarios) + 1



# Métodos GET

@usersBP.get('/')
def get_usuarios():
    usuarios = leeArchivo(rutaFichero)
    return jsonify(usuarios)

@usersBP.get('/<int:id>')
def get_usuario(id):
    usuarios = leeArchivo(rutaFichero)
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario, 200
    return {"error": "User not found"}, 404

# Método POST

@usersBP.post('/')
@jwt_required()
def add_usuario():
    usuarios = leeArchivo(rutaFichero)
    if request.is_json:
        usuario = request.get_json()

        usuario["id"] = find_next_id()

        usuarios.append(usuario)
        escribeArchivo(usuarios, rutaFichero)

        return usuario, 201
    return {"error": "Request must be JSON"}, 415


# Métodos PUT y PATCH (Como el profesor aquí ponga que hagamos algo más específico en los campos del put y el patch, me cago en todo)

@usersBP.put("/<int:id>")
@usersBP.patch("/<int:id>")
@jwt_required()
def modify_user(id):
    if request.is_json:

        newUsuario = request.get_json()

        for usuario in usuarios:
            if usuario["id"] == id:
                for element in newUsuario:
                    usuario[element] = newUsuario[element]
                return usuario, 200
    return {"error":"Request must be JSON"}, 415


# Método DELETE

@usersBP.delete("/<int:id>")
@jwt_required()
def delete_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return "{}", 200
    return {"error":"Usuario not found"}, 404

