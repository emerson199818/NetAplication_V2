import tkinter as tk

import Variables
import Home_funciones
import Wireless_funciones
import Conexiones_funciones
from Logs import agregar_log

def mostrar_opciones(event):
    global menu_visible

    # Obtener la posición del Label
    x = Variables.root.winfo_rootx() + event.widget.winfo_x()
    y = Variables.root.winfo_rooty() + event.widget.winfo_y() + event.widget.winfo_height() + 0

    Variables.root.after(200, lambda: menu.post(x, y))
    menu_visible = True

def mostrar_ocultar_menu(event):
    global menu_visible

    # Si el menú no está visible, lo mostramos
    if not menu_visible:
        mostrar_opciones(event)
    # Si el menú está visible, no lo mostramos
    else:
        menu.unpost()
        menu_visible = False

def B_ayuda(event): #boton ayuda habre nueva ventana ayuda
    Msg = "Se abrio ventana de menu ayuda"
    agregar_log(Msg)
    Ayuda= tk.Toplevel()
    Ayuda.title("Ayuda") #Titulo
    Ayuda.iconbitmap(Variables.icono_v) #icono
    n_ancho_ayuda = Variables.ancho_p // 3
    n_alto_ayuda = Variables.alto_p // 3
    Ayuda.geometry(f"{n_ancho_ayuda}x{n_alto_ayuda}") #aplicar zise a ventana
    Ayuda.resizable(0,0) #bloquear tamaño ventana
    tk.Label(Ayuda, text="¡AYUDA!").pack()

def B_wireless():
    cambio_ventana(Wireless_funciones.Centro_wireless, Home_funciones.Centro_p)

def B_home(event):
    cambio_ventana(Home_funciones.Centro_principal, Home_funciones.Centro_p)

def B_conexiones(event):
    cambio_ventana(Conexiones_funciones.Centro_conexiones, Home_funciones.Centro_p)

def cambio_ventana(ventana_factory, frame):
    # Destruir el contenido actual del frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Crear un nuevo frame utilizando la función proporcionada
    ventana = ventana_factory(frame)
    ventana.pack(side="top", fill="both", expand=True)
    Msg = f"se cambio de ventana {frame} a {ventana}"
    agregar_log(Msg)


#####################################
    #Sub menu boton Monitores 
#####################################
# Menu boton Monitores
menu = tk.Menu(Variables.root, tearoff=0)
menu.add_command(label="WireLess Monitor", command=B_wireless, font=(Variables.poppins, 10))#se llama a la funcion Wireless
menu.add_command(label="Battery Monitor", font=(Variables.poppins, 10)) #por hacer
menu.add_command(label="Ram Monitor", font=(Variables.poppins, 10)) #por hacer

#########################################################
    #funciones mostrar/ocultar Botones Barra_superior 
#########################################################

menu_visible = False #inicializar menu como falso