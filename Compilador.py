import sys
from cx_Freeze import setup, Executable

base = None

build_exe_options = { #incluir paquetes que usa el programa
	"packages": ["tkinter"],
	"includes": [
	"tkinter", "ctypes", "datetime", "os", "getpass",
	"time", "random", "socket", "psutil", "speedtest",
	"keyboard", "subprocess", "re", "PIL", "pandas", "pyperclip", "pywifi", "openpyxl",
	"shutil", "openpyxl.styles"
	],
	"include_files": [
	("lib/Data", "lib/data") #va a cipiar todo de la ruta lib/Data a lib/data que esta dentro del build del aplicacion
	]
}

executables = [ #con base a el scrip pricipal y el icono creara el ejecutable
    Executable("NetAplicationV2.py", base=base, icon="lib/data/icono.ico")
]

setup(
    name="NetAplication_v2", #nombre de la aplicacion
    version="2.0", #version
    description="Bienvenido a tu herramienta todo en uno para ingeniería de sistemas y redes. Diseñada pensando en los profesionales de las telecomunicaciones, esta herramienta proporciona un conjunto integral de funciones para facilitar la gestión eficiente de tus sistemas y redes.",
    options={"build_exe": build_exe_options},
    executables=executables
)

"""
PARA EJECUTAR Y CREAR EL .EXE DEL PROGRAMA EDITAR EL NOMBRE DEL .PY,
Y CORRER EN CMD ESTE COMANDO, python _compilador.py build
"""
