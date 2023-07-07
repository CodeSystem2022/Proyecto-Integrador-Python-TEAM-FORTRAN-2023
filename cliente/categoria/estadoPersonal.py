import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from formulario import Ui_MainWindowfrom
from model.empleado_Dao import EmpleadoDao

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))



class Formulario(QMainWindow, Ui_MainWindowfrom):
    def __init__(self):
        super().__init__()
        try:
            self.setupUi(self)
        except Exception as e:
            print("Error al cargar el archivo UI:", str(e))

        # Botones
        self.bt_buscar.clicked.connect(self.search_data)
        #self.bt_limpiar.clicked.connect(self.clear_data)
        #self.bt_regresar.clicked.connect(self.return_data)
        #self.bt_salir.clicked.connect(self.output_data)

    # Funciones
    def search_data(self):
        dni_a_buscar = self.in_dni.text()
        empleado = EmpleadoDao.buscar_por_dni(dni_a_buscar)

    #def clear_data(self):
        #self.in_dni.clear()

def llamarRecibo():
    subprocess.run(['python', 'Recibo.py'])

if __name__ == '__main__':
    llamarRecibo()
    app = QApplication([])
    window = Formulario()
    window.show()
    sys.exit(app.exec())
