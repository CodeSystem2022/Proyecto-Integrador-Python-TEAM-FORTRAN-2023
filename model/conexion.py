from psycopg2 import pool
import sys
import os
from urllib.parse import urlparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..',)))

from model.logger_base import log

class Conexion:
    _DATABASE = 'rootdatabase'
    _USERNAME = 'root'
    _PASSWORD = 'pFoxWiP0l6uGqYfT0VuMxMSSY8wa7Xg2'
    _DB_PORT = '5432'
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
                external_db_url = 'postgres://root:pFoxWiP0l6uGqYfT0VuMxMSSY8wa7Xg2@dpg-cij0vt95rnut2s9uuqfg-a.oregon-postgres.render.com/rootdatabase'

                url_parts = urlparse(external_db_url)

                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      host=url_parts.hostname,
                                                      port=url_parts.port,
                                                      user=url_parts.username,
                                                      password=url_parts.password,
                                                      database=url_parts.path.lstrip('/'),
                                                      maxconn=5)
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

