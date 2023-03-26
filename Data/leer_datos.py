"""
Módulo para leer los datos de los clientes desde un archivo excel
"""
import pandas as pd
from Model.Cliente import Cliente
from datetime import *


def cargar_clientes(clientes):
    lista = []
    for row in clientes.iterrows():
        cliente = Cliente(row[1].values[0], row[1].values[1], str(row[1].values[2]).split(' ')[0])
        if validar_fecha(cliente.fecha_nacimiento):
            lista.append(cliente)
    return lista


def validar_fecha(fecha):
    fecha = fecha.split('-')
    return datetime.now().month == int(fecha[1]) and datetime.now().day == int(fecha[2])


sheet = pd.read_excel(r"Data/clientes.xls", sheet_name="Clientes")

lista_clientes = cargar_clientes(sheet)


