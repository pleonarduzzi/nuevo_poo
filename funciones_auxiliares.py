from difflib import SequenceMatcher
import pandas as pd

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def quitar_vocales_con_acento(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a+') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log("log_migracion.txt")
def guardar_en_evaluados(evaluados,datos,profesional_sicap,razon):
    res = pd.DataFrame(columns=['DNI','Paciente','Fecha de cita','Hora','Agenda','Especialidad','Profesional SICAP','Razon'])
    res.loc[len(res.index)] = [datos['DNI'],datos['Paciente'],datos['Fecha de cita'],datos['Hora'],datos['Agenda'], datos['Especialidad'],profesional_sicap,razon]

    ev=pd.read_excel(evaluados)
    with pd.ExcelWriter(evaluados,mode='a',engine='openpyxl',if_sheet_exists='overlay') as writer:
        res.to_excel(writer, sheet_name="Hoja1", startrow=len(ev.index)+1, header=False, index=False)
    
    return razon