import tkinter as tk
from tkinter import font


ventana = tk.Tk()
ventana.title("Estilos de Fuente")

# Ruta al archivo de la fuente personalizada
ruta_fuente = "lib/Data/fuente/poppins.ttf"

# Cargar la fuente personalizada
fuente_personalizada = font.Font(family="Popins", size=12, weight="bold")


# Negrita
label_negrita = tk.Label(ventana, text="Texto en negrita", font=(fuente_personalizada))
label_negrita.pack(pady=10)


ventana.mainloop()
