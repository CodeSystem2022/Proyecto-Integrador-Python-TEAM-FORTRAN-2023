import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.logger_base import log


class Empleado:
    def __init__(self, nombre, apellido, dni, cuit, categoria, sueldo):
        # Constructor de la clase Empleado que recibe los atributos del empleado
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._cuit = cuit
        self._categoria = categoria
        self._sueldo = sueldo

# Método que retorna una representación en forma de cadena del objeto Empleado
    def __str__(self):
        return f'''
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            DNI: {self._dni},
            Cuit: {self._cuit},
            Categoria: {self._categoria},
            Sueldo: {self._sueldo}
        '''

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto.")


    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @staticmethod
    def validar_apellido(apellido):
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser una cadena de texto.")


    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @staticmethod
    def validar_dni(dni):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un número entero.")


    @property
    def cuit(self):
        return self._cuit
    
    @cuit.setter
    def cuit(self, cuit):
        self._cuit = cuit

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

        
    @staticmethod
    def validar_sueldo(sueldo):
        if not isinstance(sueldo, float) and not isinstance(sueldo, int):
            raise ValueError("El sueldo debe ser un número.")

