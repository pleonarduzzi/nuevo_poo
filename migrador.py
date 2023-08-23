import pandas as pd
import time
from logica_negocio import *
from automatizador import *

def migracion(archivo_turnos, archivo_ayp, archivo_evaluados):
    
    turnos_ehcos = pd.read_excel(archivo_turnos)
    agendas_y_profesionales = pd.read_excel(archivo_ayp)

    navegador = Navegador("https://www.santafe.gov.ar/sicap/login.php")

    time.sleep(0.5)

    campo_usuario = navegador.buscar_elemento('/html/body/div[2]/div/div/div/div[3]/form/fieldset/div[1]/input')
    navegador.ingresar_objeto_en_elemento('pleonarduzzi',campo_usuario)

    campo_password = navegador.buscar_elemento('/html/body/div[2]/div/div/div/div[3]/form/fieldset/div[2]/input')
    navegador.ingresar_objeto_en_elemento('fibonacci011',campo_password)
    
    navegador.click_objeto('/html/body/div[2]/div/div/div/div[3]/form/fieldset/button/span')

