from conexion import Conexion
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.empleado import Empleado
from logger_base import log


class EmpleadoDao:
    _SELECIONAR = 'SELECT * FROM empleado ORDER BY id_empleado'
    _INSERTAR = 'INSERT INTO empleado(nombre, apellido, dni, cuit, categoria, sueldo) VALUES (%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE empleado SET nombre=%s, apellido=%s, dni=%s, cuit=%s, categoria=%s, sueldo=%s WHERE id_empleado=%s'
    _ELIMINAR = 'DELETE FROM empleado WHERE id_empleado=%s '

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECIONAR)
                registros = cursor.fetchall()
                empleados = []
                for registro in registros:
                    empleado = Empleado(registro[0], registro[1], registro[2], registro[3],registro[4], registro[5], registro[6])
                    empleados.append(empleado)
                return empleados

    @classmethod
    def insertar(cls, empleado):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (empleado.nombre, empleado.apellido, empleado.dni, empleado.cuit, empleado.categoria, empleado.sueldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Empleado Agregado: {empleado}')
                return cursor.rowcount
            
if __name__ == '__main__':
    empleado1 = Empleado('1','lucas', 'vizcaino', '32','322','contratado',15000)
    insertar_empleado = EmpleadoDao.insertar(empleado1)

    empleados = EmpleadoDao.seleccionar()
    for empleado in empleados:
        log.debug(empleado)