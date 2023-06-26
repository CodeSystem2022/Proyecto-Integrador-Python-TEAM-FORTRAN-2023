import psycopg2

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