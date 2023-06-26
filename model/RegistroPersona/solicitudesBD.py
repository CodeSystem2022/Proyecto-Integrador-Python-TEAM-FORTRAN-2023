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