import psycopg2
from PyQt5.QtWidgets import QTableWidgetItem

datosBD = {
    "dbname" : "",
    "user": "",
    "password" : "",
    "host" : "",
    "port" : ""
}

def insertarEmpleado(empleado):
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''INSERT INTO empleados (nombre, apellido, dni, cuit, categoria, sueldo) VALUES (%s, %s, %s, %s, %s, %s)'''
        try:
            datos = (empleado.nombre, empleado.apellido, empleado.dni,
                       empleado.cuit, empleado.categoria, empleado.sueldo)
            cursor.execute(query, (datos))
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()
        
def cantidadEmpleados():
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''SELECT COUNT(*) FROM empleados'''
        try:
            cursor.execute(query)
            respuesta = cursor.fetchone()
            return respuesta[0]
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()
        
def actualizarEmpleado(empleado):
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''UPDATE empleados SET nombre=%s, apellido=%s, dni=%s, cuit=%s, categoria=%s, sueldo=%s WHERE dni=%s'''
        try:
            datos = (empleado.nombre, empleado.apellido, empleado.dni,
                       empleado.cuit, empleado.categoria, empleado.sueldo, empleado.dni)
            cursor.execute(query, (datos))
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()
    
def eliminarEmpleado(empleado):
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''DELETE FROM empleados WHERE dni=%s'''
        try:
            # datos = empleado.dni
            cursor.execute(query, (empleado.dni,))
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()
        
def mostrarEmpleados(self):
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''SELECT * FROM empleados ORDER BY apellido'''
        try:
            cursor.execute(query)
            registros = cursor.fetchall()
            
            tabla = self.ventana.tabla_productos
            tabla.setRowCount(cantidadEmpleados())
            tabla.setColumnCount(6)
            
            for index,registro in enumerate(registros):
                    tabla.setItem(index, 0, QTableWidgetItem(registro[0])) 
                    tabla.setItem(index, 1, QTableWidgetItem(registro[1]))  
                    tabla.setItem(index, 2, QTableWidgetItem(str(registro[2])))  
                    tabla.setItem(index, 3, QTableWidgetItem(str(registro[3])))  
                    tabla.setItem(index, 4, QTableWidgetItem(registro[4]))  
                    tabla.setItem(index, 5, QTableWidgetItem(str(registro[5])))
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()
        
def buscarEmpleado(dni):
        conn = psycopg2.connect(**datosBD)
        cursor = conn.cursor()
        query = '''SELECT * FROM empleados WHERE dni=%s'''
        try:
            cursor.execute(query, (dni,))
            encontrados = cursor.fetchall()
            if(bool(encontrados)):
                for empleadoEncontrado in encontrados:
                    return(empleadoEncontrado)
            else:
                return ('null', 'null', 'null', 'null', 'null', 'null')
        except Exception as e:
            print(e)
        conn.commit()
        cursor.close()