"""
Model Cliente
"""


class Cliente:
    def __init__(self, nombre, numero, fecha_nacimiento):
        self.nombre = nombre
        self.numero = numero
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Nombre: {self.nombre}, Numero: {self.numero}, Fecha de Nacimiento: {self.fecha_nacimiento}'
