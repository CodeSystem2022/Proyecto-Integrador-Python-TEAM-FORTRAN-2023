import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import Qt
from diseñoRegistroPersonaPy import Ui_MainWindow
import menuOpciones
from model.empleado_Dao import EmpleadoDao, crear_tabla, Empleado


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

        self.seccionMostrarBaseDatos()

        self.show()

    def seccionMostrarBaseDatos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)
        empleados = EmpleadoDao.seleccionar()
        self.mostrarEmpleados(empleados)

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

    def mostrarEmpleados(self, empleados):
        self.ventana.tabla_productos.setRowCount(len(empleados))
        self.ventana.tabla_productos.setColumnCount(6)
        for i, empleado in enumerate(empleados):
            self.ventana.tabla_productos.setItem(i, 0, QTableWidgetItem(empleado.nombre))
            self.ventana.tabla_productos.setItem(i, 1, QTableWidgetItem(empleado.apellido))
            self.ventana.tabla_productos.setItem(i, 2, QTableWidgetItem(empleado.dni))
            self.ventana.tabla_productos.setItem(i, 3, QTableWidgetItem(empleado.cuit))
            self.ventana.tabla_productos.setItem(i, 4, QTableWidgetItem(empleado.categoria))
            self.ventana.tabla_productos.setItem(i, 5, QTableWidgetItem(str(empleado.sueldo)))

    def agregarEmpleado(self):
        try:
            nombre = self.ventana.reg_nombre.text()
            apellido = self.ventana.reg_apellido.text()
            dni = int(self.ventana.reg_dni.text())
            cuit = self.ventana.reg_cuit.text()
            categoria = self.ventana.reg_categoria.text()
            sueldo = int(self.ventana.reg_sueldo.text())

            empleado = Empleado(nombre, apellido, dni, cuit, categoria, sueldo)  # Crear instancia de Empleado
            EmpleadoDao.insertar(empleado)  # Pasar la instancia de Empleado como argumento
            self.ventana.reg_nombre.clear()
            self.ventana.reg_apellido.clear()
            self.ventana.reg_dni.clear()
            self.ventana.reg_cuit.clear()
            self.ventana.reg_categoria.clear()
            self.ventana.reg_sueldo.clear()
            self.seccionMostrarBaseDatos()
        except Exception as e:
            print("Error al agregar empleado:", str(e))

    def actualizarEmpleado(self):
        try:
            nombre = self.ventana.act_nombre.text()
            apellido = self.ventana.act_apellido.text()
            dni = int(self.ventana.act_dni.text())
            cuit = self.ventana.act_cuit.text()
            categoria = self.ventana.act_categoria.text()
            sueldo = float(self.ventana.act_sueldo.text().replace(',', '.'))

            empleado = Empleado(nombre, apellido, dni, cuit, categoria, sueldo)
            EmpleadoDao.actualizar(empleado)

            self.ventana.act_nombre.clear()
            self.ventana.act_apellido.clear()
            self.ventana.act_dni.clear()
            self.ventana.act_cuit.clear()
            self.ventana.act_categoria.clear()
            self.ventana.act_sueldo.clear()

            self.seccionMostrarBaseDatos()
        except Exception as e:
            print("Error al actualizar empleado:", str(e))

    def buscarActualizarEmpleado(self):
        try:
            dniBuscado = self.ventana.act_buscar.text()
            print("Valor de dniBuscado:", dniBuscado)  # Agrega esta línea de depuración
            empleado = EmpleadoDao.buscar_por_dni(dniBuscado)
            if empleado:
                self.ventana.act_nombre.setText(empleado.nombre)
                self.ventana.act_apellido.setText(empleado.apellido)
                self.ventana.act_dni.setText(empleado.dni)
                self.ventana.act_cuit.setText(empleado.cuit)
                self.ventana.act_categoria.setText(empleado.categoria)
                self.ventana.act_sueldo.setText(str(empleado.sueldo))  # Convertir a cadena de texto
        except Exception as e:
            print("Error al actualizar empleado:", str(e))

    def buscarEliminarEmpleado(self):
        try:
            dniBuscado = self.ventana.eliminar_buscar.text()
            empleado = EmpleadoDao.buscar_por_dni(dniBuscado)
            if empleado:
                tabla = self.ventana.tabla_eliminar
                tabla.setRowCount(1)
                tabla.setColumnCount(6)
                tabla.setItem(0, 0, QTableWidgetItem(empleado.nombre))
                tabla.setItem(0, 1, QTableWidgetItem(empleado.apellido))
                tabla.setItem(0, 2, QTableWidgetItem(empleado.dni))
                tabla.setItem(0, 3, QTableWidgetItem(empleado.cuit))
                tabla.setItem(0, 4, QTableWidgetItem(empleado.categoria))
                tabla.setItem(0, 5, QTableWidgetItem(str(empleado.sueldo)))
        except Exception as e:
         print("Error al eliminar1 empleado:", str(e))

    def botonEliminarEmpleado(self):
        try:
            tabla = self.ventana.tabla_eliminar

            dni = tabla.item(0, 2).text()
            empleado = EmpleadoDao.buscar_por_dni(dni)

            if empleado:
                EmpleadoDao.eliminar(empleado)
                tabla.setItem(0, 0, QTableWidgetItem(''))
                tabla.setItem(0, 1, QTableWidgetItem(''))
                tabla.setItem(0, 2, QTableWidgetItem(''))
                tabla.setItem(0, 3, QTableWidgetItem(''))
                tabla.setItem(0, 4, QTableWidgetItem(''))
                tabla.setItem(0, 5, QTableWidgetItem(''))
                self.ventana.eliminar_buscar.setText('')
                self.seccionMostrarBaseDatos()
        except Exception as e:
         print("Error al eliminar2 empleado:", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Iniciar()
    sys.exit(app.exec())
