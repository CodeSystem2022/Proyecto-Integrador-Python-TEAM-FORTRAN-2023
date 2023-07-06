from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Recibo import ReciboSueldo
from formulario import Ui_MainWindowfrom
from model.empleado_Dao import EmpleadoDao


class Formulario(QMainWindow, Ui_MainWindowfrom):
    def __init__(self):
        super(Formulario, self).__init__()
        try:
            self.setupUi(self)
        except Exception as e:
            print("Error al cargar el archivo UI:", str(e))

        #Botones
        self.bt_buscar.clicked.connect(self.search_data)
        self.bt_limpiar.clicked.connect(self.clear_data)
        self.bt_regresar.clicked.connect(self.return_data)
        self.bt_salir.clicked.connect(self.output_data)

    # Funciones
    def search_data(self):
        dni_a_buscar = self.in_dni.text()
        empleado = EmpleadoDao.obtener_empleado_por_dni(dni_a_buscar)

        if empleado is not None:
            # Otros campos de la interfaz
            recibo = ReciboSueldo(empleado)
            recibo.show()
        else:
            QMessageBox.warning(self, "Error", "No se encontró un empleado con el DNI proporcionado.")
            self.clear_data()

    def clear_data(self):
        self.in_dni.clear()

if __name__ == '__main__':
    app = QApplication([])
    window = Formulario()
    window.show()
    app.exec()