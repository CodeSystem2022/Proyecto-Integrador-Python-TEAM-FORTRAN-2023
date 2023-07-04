import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from solicitudesBD import mostrarEmpleados, insertarEmpleado, buscarEmpleado, actualizarEmpleado, eliminarEmpleado
from database.empleado import Empleado
from diseñoRegistroPersonaPy import Ui_MainWindow
import menuOpciones


class Iniciar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Iniciar, self).__init__()
        try:
            self.setupUi(self)  # Reemplaza loadUi por setupUi
        except Exception as e:
            print("Error al cargar el archivo UI:", str(e))
        # Agregar la variable "ventana" como un atributo de la instancia actual
        self.ventana = self


        self.ventana.bt_datos.clicked.connect(self.seccionMostrarBaseDatos)
        self.ventana.bt_registrar.clicked.connect(self.seccionRegistrar)
        self.ventana.bt_actualizar.clicked.connect(self.seccionActualizar)
        self.ventana.bt_eliminar_2.clicked.connect(self.seccionEliminar)
        self.ventana.pushButton.clicked.connect(self.seccionMenu)

        self.ventana.bt_agregar.clicked.connect(self.agregarEmpleado)
        self.ventana.bt_refrescar.clicked.connect(self.seccionMostrarBaseDatos)
        self.ventana.bt_actualizar_tabla.clicked.connect(self.actualizarEmpleado)
        self.ventana.bt_actualizar_buscar.clicked.connect(self.buscarActualizarEmpleado)
        self.ventana.bt_buscar_borrar.clicked.connect(self.buscarEliminarEmpleado)
        self.ventana.bt_eliminar.clicked.connect(self.botonEliminarEmpleado)

        mostrarEmpleados(self)

        self.show()


    def seccionMostrarBaseDatos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)
        mostrarEmpleados(self)

    def seccionRegistrar(self):
        self.ventana.stackedWidget.setCurrentIndex(1)

    def seccionActualizar(self):
        self.ventana.stackedWidget.setCurrentIndex(2)

    def seccionEliminar(self):
        self.ventana.stackedWidget.setCurrentIndex(3)

    def seccionMenu(self):
        self.close()
        self.menu_principal = menuOpciones.Ui_iniciar()
        self.menu_principal.show()

    def agregarEmpleado(self):
        nombre = self.ventana.reg_nombre.text()
        apellido = self.ventana.reg_apellido.text()
        dni = self.ventana.reg_dni.text()
        cuit = self.ventana.reg_cuit.text()
        categoria = self.ventana.reg_categoria.text()
        sueldo = self.ventana.reg_sueldo.text()

        datosEmpleado = Empleado(1, nombre, apellido, dni, cuit, categoria, sueldo)
        insertarEmpleado(datosEmpleado)

        self.ventana.reg_nombre.setText('')
        self.ventana.reg_apellido.setText('')
        self.ventana.reg_dni.setText('')
        self.ventana.reg_cuit.setText('')
        self.ventana.reg_categoria.setText('')
        self.ventana.reg_sueldo.setText('')

    def actualizarEmpleado(self):
        nombre = self.ventana.act_nombre.text()
        apellido = self.ventana.act_apellido.text()
        dni = self.ventana.act_dni.text()
        cuit = self.ventana.act_cuit.text()
        categoria = self.ventana.act_categoria.text()
        sueldo = self.ventana.act_sueldo.text()

        datosEmpleado = Empleado(1, nombre, apellido, dni, cuit, categoria, sueldo)
        actualizarEmpleado(datosEmpleado)

        self.ventana.act_nombre.setText('')
        self.ventana.act_apellido.setText('')
        self.ventana.act_dni.setText('')
        self.ventana.act_cuit.setText('')
        self.ventana.act_categoria.setText('')
        self.ventana.act_sueldo.setText('')

    def buscarActualizarEmpleado(self):
        dniBuscado = self.ventana.act_buscar.text()
        dniEncontrado = buscarEmpleado(dniBuscado)

        self.ventana.act_nombre.setText(dniEncontrado[0])
        self.ventana.act_apellido.setText(dniEncontrado[1])
        self.ventana.act_dni.setText(str(dniEncontrado[2]))
        self.ventana.act_cuit.setText(str(dniEncontrado[3]))
        self.ventana.act_categoria.setText(dniEncontrado[4])
        self.ventana.act_sueldo.setText(str(dniEncontrado[5]))

    def buscarEliminarEmpleado(self):
        dniBuscado = self.ventana.eliminar_buscar.text()
        dniEncontrado = buscarEmpleado(dniBuscado)

        tabla = self.ventana.tabla_eliminar
        tabla.setRowCount(1)
        tabla.setColumnCount(6)
        tabla.setItem(0, 0, QTableWidgetItem(dniEncontrado[0]))
        tabla.setItem(0, 1, QTableWidgetItem(dniEncontrado[1]))
        tabla.setItem(0, 2, QTableWidgetItem(str(dniEncontrado[2])))
        tabla.setItem(0, 3, QTableWidgetItem(str(dniEncontrado[3])))
        tabla.setItem(0, 4, QTableWidgetItem(dniEncontrado[4]))
        tabla.setItem(0, 5, QTableWidgetItem(str(dniEncontrado[5])))

    def botonEliminarEmpleado(self):
        tabla = self.ventana.tabla_eliminar

        nombre = tabla.item(0, 0).text()
        apellido = tabla.item(0, 1).text()
        dni = tabla.item(0, 2).text()
        cuit = tabla.item(0, 3).text()
        categoria = tabla.item(0, 4).text()
        sueldo = tabla.item(0, 5).text()

        datosEmpleado = Empleado(3, nombre, apellido, dni, cuit, categoria, sueldo)
        eliminarEmpleado(datosEmpleado)

        tabla.setItem(0, 0, QTableWidgetItem(''))
        tabla.setItem(0, 1, QTableWidgetItem(''))
        tabla.setItem(0, 2, QTableWidgetItem(''))
        tabla.setItem(0, 3, QTableWidgetItem(''))
        tabla.setItem(0, 4, QTableWidgetItem(''))
        tabla.setItem(0, 5, QTableWidgetItem(''))
        self.ventana.eliminar_buscar.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Iniciar()
    sys.exit(app.exec())
