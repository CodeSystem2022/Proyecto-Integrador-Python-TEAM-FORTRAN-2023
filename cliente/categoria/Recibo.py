import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from model.logger_base import log
from model.conexion import Conexion
from model.empleado_Dao import EmpleadoDao

class ReciboSueldo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recibo de Sueldo")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label_datos_empresa = QLabel()
        self.label_datos_empresa.setStyleSheet("color: darkblue;")
        self.label_datos_empleado = QLabel()
        self.label_datos_empleado.setStyleSheet("color: darkblue;")
        self.label_conceptos = QLabel()
        self.label_conceptos.setStyleSheet("color: darkblue;")
        self.label_remunerativo = QLabel()
        self.label_deducciones = QLabel()
        self.label_no_remunerativo = QLabel()
        self.label_total_remu = QLabel()
        self.label_total_deduc = QLabel()
        self.label_total_neto = QLabel()

        # Mostrar el mensaje al usuario
        # self.label_mensaje = QLabel("Ingrese el número de DNI del empleado:")
        # self.layout.addWidget(self.label_mensaje)

        # Ingreso del número de DNI
        # self.input_dni = QLineEdit()
        # self.layout.addWidget(self.input_dni)

        # Botón para obtener el recibo de sueldo
        self.btn_obtener_recibo = QPushButton("Obtener Recibo")
        self.btn_obtener_recibo.clicked.connect(self.obtener_recibo)
        self.layout.addWidget(self.btn_obtener_recibo)

        self.layout.addWidget(self.label_datos_empresa)
        self.layout.addWidget(self.label_datos_empleado)
        self.layout.addWidget(self.label_conceptos)
        self.layout.addWidget(self.label_remunerativo)
        self.layout.addWidget(self.label_deducciones)
        self.layout.addWidget(self.label_no_remunerativo)
        self.layout.addWidget(self.label_total_remu)
        self.layout.addWidget(self.label_total_deduc)
        self.layout.addWidget(self.label_total_neto)

        self.setStyleSheet("background-color: white")  # color fondo
        self.btn_obtener_recibo.setStyleSheet(
            "background-color: darkblue; color: white;")  # color boton, color fondo y texto

    def obtener_recibo(self):
            # Conexión a la base de datos
            conn = Conexion.obtenerConexion()
            cursor = conn.cursor()

            # Obtener el número de DNI ingresado por el usuario
            numero_dni = self.input_dni.text()

            # Consulta para obtener los datos del empleado
            cursor.execute("SELECT * FROM Personal WHERE dni = %s", (numero_dni,))
            empleado = cursor.fetchone()

            # Cerrar conexión
            cursor.close()
            Conexion.liberarConexion(conn)

            if empleado:
                nombre, apellido, dni, cuit, categoria, sueldo = empleado

                datos_empresa = f"""
                   DATOS DE LA EMPRESA
                 |---------------------------------------------------|---------------------------------------------------|
                   NOMBRE DE LA EMPRESA: Team Fortran               Cuit: 9-52634875-0
                 |---------------------------------------------------|---------------------------------------------------|
                   DIRECCION: Gotan 985
                 |---------------------------------------------------|---------------------------------------------------|
                  """

                # Datos del empleado
                datos_empleado = f"""
                  DATOS DE LOS EMPLEADOS
                |----------------------------------------------------|---------------------------------------------------|
                  APELLIDO: {apellido}                                  NOMBRE :  {nombre}
                |----------------------------------------------------|---------------------------------------------------|
                  DNI: {dni}                                            CUIL: {cuit}
                |----------------------------------------------------|---------------------------------------------------|
                  CATEGORIA: {categoria}                                SUELDO BASICO: ${sueldo}
                |----------------------------------------------------|---------------------------------------------------|
                """

                # Conceptos y montos
                sueldo_bruto = float(sueldo)
                antiguedad = sueldo_bruto * 5 / 100
                presentismo = sueldo_bruto * 20 / 100
                jubilacion = sueldo_bruto * 11 / 100
                obra_social = sueldo_bruto * 3 / 100
                ley19032 = sueldo_bruto * 3 / 100
                sub_total = sueldo_bruto + antiguedad + presentismo
                total_deducciones = jubilacion + obra_social + ley19032
                neto_a_cobrar = sub_total - total_deducciones

                conceptos = f"""
                  CONCEPTOS                            REMUNERATIVO                                         DEDUCCIONES                   
                |--------------------------------|------------------------------------------------|----------------------------------------------|
                  SUELDO BASICO                            ${sueldo}                                                                                
                |--------------------------------|------------------------------------------------|                                                                
                  ANTIGUEDAD                                ${antiguedad}                                                                            
                |--------------------------------|------------------------------------------------|                                                                  
                  PRESENTISMO                               ${presentismo}                                                                           
                |--------------------------------|------------------------------------------------|----------------------------------------------|                                
                  JUBILACION                                                                                           ${jubilacion} 
                |--------------------------------|------------------------------------------------|----------------------------------------------|                                               
                  OBRA SOCIAL                                                                                        ${obra_social}                               
                |--------------------------------|------------------------------------------------|----------------------------------------------|                        
                  LEY 19032                                                                                             ${ley19032} 
                |--------------------------------|------------------------------------------------|----------------------------------------------|
                                                          TOTAL REMUNERATIVO: {sub_total}            TOTAL DEDUCCIONES: {total_deducciones} 
                |--------------------------------|------------------------------------------------------------------------------------------------|
                                                          TOTAL NETO A COBRAR: {neto_a_cobrar}    
                |--------------------------------|------------------------------------------------------------------------------------------------|                                        
                """

                # Oculta las etiquetas
                #self.label_mensaje.hide()
                #self.input_dni.hide()
                self.btn_obtener_recibo.hide()
                self.label_datos_empresa.show()
                self.label_datos_empleado.show()
                self.label_conceptos.show()

                # Cambia estilo a fondo azul claro para mostrar el recibo
                self.setStyleSheet("background-color: lightblue;")

                # Actualiza las etiquetas con los datos obtenidos
                self.label_datos_empresa.setText(datos_empresa)
                self.label_datos_empleado.setText(datos_empleado)
                self.label_conceptos.setText(conceptos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recibo = ReciboSueldo()
    recibo.show()
    sys.exit(app.exec_())
