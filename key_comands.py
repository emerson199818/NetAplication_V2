import keyboard
import pyperclip
import Wireless_funciones
import win32gui

# Obtener el título de la ventana en primer plano
def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def on_key_event(e):
    # Verificar si la ventana en primer plano es "netaplication"
    if get_active_window_title() == "NetAplication_v2" and keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
        # Tu código para copiar los datos
        elementos_seleccionados = Wireless_funciones.view_data.selection()
        datos_a_copiar = []
        for elemento in elementos_seleccionados:
            valores_elemento = Wireless_funciones.view_data.item(elemento, "values")
            datos_a_copiar.append("\t".join(map(str, valores_elemento)))

        datos_copiados = "\n".join(datos_a_copiar)
        pyperclip.copy(datos_copiados)