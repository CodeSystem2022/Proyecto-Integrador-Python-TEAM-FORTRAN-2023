from psycopg2 import pool
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

from model.logger_base import log

class Conexion:
    _DATABASE = 'root'  # Nombre de la base de datos
    _USERNAME = 'root'  # Nombre de usuario de la base de datos
    _PASSWORD = 'root'  # Contraseña de la base de datos
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
        pass

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      database=cls._DATABASE,
                                                      port=cls._DB_PORT)
                log.debug(f"Creacion del pool: {cls._pool}")
                return cls._pool
            except Exception as e: 
                log.error(f'Ocurrio un error {e}')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()

