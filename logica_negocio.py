from abc import ABC, abstractclassmethod

"""
https://www.scaler.com/topics/abstract-class-in-python/ -> interfaces y clases abstractas en Python

"""

class Persona(ABC):
    def __init__(self,apellido,nombre) -> None:
        self.apellido = apellido
        self.nombre = nombre
    
    @abstractclassmethod
    def __eq__(self,persona):
        pass

class Paciente(Persona):
    def __init__(self,apellido,nombre,dni) -> None:
        super().__init__(apellido,nombre)
        self.dni = dni

class Profesional(Persona):
    def __init__(self,apellido,nombre,especialidad) -> None:
        super().__init__(apellido,nombre)
        self.especialidad = especialidad

class Turno:
    def __init__(self,fecha,hora,paciente,profesional) -> None:
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.profesional = profesional