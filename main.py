"""
Programa para enviar mensajes de cumpleaños a clientes por wpp automatizados recibiendo
los datos desde un archivo de excel utilizando libreria pandas y pywhatkit.
"""
from Data.leer_datos import *
from Feature.enviar_mensajes import *


def main():
    enviar_mensajes(lista_clientes)


if __name__ == '__main__':
    main()

