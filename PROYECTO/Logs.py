import os
import logging
from _t_d import fecha_dia, hora

Fecha, Dia = fecha_dia()
Hora = hora()

def configurar_logs(nombre_archivo):
    # Configurar el archivo de logs
    logging.basicConfig(filename=nombre_archivo, level=logging.INFO, format='%(message)s')

def agregar_log(mensaje):
    mensaje_completo = f"[{Fecha} {Hora}] - {mensaje}"
    logging.info(mensaje_completo)
