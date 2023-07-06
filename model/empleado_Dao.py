import os
import statistics
import sys
from logger_base import log
from database.empleado import Empleado
from conexion import Conexion
from cursor_del_pool import CursorDelPool

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar la ruta base al sys.path
sys.path.append(BASE_DIR)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definir la clase EmpleadoDao
class EmpleadoDao:
    # Consultas SQL
    _SELECCIONAR = 'SELECT * FROM empleado ORDER BY dni'
    _INSERTAR = 'INSERT INTO empleado(nombre, apellido, dni, cuit, categoria, sueldo) VALUES (%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre=%s, apellido=%s, dni=%s, cuit=%s, categoria=%s, sueldo=%s WHERE dni=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE dni=%s '
    _MOSTRAR = 'SELECT * FROM empleado ORDER BY apellido'

    @classmethod
    def seleccionar(cls):
        # Método para seleccionar todos los empleados de la base de datos
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            empleados = []
            for registro in registros:
                     # Crear objetos Empleado a partir de los registros obtenidos
                empleado = Empleado(
                    registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                empleados.append(empleado)
            return empleados

    @classmethod
    def insertar(cls, empleado):
        # Método para insertar un empleado en la base de datos
        Empleado.validar_dni(empleado.dni)
        Empleado.validar_nombre(empleado.nombre)
        Empleado.validar_apellido(empleado.apellido)
        Empleado.validar_sueldo(empleado.sueldo)
        with CursorDelPool() as cursor:
            valores = (empleado.nombre, empleado.apellido, empleado.dni,
                        empleado.cuit, empleado.categoria, empleado.sueldo)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Empleado Agregado: {empleado}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, empleado):
        # Método para actualizar un empleado en la base de datos
        Empleado.validar_dni(empleado.dni)
        Empleado.validar_nombre(empleado.nombre)
        Empleado.validar_apellido(empleado.apellido)
        Empleado.validar_sueldo(empleado.sueldo)
        with CursorDelPool() as cursor:
            valores = (empleado.nombre, empleado.apellido, empleado.dni, empleado.cuit,
                        empleado.categoria, empleado.sueldo)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Empleado actualizado {empleado}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, empleado):
        # Método para eliminar un empleado de la base de datos
        with CursorDelPool() as cursor:
            valores = (empleado.dni)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Empleado eliminado {empleado}')
            return cursor.rowcount


    @classmethod
    def mostrar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._MOSTRAR)
            registro = cursor.fetchall()
            for index, registro in enumerate(registro):
                empleado = Empleado(
                    registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]
                )
                print(f"Empleado {index+1}: {empleado}")


    @classmethod
    def buscar_por_dni(cls, dni):
        # Método para buscar un empleado por su DNI en la base de datos
        with CursorDelPool() as cursor:
            consulta = 'SELECT * FROM empleado WHERE dni = %s'
            cursor.execute(consulta, (dni,))
            registro = cursor.fetchone()
            if registro:
                empleado = Empleado(
                    registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]
                )
                return empleado
            else:
                return None
    
    @classmethod
    def obtener_sueldos(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            sueldos = [registro[5] for registro in registros]
            return sueldos

    @classmethod
    def calcular_moda(cls):
        sueldos = cls.obtener_sueldos()
        if sueldos:
            return statistics.mode(sueldos)
        else:
            return None

    @classmethod
    def calcular_mediana(cls):
        sueldos = cls.obtener_sueldos()
        if sueldos:
            return statistics.median(sueldos)
        else:
            return None

    @classmethod
    def calcular_media(cls):
        sueldos = cls.obtener_sueldos()
        if sueldos:
            return statistics.mean(sueldos)
        else:
            return None


def crear_tabla():
    query = '''
    CREATE TABLE IF NOT EXISTS empleado (
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        dni VARCHAR(8) NOT NULL,
        cuit VARCHAR(11) NOT NULL,
        categoria VARCHAR(100) NOT NULL,
        sueldo DECIMAL(10, 2) NOT NULL
    )
    '''

    with Conexion.obtenerConexion() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute(query)
            log.debug('Tabla empleado creada')
