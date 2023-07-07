import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from formulario import Ui_MainWindowfrom
from model.empleado_Dao import EmpleadoDao
from Recibo import ReciboSueldo


class Formulario(QMainWindow, Ui_MainWindowfrom):
    def __init__(self):
        super().__init__()
        try:
            self.setupUi(self)
        except Exception as e:
            print("Error al cargar el archivo UI:", str(e))

        # Botones
        self.bt_buscar.clicked.connect(self.search_data)

    # Funciones
    def search_data(self):
        dni_a_buscar = self.in_dni.text()
        empleado = EmpleadoDao.buscar_por_dni(dni_a_buscar)
        if empleado:
            print("Empleado encontrado:", empleado)  # Mensaje de depuración
            # Obtener los datos del empleado
            dni = empleado.dni
            nombre = empleado.nombre
            apellido = empleado.apellido
            cuit = empleado.cuit
            categoria = empleado.categoria
            sueldo = empleado.sueldo

            # Llamar directamente a la función obtener_recibo en ReciboSueldo
            print("Llamando a la función obtener_recibo en Recibo.py")  # Mensaje de depuración
            app = QApplication.instance()  # Obtener la instancia de la aplicación
            recibo = ReciboSueldo(dni, nombre, apellido, cuit, categoria, sueldo)
            recibo.show()
        else:
            QMessageBox.warning(self, "Error", "Empleado no encontrado.")

if __name__ == '__main__':
    app = QApplication([])
    window = Formulario()
    window.show()
    sys.exit(app.exec())
