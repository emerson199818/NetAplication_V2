import pyautogui
import subprocess
import time

# Abrir el Panel de control de Windows
subprocess.Popen('control.exe', shell=True)
time.sleep(1)  # Esperar a que se abra el Panel de control

# Seleccionar "Sistema y seguridad"
pyautogui.write('Sistema y seguridad')
pyautogui.press('enter')
time.sleep(1)  # Esperar a que se abra la opción "Sistema y seguridad"

# Seleccionar "Sistema"
pyautogui.write('Sistema')
pyautogui.press('enter')
time.sleep(1)  # Esperar a que se abra la opción "Sistema"

# Seleccionar "Configuración remota"
pyautogui.write('Configuración remota')
pyautogui.press('enter')
time.sleep(1)  # Esperar a que se abra la opción "Configuración remota"

# En la pestaña "Control remoto", seleccionar "Permitir conexiones de asistencia remota a este equipo" y "Permitir conexiones remotas a este equipo"
# (Aquí es donde el script simularía hacer clic en las casillas correspondientes)

# Cerrar el Panel de control
pyautogui.hotkey('alt', 'f4')
