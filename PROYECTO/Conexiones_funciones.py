import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import paramiko
import telnetlib3
import sys
import os
from cryptography.fernet import Fernet
import base64
import json
import re
import time

import Variables
import Perzonalizacion_botones
import Alertas

def Centro_conexiones(frame): 
    # Crear el contenedor principal 
    C_conexiones_p = tk.Frame(frame, bg=Variables.c_centros)
    C_conexiones_p.pack(side="top", fill="both", expand=True)

    # Línea de separación entre subframes C_conexiones1 y C_conexiones2
    separacion = tk.PanedWindow(C_conexiones_p, bg=Variables.c_lina_separacion, orient="vertical", sashwidth=30, sashrelief="sunken")
    separacion.pack(side="top", fill="both", expand=True)
    
    # Agregar dos frames al PanedWindow
    global C_conexiones2
    C_conexiones1 = tk.Frame(separacion, bg=Variables.c_barras)
    C_conexiones2 = tk.Frame(separacion, bg="black")
    separacion.add(C_conexiones1)
    separacion.add(C_conexiones2)

    ######################################################
    #   seccion opciones subframe 1  dispositivos        #
    ######################################################
    sub_frame1 = tk.Frame(C_conexiones1, bg=Variables.c_centros, width=210, height=280) #la altura de aqui depente la pocision inicial de la barra separacion!
    sub_frame1.pack(side="left", fill="both", expand=False)

    dispositivos = tk.Label(sub_frame1, text="Dispositivos", bg=Variables.c_centros, font=(Variables.poppins_negrita, 12))
    dispositivos.place(x=50, y=10, width=100) 

    texto_con_punto = "• Windows\n• Unix\n• Cisco\n    - Switches\n    - Routers\n• Huawei\n    - Switches\n    - Routers"
    label_with_bullet = tk.Label(sub_frame1, text=texto_con_punto, justify=tk.LEFT, bg=Variables.c_centros, font=(Variables.poppins, 10))
    label_with_bullet.place(x=25, y=35, width=100)

    dispositivos = tk.Label(sub_frame1, text="Conexiones", bg=Variables.c_centros, font=(Variables.poppins_negrita, 12))
    dispositivos.place(x=50, y=180, width=100) 

    texto_con_punto = "• Ssh\n• Telnet\n• PowerShell\n• WinRS/WinRM"
    label_with_bullet = tk.Label(sub_frame1, text=texto_con_punto, justify=tk.LEFT, bg=Variables.c_centros, font=(Variables.poppins, 10))
    label_with_bullet.place(x=35, y=200, width=100)

    separacion1 = tk.Frame(C_conexiones1, bg=Variables.c_lina_separacion, width=5)
    separacion1.pack(side="left", fill="y")

    ######################################################
    #   seccion opciones subframe 2 establecer Conexion  #
    ######################################################

    sub_frame2 = tk.Frame(C_conexiones1, bg=Variables.c_barras, width=600)
    sub_frame2.pack(side="left", fill="both", expand=False)

    dispositivos = tk.Label(sub_frame2, text="Establecer Conexion", bg=Variables.c_barras, font=(Variables.poppins_negrita, 12))
    dispositivos.place(x=230, y=10, width=200) 

    Perfil = tk.Label(sub_frame2, text="Perfil:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    Perfil.place(x=25, y=35) 
    global Perfil_entry
    Perfil_entry = tk.Entry(sub_frame2, bg="lightgray")
    Perfil_entry.place(x=100, y=36, width=145, height=20)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
        "Establece un nombre con el cual se guardara el perfil de la conexion.", 
        7, 36) 

    dispositivos = tk.Label(sub_frame2, text="Dispositivo:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    dispositivos.place(x=25, y=70) 
    opciones_dispositivos = ["Windows", "Unix", "Switch", "Router"]
    canal = tk.StringVar()
    global combo_dispositivos
    combo_dispositivos = ttk.Combobox(sub_frame2, textvariable=canal, values=opciones_dispositivos)
    combo_dispositivos.place(x=100, y=71)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, "Elejir un dispositivo.", 7, 71)

    Protocolo = tk.Label(sub_frame2, text="Protocolo:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    Protocolo.place(x=25, y=105) 
    opciones_Protocolo = ["Ssh", "Telnet", "PowerShell", "WinRS/WinRM"]
    canal = tk.StringVar()
    global combo_Protocolo
    combo_Protocolo = ttk.Combobox(sub_frame2, textvariable=canal, values=opciones_Protocolo)
    combo_Protocolo.place(x=100, y=106)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, "Elejir un protocolo de conexion.", 7, 106)

    Puerto = tk.Label(sub_frame2, text="Puerto:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    Puerto.place(x=25, y=140) 
    global Puerto_entry
    Puerto_entry = tk.Entry(sub_frame2, bg="lightgray")
    Puerto_entry.place(x=100, y=141, width=145, height=20)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
        "Ingresar el numero del puerto por defecto o por el cual corre el servicio.", 
        7, 141)

    host_ip = tk.Label(sub_frame2, text="Host/Ip:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    host_ip.place(x=25, y=175) 
    global host_ip_entry
    host_ip_entry = tk.Entry(sub_frame2, bg="lightgray")
    host_ip_entry.place(x=100, y=176, width=145, height=20)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
        "Ingresar la direccion IP o nombre del host destino.", 
        7, 176)

    usuario = tk.Label(sub_frame2, text="Usuario:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    usuario.place(x=25, y=205) 
    global usuario_entry
    usuario_entry = tk.Entry(sub_frame2, bg="lightgray")
    usuario_entry.place(x=100, y=206, width=145, height=20)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
        "Ingresar el usuario de la session.", 
        7, 206)

    password = tk.Label(sub_frame2, text="Contraseña:", bg=Variables.c_barras, font=(Variables.poppins, 10))
    password.place(x=25, y=245) 
    global password_entry
    password_entry = tk.Entry(sub_frame2, bg="lightgray", show="*")
    password_entry.place(x=100, y=246, width=145, height=20)
    Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
        "Ingresar la Contraseña del usuario de la session.", 
        7, 246)

    Boton_conectar = tk.Button(sub_frame2, text="Conectar", command=conectar, font=(Variables.poppins))
    Boton_conectar.place(x=400, y=45, width=100)
    Perzonalizacion_botones.selecion_boton(Boton_conectar)

    Boton_guardar = tk.Button(sub_frame2, text="Guardar", command=B_guardar, font=(Variables.poppins))
    Boton_guardar.place(x=400, y=90, width=100)
    Perzonalizacion_botones.selecion_boton(Boton_guardar)

    Boton_cargar = tk.Button(sub_frame2, text="Cargar", command=importar_desde_bin, font=(Variables.poppins))
    Boton_cargar.place(x=400, y=135, width=100)
    Perzonalizacion_botones.selecion_boton(Boton_cargar)

    Boton_limpiar = tk.Button(sub_frame2, text="Limpiar", command=limpiar_casillas, font=(Variables.poppins))
    Boton_limpiar.place(x=400, y=180, width=100)
    Perzonalizacion_botones.selecion_boton(Boton_limpiar)

    separacion2 = tk.Frame(C_conexiones1, bg=Variables.c_lina_separacion, width=5)
    separacion2.pack(side="left", fill="y")

    ######################################################
    #   seccion opciones subframe 2 hosts                #
    ######################################################

    sub_frame3 = tk.Frame(C_conexiones1, bg=Variables.c_barras, width=0)
    sub_frame3.pack(side="left", fill="both", expand=True)

    dispositivos = tk.Label(sub_frame3, text="Hosts", bg=Variables.c_barras, font=(Variables.poppins_negrita, 12))
    dispositivos.place(x=230, y=10, width=80) 

    ######################################################
    #   seccion opciones C_conexiones2                   #
    ######################################################
    return frame

def limpiar_casillas():# Función para limpiar todas las casillas de entrada
    perfil = Perfil_entry.get()
    dispositivo = combo_dispositivos.get()
    protocolo = combo_Protocolo.get()
    puerto = Puerto_entry.get()
    host_ip = host_ip_entry.get()
    usuario = usuario_entry.get()
    password = password_entry.get()
    # Verificar si todos los campos están completosor
    if perfil or dispositivo or protocolo or puerto or host_ip or usuario or password:
        Perfil_entry.delete(0, tk.END)
        Puerto_entry.delete(0, tk.END)
        host_ip_entry.delete(0, tk.END)
        usuario_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        combo_dispositivos.set("")
        combo_Protocolo.set("")
    else:
        Msg = "No se detectan valores en las celdas que limpiar"
        Alertas.alerta_ok(Variables.titulo, Variables.alerta_aviso, Msg)

def guardar_datos_cifrados(perfil, dispositivo, protocolo, puerto, host_ip, usuario, password, clave_maestra, archivo):
    cifrador = Fernet(clave_maestra)

    # Crear un diccionario con los datos
    datos_dict = {
        "perfil": perfil,
        "dispositivo": dispositivo,
        "protocolo": protocolo,
        "puerto": puerto,
        "host_ip": host_ip,
        "usuario": usuario,
        "password": password
    }

    # Convertir el diccionario a una cadena JSON
    datos_json = json.dumps(datos_dict)

    # Cifrar los datos
    datos_cifrados = cifrador.encrypt(datos_json.encode())

    # Guardar los datos cifrados en el archivo
    with open(archivo, "wb") as f:
        f.write(datos_cifrados)

def importar_desde_bin():
    try:
        # Abrir el explorador de archivos para seleccionar el archivo .bin
        archivo_bin = filedialog.askopenfilename(filetypes=[("Archivos Binarios", "*.bin")])

        # Asegúrate de que la clave sea de 32 bytes
        if len(Variables.Clave_maestra) != 32:
            raise ValueError("La clave maestra debe ser de 32 bytes")

        # Codificar en base64 para obtener la clave Fernet válida
        clave_maestra_codificada = base64.urlsafe_b64encode(Variables.Clave_maestra)

        # Crear el objeto Fernet con la clave codificada
        cifrador = Fernet(clave_maestra_codificada)

        # Leer datos cifrados desde el archivo
        with open(archivo_bin, 'rb') as file:
            datos_cifrados = file.read()

        # Descifrar los datos
        datos_descifrados = cifrador.decrypt(datos_cifrados)

        # Convertir los datos desde formato JSON a un diccionario
        datos_dict = json.loads(datos_descifrados.decode('utf-8'))

        # Obtener valores del diccionario
        perfil = datos_dict.get('perfil', '')
        dispositivo = datos_dict.get('dispositivo', '')
        protocolo = datos_dict.get('protocolo', '')
        puerto = datos_dict.get('puerto', '')
        host_ip = datos_dict.get('host_ip', '')
        usuario = datos_dict.get('usuario', '')
        password = datos_dict.get('password', '')

        # Actualizar las variables de la interfaz gráfica con los valores obtenidos
        Perfil_entry.delete(0, 'end')
        Perfil_entry.insert(0, perfil)
        combo_dispositivos.set(dispositivo)
        combo_Protocolo.set(protocolo)
        Puerto_entry.delete(0, 'end')
        Puerto_entry.insert(0, puerto)
        host_ip_entry.delete(0, 'end')
        host_ip_entry.insert(0, host_ip)
        usuario_entry.delete(0, 'end')
        usuario_entry.insert(0, usuario)
        password_entry.delete(0, 'end')
        password_entry.insert(0, password)


    except Exception as e:
        print(f"Error al importar desde archivo binario: {e}")

def filter_ansi_escape(text):
    # Filtrar las secuencias de escape ANSI
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def B_guardar():
    perfil = Perfil_entry.get()
    dispositivo = combo_dispositivos.get()
    protocolo = combo_Protocolo.get()
    puerto = Puerto_entry.get()
    host_ip = host_ip_entry.get()
    usuario = usuario_entry.get()
    password = password_entry.get()
    # Verificar si todos los campos están completos
    if perfil and dispositivo and protocolo and puerto and host_ip and usuario and password:
        archivo = f"{perfil}.bin"
        rutacompleta = os.path.join(Variables.ruta_escritorio, archivo)
        guardar_datos_cifrados(perfil, dispositivo, protocolo, puerto, host_ip, usuario, password, Variables.clave_maestra, rutacompleta)
        Msg = f"Perfil de sesión guardado correctamente, en la ruta: {rutacompleta}, se guardan de forma encriptada asi que estara seguro!"
        Alertas.alerta_Amarilla(Variables.titulo, Variables.alerta_aviso, Msg)
    else:
        Msg = f"Te falta completar algunos campos antes de guardar el perfil"
        Alertas.alerta_Amarilla(Variables.titulo, Variables.alerta_aviso, Msg)

def conectar():
    perfil = Perfil_entry.get()
    dispositivo = combo_dispositivos.get()
    protocolo = combo_Protocolo.get()
    puerto = Puerto_entry.get()
    host_ip = host_ip_entry.get()
    usuario = usuario_entry.get()
    password = password_entry.get()

    # Verificar si todos los campos están completos
    if perfil and dispositivo and protocolo and puerto and host_ip and usuario and password:
        app = SSHShellUI(C_conexiones2)
    else:
        Msg = "Diligencie los campos necesarios para su tipo de conexion"
        Alertas.alerta_Amarilla(Variables.titulo, Variables.alerta_aviso, Msg)

class SSHShellUI:
    def __init__(self, master):

        self.master = master

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=20, bg="black", foreground="green")
        self.text_area.pack(expand=True, fill="both")

        self.etiqueta = tk.Label(master, text="Ingresar comando", foreground="white", background="black", font=("Arial", 10))
        self.etiqueta.pack(side="left", padx=5, pady=5)

        self.entry = tk.Entry(master, width=80, font=("Arial", 10), bg="white", foreground="black")
        self.entry.pack(side="left", padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Limpiar OutPut", command=self.limpiar_texto, font=("Arial", 10))
        self.clear_button.pack(side="left", padx=5, pady=5)

        self.entry.bind("<Return>", self.enviar_comando)  # Asociar la tecla Enter a la función enviar_comando

        self.ssh = self.iniciar_sesion_ssh()  # Iniciar la sesión SSH al inicializar la clase

    def iniciar_sesion_ssh(self):
        perfil = Perfil_entry.get()
        dispositivo = combo_dispositivos.get()
        protocolo = combo_Protocolo.get()
        puerto = Puerto_entry.get()
        host_ip = host_ip_entry.get()
        usuario = usuario_entry.get()
        Password = password_entry.get()
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host_ip, port=puerto, username=usuario, password=Password)
            self.text_area.insert(tk.END, "Conexión SSH establecida.\n", "output")
            limpiar_casillas()
            return ssh_client
        except Exception as e:
            self.text_area.insert(tk.END, f"Error al establecer conexión SSH: {e}\n")
            return None

    def ejecutar_comando_interactivo(self, comando):
        try:
            if self.ssh:
                # Abrir un canal "shell" interactivo
                channel = self.ssh.invoke_shell()

                # Enviar el comando
                channel.send(comando + '\n')

                # Configurar el canal para recibir datos no bloqueantes
                channel.setblocking(0)

                while True:
                    # Esperar a que el canal esté listo para recibir datos
                    while not channel.recv_ready():
                        self.master.update_idletasks()
                        time.sleep(0.1)

                    # Recibir y mostrar la salida del comando
                    output = channel.recv(1024).decode()
                    if not output:
                        break

                    self.text_area.insert(tk.END, output)
                    self.text_area.yview(tk.END)
                    self.master.update_idletasks()

                # Cerrar el canal
                channel.close()

        except Exception as e:
            self.text_area.insert(tk.END, f"Error al ejecutar comando: {e}\n")

    def enviar_comando(self, event):
        comando_usuario = self.entry.get()
        if comando_usuario.lower() == 'exit':
            self.cerrar_sesion_ssh()
            self.master.destroy()
            return

        self.ejecutar_comando_interactivo(comando_usuario)
        self.entry.delete(0, tk.END)

    def cerrar_sesion_ssh(self):
        try:
            if self.ssh is not None and self.ssh.get_transport().is_active():
                self.ssh.close()
        except Exception as e:
            print(f"Error al cerrar la sesión SSH: {e}")

    def limpiar_texto(self):
        self.text_area.delete(1.0, tk.END)