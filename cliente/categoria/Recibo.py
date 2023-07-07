import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

from model.logger_base import log
from model.conexion import Conexion
from model.empleado_Dao import EmpleadoDao


class ReciboSueldo(QWidget):
    def __init__(self, dni=None, nombre=None, apellido=None, cuit=None, categoria=None, sueldo=None):
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

        self.setStyleSheet("background-color: white")
        self.btn_obtener_recibo.setStyleSheet(
            "background-color: darkblue; color: white;")

        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit
        self.categoria = categoria
        self.sueldo = sueldo

    def obtener_recibo(self):
        log.debug("Iniciando generación del recibo de sueldo")
        if self.sueldo is None:
            log.error("El sueldo no está definido")
            return  # Salir del método o mostrar un mensaje de error al usuario

        try:
            datos_empresa = """

               DATOS DE LA EMPRESA
             |---------------------------------------------------|---------------------------------------------------|
               NOMBRE DE LA EMPRESA: Team Fortran               Cuit: 9-52634875-0
             |---------------------------------------------------|---------------------------------------------------|
               DIRECCION: Gotan 985
             |---------------------------------------------------|---------------------------------------------------|

            """

            datos_empleado = f"""
              DATOS DE LOS EMPLEADOS
            |----------------------------------------------------|---------------------------------------------------|
              APELLIDO: {self.apellido}                                  NOMBRE :  {self.nombre}
            |----------------------------------------------------|---------------------------------------------------|
              DNI: {self.dni}                                            CUIL: {self.cuit}
            |----------------------------------------------------|---------------------------------------------------|
              CATEGORIA: {self.categoria}                                SUELDO BASICO: ${self.sueldo}
            |----------------------------------------------------|---------------------------------------------------|
            """

            sueldo_bruto = float(self.sueldo)
            log.debug(f"Sueldo bruto: {sueldo_bruto}")

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
            SUELDO BASICO                            ${self.sueldo}                                                                                
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

            self.btn_obtener_recibo.hide()
            self.label_datos_empresa.show()
            self.label_datos_empleado.show()
            self.label_conceptos.show()


            self.setStyleSheet("background-color: lightblue;")

            self.label_datos_empresa.setText(datos_empresa)
            self.label_datos_empleado.setText(datos_empleado)
            self.label_conceptos.setText(conceptos)
            log.debug("Recibo de sueldo generado exitosamente")
        except Exception as e:
            log.error("Se produjo un error al generar el recibo de sueldo:", str(e))



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Verificar si se proporcionaron argumentos y establecer los valores predeterminados en caso contrario
    if len(sys.argv) >= 7:
        log.debug("Argumentos proporcionados. Creando instancia de ReciboSueldo con argumentos")
        recibo = ReciboSueldo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        log.debug("No se proporcionaron argumentos. Creando instancia de ReciboSueldo sin argumentos")
        recibo = ReciboSueldo()  # Usar valores predeterminados

    recibo.show()
    sys.exit(app.exec())
