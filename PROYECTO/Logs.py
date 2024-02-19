import os
import logbook
import Variables

Fecha = Variables.fecha
Hora = Variables.hora

def configurar_logs(log_doc):
    # Configurar el archivo de logs
    logbook.FileHandler(log_doc).push_application()

def agregar_log(mensaje):
    mensaje_completo = f"[{Fecha} {Hora}] - {mensaje}"
    logbook.info(mensaje_completo)
