import os
import sys

# Obtener la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar la ruta base al sys.path
sys.path.append(BASE_DIR)
from logger_base import log
from database.empleado import Empleado
from conexion import Conexion

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definir la clase EmpleadoDao
class EmpleadoDao:
    # Consultas SQL
    _SELECIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre, apellido, dni, cuit, categoria, sueldo) VALUES (%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre=%s, apellido=%s, dni=%s, cuit=%s, categoria=%s, sueldo=%s WHERE id_empleado=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE id_empleado=%s '

    @classmethod
    def seleccionar(cls):
        # Método para seleccionar todos los empleados de la base de datos
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECIONAR)
                registros = cursor.fetchall()
                empleados = []
                for registro in registros:
                     # Crear objetos Empleado a partir de los registros obtenidos
                    empleado = Empleado(
                        registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                    empleados.append(empleado)
                return empleados

    @classmethod
    def insertar(cls, empleado):
        # Método para insertar un empleado en la base de datos
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (empleado.nombre, empleado.apellido, empleado.dni,
                           empleado.cuit, empleado.categoria, empleado.sueldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Empleado Agregado: {empleado}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, empleado):
        # Método para actualizar un empleado en la base de datos
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (empleado.nombre, empleado.apellido, empleado.dni, empleado.cuit,
                           empleado.categoria, empleado.sueldo, empleado.id_empleado)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Empleado actualizado {empleado}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, empleado):
        # Método para eliminar un empleado de la base de datos
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (empleado.id_empleado)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Empleado eliminado {empleado}')
                return cursor.rowcount

