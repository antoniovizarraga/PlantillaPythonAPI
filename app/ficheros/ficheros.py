from flask import *


def leeArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    usuarios = json.load(archivo)
    archivo.close()
    return usuarios

def escribeArchivo(usuarios, rutaArchivo):
    archivo = open(rutaArchivo, "w")
    json.dump(usuarios, archivo)
    archivo.close()