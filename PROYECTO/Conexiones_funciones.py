import tkinter as tk

import Variables
import Perzonalizacion_botones

def Centro_conexiones(frame): 
	# Crear el contenedor principal 
	C_conexiones_p = tk.Frame(frame, bg=Variables.c_centros)
	C_conexiones_p.pack(side="top", fill="both", expand=True)

	# Línea de separación entre subframes C_conexiones1 y C_conexiones2
	separacion = tk.PanedWindow(C_conexiones_p, bg=Variables.c_lina_separacion, orient="vertical", sashwidth=30, sashrelief="sunken")
	separacion.pack(side="top", fill="both", expand=True)
	
	# Agregar dos frames al PanedWindow
	C_conexiones1 = tk.Frame(separacion, bg=Variables.c_barras)
	C_conexiones2 = tk.Frame(separacion, bg=Variables.c_centros)
	separacion.add(C_conexiones1)
	separacion.add(C_conexiones2)

	######################################################
	#   seccion opciones subframe 1  dispositivos		 #
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
	Perfil_entry = tk.Entry(sub_frame2, bg="lightgray")
	Perfil_entry.place(x=65, y=36, width=150, height=20)
	Perzonalizacion_botones.boton_ayuda(Variables.c_barras, sub_frame2, 
		"Establece un nommbre con el cual se guardara el perfil de la conexion.", 
		7, 36) 

	separacion2 = tk.Frame(C_conexiones1, bg=Variables.c_lina_separacion, width=5)
	separacion2.pack(side="left", fill="y")

	######################################################
	#   seccion opciones subframe 2 hosts				 #
	######################################################

	sub_frame3 = tk.Frame(C_conexiones1, bg=Variables.c_barras, width=0)
	sub_frame3.pack(side="left", fill="both", expand=True)

	dispositivos = tk.Label(sub_frame3, text="Hosts", bg=Variables.c_barras, font=(Variables.poppins_negrita, 12))
	dispositivos.place(x=230, y=10, width=80) 

	return frame
