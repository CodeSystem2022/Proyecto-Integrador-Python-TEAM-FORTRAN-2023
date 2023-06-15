import psycopg2 as bd
import sys
from logger_base import log

class Conexion:
    _DATABASE = 'teamfortran'  # Nombre de la base de datos
    _USERNAME = 'postgres'  # Nombre de usuario de la base de datos
    _PASSWORD = 'admin'  # Contraseña de la base de datos
    _DB_PORT = '5432'  # Puerto de la base de datos
    _HOST = '127.0.0.1'  # Host de la base de datos
    _conexion = None  # Variable para almacenar la conexión a la base de datos
    _cursor = None  # Variable para almacenar el cursor de la conexión

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                # Establecer la conexión a la base de datos utilizando los parámetros de conexión
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexion Establecida {cls._conexion}')
                return cls._conexion
            except Exception as e :
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion
            
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                 # Obtener el cursor de la conexión a la base de datos
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e: 
                log.error(f'Ocurrio un error {e}')
                sys.exit()
        else:
            return cls._cursor









