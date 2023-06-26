from psycopg2 import pool
import sys
from logger_base import log

class Conexion:
    _DATABASE = 'teamfortran'  # Nombre de la base de datos
    _USERNAME = 'postgres'  # Nombre de usuario de la base de datos
    _PASSWORD = 'admin'  # Contraseña de la base de datos
    _DB_PORT = '5432'  # Puerto de la base de datos
    _HOST = '127.0.0.1'  # Host de la base de datos
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenida del pool {conexion}")
        return conexion
            
    @classmethod
    def obtenerCursor(cls):
        conexion = cls.obtenerConexion()
        cursor = conexion.cursor()
        log.debug(f"Cursor obtenido: {cursor}")
        return cursor

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
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









