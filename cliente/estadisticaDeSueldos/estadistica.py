import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database')))

from model import logger_base as log
from model import conexion as Conexion
from model import empleado_dao as EmpleadoDao
from database import empleado as Empleado


if __name__ == '__main__':

    empleados = EmpleadoDao.seleccionar()

# Extraer los sueldos de cada empleado
    sueldos = [empleado.sueldo for empleado in empleados]

# Ordenar los sueldos en forma ascendente
    sueldos_ordenados = sorted(sueldos)

    print(sueldos_ordenados)

#METODO PARA CALCULAR LA MODA 

def calcular_moda(sueldos):
    # Calcular la frecuencia de cada sueldo utilizando un diccionario
    frecuencias = {}
    for sueldo in sueldos:
        if sueldo in frecuencias:
            frecuencias[sueldo] += 1
        else:
            frecuencias[sueldo] = 1

    # Encontrar la moda(s) como el(s) valor(es) con mayor frecuencia
    moda = []
    max_frecuencia = max(frecuencias.values())
    for sueldo, frecuencia in frecuencias.items():
        if frecuencia == max_frecuencia:
            moda.append(sueldo)

    return moda
    
    