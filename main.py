from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open
from migrador import migracion
import sys
import os

archivo_turnos_seleccionado = False
archivo_turnos = None
archivo_ayp_seleccionado = False
archivo_ayp = None
driver_chrome_seleccionado = False
driver_chrome = None

def abrirDriverChrome():
    global driver_chrome_seleccionado
    global driver_chrome

    ruta_driver_chrome = FileDialog.askopenfilename(title="Seleccione driver de Google Chrome",filetypes=(("Archivo ejecutable", "*.exe"),))
    driver_chrome = repr(ruta_driver_chrome) #Convierte string a raw string
    nombre_driver_chrome = ruta_driver_chrome.split('/')[-1]
    #label_driver.configure(anchor="w",text="Archivo seleccionado: "+nombre_driver_chrome, font=("Arial",8))
    driver_chrome_seleccionado = True

def abrirArchivoTurnos():
    global archivo_turnos_seleccionado
    global archivo_turnos

    ruta_archivo_turnos = FileDialog.askopenfilename(title="Seleccione archivo de turnos",filetypes=(("Hojas de cálculo", "*.xlsx"),))
    archivo_turnos = ruta_archivo_turnos
    nombre_archivo = ruta_archivo_turnos.split('/')[-1]
    label_turnos.configure(anchor="w",text="Archivo seleccionado: "+nombre_archivo, font=("Arial",8))
    archivo_turnos_seleccionado = True

def abrirArchivosAyP():
    global archivo_ayp_seleccionado
    global archivo_ayp

    ruta_archivo_ayp = FileDialog.askopenfilename(title="Seleccione archivo de agendas y profesionales",filetypes=(("Hojas de cálculo", "*.xlsx"),))
    archivo_ayp = ruta_archivo_ayp
    nombre_archivo = ruta_archivo_ayp.split('/')[-1]
    label_ayp.configure(anchor="w",text="Archivo seleccionado: "+nombre_archivo, font=("Arial",8))
    archivo_ayp_seleccionado = True

def abrirTurnosEvaluados():
    global archivo_evaluados_seleccionado
    global archivo_evaluados

    ruta_archivo_evaluados = FileDialog.askopenfilename(title="Seleccione archivo de turnos evaluados",filetypes=(("Hojas de cálculo", "*.xlsx"),))
    archivo_evaluados = ruta_archivo_evaluados
    nombre_archivo = ruta_archivo_evaluados.split('/')[-1]
    label_evaluados.configure(anchor="w",text="Archivo seleccionado: "+nombre_archivo, font=("Arial",8))
    archivo_evaluados_seleccionado = True

def comenzar():
    if not archivo_turnos_seleccionado or not archivo_ayp_seleccionado or not archivo_evaluados_seleccionado:
        MessageBox.showerror("Error", "Debe seleccionar el driver de Google Chrome, un archivo de turnos, un archivo de agendas y profesionales y un archivo de turnos evaluados.")
    else:
        #boton_iniciar.config(state="disabled")
        #hilo = threading.Thread(target=migracion.migracion, args=(archivo_turnos,archivo_ayp))
        #hilo.start()
        migracion(archivo_turnos=archivo_turnos, archivo_ayp=archivo_ayp, archivo_evaluados=archivo_evaluados)

def salir():
    root.destroy()

root = Tk()
root.title("CEMAFE")
#im = Image.open(resource_path('Logo-SANTAFE-circulo.png'))
#photo = ImageTk.PhotoImage(im)
#root.wm_iconphoto(True, photo)
#root.iconbitmap(resource_path("Logo-SANTAFE-circulo.ico"))
#imprimir_por_pantalla_y_escribir_en_log(resource_path("Logo-SANTAFE-circulo.ico"))
root.config(width=300,height=210)
#root.config(background="white")
root.resizable(0, 0)

#Titulo
frame_titulo = Frame(root,width=450,height=100)
frame_titulo.grid(column=1, row=1)
label_titulo = Label(frame_titulo, text="Migrador de turnos de ehCOS a SICAP")
label_titulo.pack()
label_titulo.config(font=("Arial",10, UNDERLINE),padx=10,pady=10)
#label_titulo2 = Label(frame_titulo, text="TESTING")
#label_titulo2.pack()
#label_titulo2.config(font=("Arial",10, UNDERLINE),padx=10,pady=10)

#Apertura de archivos
frame_archivos = Frame(root,width=300,height=70)
frame_archivos.grid(column=1, row=2)
#frame_archivos.config(background="yellow")
#boton_driver = Button(frame_archivos, text="Seleccione driver de Chrome", command=abrirDriverChrome)
#boton_driver.grid(column=1, row=1, sticky="w")
#label_driver = Label(frame_archivos, text="Archivo seleccionado: ", width = 50, height = 2, fg = "red", anchor="w", font=("Arial",8))
#label_driver.grid(column=1, row=2, sticky="w")

boton_turnos = Button(frame_archivos, text="Seleccione archivo de turnos", command=abrirArchivoTurnos)
boton_turnos.grid(column=1, row=3, sticky="w")
label_turnos = Label(frame_archivos, text="Archivo seleccionado: ", width = 50, height = 2, fg = "red", anchor="w", font=("Arial",8))
label_turnos.grid(column=1, row=4, sticky="w")

boton_ayp = Button(frame_archivos, text="Seleccione archivo de agendas y profesionales", command=abrirArchivosAyP)
boton_ayp.grid(column=1, row=5, sticky="w")
label_ayp = Label(frame_archivos, text="Archivo seleccionado: ", width = 50, height = 2, fg = "red", anchor="w", font=("Arial",8))
label_ayp.grid(column=1, row=6, sticky="w")

boton_evaluados = Button(frame_archivos, text="Seleccione archivo donde se guardaran los turnos ya evaluados", command=abrirTurnosEvaluados)
boton_evaluados.grid(column=1, row=7, sticky="w")
label_evaluados = Label(frame_archivos, text="Archivo seleccionado: ", width = 50, height = 2, fg = "red", anchor="w", font=("Arial",8))
label_evaluados.grid(column=1, row=8, sticky="w")

frame_botones = Frame(root,width=300,height=70)
frame_botones.grid(column=1, row=3)
#frame_botones.config(background="white")
boton_iniciar = Button(frame_botones, text="Comenzar",command=comenzar)
boton_iniciar.grid(column=1, row=1, pady=5)
boton_salir = Button(frame_botones, text="Salir", command=salir)
boton_salir.grid(column=1, row=2, pady=5)

label_info = Label(frame_botones, text="v1.1 - Hecho por Pablo Leonarduzzi y Sebastián Tanoni", font=("Arial",6))
label_info.grid(column=1, row=3, sticky="w")

root.mainloop()