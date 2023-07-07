import os
import sys
from model.logger_base import log
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta el metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepcion : {valor_excepcion}')
        else:
            self._conexion.commit()
            log.debug('commit de la TRANSACCION')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion) 


