from abc import ABC, abstractmethod
from funciones_auxiliares import *

"""
https://www.scaler.com/topics/abstract-class-in-python/ -> interfaces y clases abstractas en Python

"""

class Persona(ABC):
    def __init__(self,apellido,nombre) -> None:
        self.apellido = apellido
        self.nombre = nombre
    
    @abstractmethod
    def __eq__(self,persona):
        pass

class Paciente(Persona):
    def __init__(self,apellido,nombre,dni) -> None:
        super().__init__(apellido,nombre)
        self.dni = dni
    
    def __eq__(self, persona):
        if self.dni.strip() == persona.dni.strip():
            apellido_1 = quitar_vocales_con_acento(self.apellido.lower().strip()).split(' ')
            apellido_1_ordenado = sorted(apellido_1)
            apellido_1_str = ' '.join(apellido_1_ordenado)
            
            apellido_2 = quitar_vocales_con_acento(persona.apellido.lower().strip()).split(' ')
            apellido_2_ordenado = sorted(apellido_2)
            apellido_2_str = ' '.join(apellido_2_ordenado)

            apellido_1_incluido_en_apellido_2 = apellido_1_str in apellido_2_str
            apellido_2_incluido_en_apellido_1 = apellido_2_str in apellido_1_str

            if len(apellido_1_ordenado) == len(apellido_2_ordenado) or apellido_1_incluido_en_apellido_2 or apellido_2_incluido_en_apellido_1:
            
                comparacion_apellidos = similar(apellido_1_str,apellido_2_str)

                if comparacion_apellidos >= 0.8 or apellido_1_incluido_en_apellido_2 or apellido_2_incluido_en_apellido_1:
                    nombre_1 = quitar_vocales_con_acento(self.nombre.lower().strip()).split(' ')
                    nombre_1_ordenado = sorted(nombre_1)
                    nombre_1_str = ' '.join(nombre_1_ordenado)
                    
                    nombre_2 = quitar_vocales_con_acento(persona.nombre.lower().strip()).split(' ')
                    nombre_2_ordenado = sorted(nombre_2)
                    nombre_2_str = ' '.join(nombre_2_ordenado)

                    nombre_1_incluido_en_nombre_2 = nombre_1_str in nombre_2_str
                    nombre_2_incluido_en_nombre_1 = nombre_2_str in nombre_1_str

                    if len(nombre_1_ordenado) == len(nombre_2_ordenado) or nombre_1_incluido_en_nombre_2 or nombre_2_incluido_en_nombre_1:
                                            
                        comparacion_nombres = similar(nombre_1_str,nombre_2_str)

                        if comparacion_nombres >= 0.8 or nombre_1_incluido_en_nombre_2 or nombre_2_incluido_en_nombre_1:
                            return True
        return False    

class Profesional(Persona):
    def __init__(self,apellido,nombre,especialidad) -> None:
        super().__init__(apellido,nombre)
        self.especialidad = especialidad

    def __eq__(self, persona):
        apellido_1 = quitar_vocales_con_acento(self.apellido.lower().strip()).split(' ')
        apellido_1_ordenado = sorted(apellido_1)
        apellido_1_str = ' '.join(apellido_1_ordenado)
        
        apellido_2 = quitar_vocales_con_acento(persona.apellido.lower().strip()).split(' ')
        apellido_2_ordenado = sorted(apellido_2)
        apellido_2_str = ' '.join(apellido_2_ordenado)

        apellido_1_incluido_en_apellido_2 = apellido_1_str in apellido_2_str
        apellido_2_incluido_en_apellido_1 = apellido_2_str in apellido_1_str

        if len(apellido_1_ordenado) == len(apellido_2_ordenado) or apellido_1_incluido_en_apellido_2 or apellido_2_incluido_en_apellido_1:
                
                comparacion_apellidos = similar(apellido_1_str,apellido_2_str)

                if comparacion_apellidos >= 0.8 or apellido_1_incluido_en_apellido_2 or apellido_2_incluido_en_apellido_1:
                    nombre_1 = quitar_vocales_con_acento(self.nombre.lower().strip()).split(' ')
                    nombre_1_ordenado = sorted(nombre_1)
                    nombre_1_str = ' '.join(nombre_1_ordenado)
                    
                    nombre_2 = quitar_vocales_con_acento(persona.nombre.lower().strip()).split(' ')
                    nombre_2_ordenado = sorted(nombre_2)
                    nombre_2_str = ' '.join(nombre_2_ordenado)

                    nombre_1_incluido_en_nombre_2 = nombre_1_str in nombre_2_str
                    nombre_2_incluido_en_nombre_1 = nombre_2_str in nombre_1_str

                    if len(nombre_1_ordenado) == len(nombre_2_ordenado) or nombre_1_incluido_en_nombre_2 or nombre_2_incluido_en_nombre_1:
                                            
                        comparacion_nombres = similar(nombre_1_str,nombre_2_str)

                        if comparacion_nombres >= 0.8 or nombre_1_incluido_en_nombre_2 or nombre_2_incluido_en_nombre_1:
                            especialidad_1 = quitar_vocales_con_acento(self.especialidad.lower().strip())
                            especialidad_2 = quitar_vocales_con_acento(persona.especialidad.lower().strip())

                            especialidad_1_incluida_en_especialidad_2 = especialidad_1 in especialidad_2
                            especialidad_2_incluida_en_especialidad_1 = especialidad_2 in especialidad_1

                            comparacion_especialidades = similar(especialidad_1,especialidad_2)

                            if comparacion_especialidades >= 0.6 or especialidad_1_incluida_en_especialidad_2 or especialidad_2_incluida_en_especialidad_1:
                                return True
                    
        return False


class Cita:
    def __init__(self,fecha,hora,paciente,profesional) -> None:
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.profesional = profesional