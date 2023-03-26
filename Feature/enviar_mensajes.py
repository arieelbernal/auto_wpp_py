"""
Módulo para enviar los mensajes automatizados
"""
import time

import pywhatkit as wk


def enviar_mensajes(clientes):
    for cliente in clientes:
        wk.sendwhatmsg_instantly(f'+{cliente.numero}'
                                 , f'{cliente.nombre} '
                                   f'te deseamos un feliz cumpleaños, '
                                   f'de parte de la pelu!'
                                 , 12
                                 , True
                                 , 12
                                 )
        time.sleep(5)

