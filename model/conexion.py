from psycopg2 import pool
import sys
from logger_base import log

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
        conexion = cls.obtenerConexion()
        cursor = conexion.cursor()
        log.debug(f"Cursor obtenido: {cursor}")
        return cursor

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
                log.error(f"Error pool: {e}")
                sys.exit()
        else:
            return cls._pool
        
def crear_tabla():
    try:
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()

        # Sentencia SQL para crear la tabla "Empleado"
        crear_tabla_sql = '''
        CREATE TABLE IF NOT EXISTS Empleado (
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            dni VARCHAR(11) NOT NULL,
            cuit VARCHAR(13) NOT NULL,
            categoria VARCHAR(100) NOT NULL,
            sueldo DECIMAL(10, 2) NOT NULL
        );
        '''

        cursor.execute(crear_tabla_sql)
        conexion.commit()

        log.debug("Tabla 'Empleado' creada exitosamente.")

    except (Exception, pool.Error) as error:
        log.error(f"Error al crear la tabla 'Empleado': {error}")

    finally:
        if conexion:
            cursor.close()
            conexion.close()
            log.debug("Conexión cerrada.")

if __name__ == '__main__':
    # Prueba de conexión
    try:
        conexion = Conexion.obtenerConexion()
        if conexion:
            print("Conexión exitosa!")
            conexion.close()
            crear_tabla()
        else:
            print("No se pudo obtener la conexión.")
    except Exception as e:
        print(f"Error al intentar conectar: {e}")
