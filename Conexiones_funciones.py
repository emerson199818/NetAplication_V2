import tkinter as tk

import Variables

def Centro_conexiones(frame): 
	# Crear el contenedor principal 
	C_conexiones_p = tk.Frame(frame, bg=Variables.c_centros)
	C_conexiones_p.pack(side="top", fill="both", expand=True)

	# Línea de separación entre subframes C_wireless1 y C_wireless2
	separacion = tk.PanedWindow(C_conexiones_p, bg=Variables.c_lina_separacion, orient="vertical", sashwidth=30, sashrelief="sunken")
	separacion.pack(side="top", fill="both", expand=True)
	
	# Agregar dos frames al PanedWindow
	C_conexiones1 = tk.Frame(separacion, bg=Variables.c_barras)
	C_conexiones2 = tk.Frame(separacion, bg=Variables.c_centros)
	separacion.add(C_conexiones1)
	separacion.add(C_conexiones2)

	######################################################
	#   seccion opciones subframe 1       				 #
	######################################################
	sub_frame1 = tk.Frame(C_conexiones1, bg=Variables.c_centros, width=210, height=340)
	sub_frame1.pack(side="left", fill="both", expand=False)

	dispositivos = tk.Label(sub_frame1, text="Dispositivos", bg=Variables.c_centros, font=("Arial", 12, "bold"))
	dispositivos.place(x=50, y=10, width=100) 

	texto_con_punto = "• Windows\n• Unix\n• Cisco\n    - Switches\n    - Routers\n• Huawei\n    - Switches\n    - Routers"
	label_with_bullet = tk.Label(sub_frame1, text=texto_con_punto, justify=tk.LEFT, bg=Variables.c_centros, font=("Arial", 10))
	label_with_bullet.place(x=25, y=35, width=100)

	dispositivos = tk.Label(sub_frame1, text="Conexiones", bg=Variables.c_centros, font=("Arial", 12, "bold"))
	dispositivos.place(x=50, y=180, width=100) 

	texto_con_punto = "• Ssh\n• Telnet\n• PowerShell\n• WinRS/WinRM"
	label_with_bullet = tk.Label(sub_frame1, text=texto_con_punto, justify=tk.LEFT, bg=Variables.c_centros, font=("Arial", 10))
	label_with_bullet.place(x=35, y=210, width=100)

	separacion1 = tk.Frame(C_conexiones1, bg=Variables.c_lina_separacion, width=5)
	separacion1.pack(side="left", fill="y")

	sub_frame2 = tk.Frame(C_conexiones1, bg=Variables.c_barras, width=600)
	sub_frame2.pack(side="left", fill="both", expand=False)

	dispositivos = tk.Label(sub_frame2, text="Establecer Conexion", bg=Variables.c_barras, font=("Arial", 12, "bold"))
	dispositivos.place(x=230, y=10, width=200) 

	separacion2 = tk.Frame(C_conexiones1, bg=Variables.c_lina_separacion, width=5)
	separacion2.pack(side="left", fill="y")

	sub_frame3 = tk.Frame(C_conexiones1, bg=Variables.c_barras, width=0)
	sub_frame3.pack(side="left", fill="both", expand=True)

	dispositivos = tk.Label(sub_frame3, text="Hosts", bg=Variables.c_barras, font=("Arial", 12, "bold"))
	dispositivos.place(x=230, y=10, width=80) 

	return frame
