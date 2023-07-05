import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from model.empleado_Dao import EmpleadoDao


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda de datos por DNI")
        self.setGeometry(200, 200, 700, 500)  # Ajusta la posición y el tamaño de la ventana

        # Widget principal
        widget = QWidget()
        self.setCentralWidget(widget)

        # Layout principal
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Etiqueta y campo de entrada para el DNI
        self.label = QLabel("Digite el DNI:")
        self.line_edit = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_data)
        layout.addWidget(self.search_button)

        # Tabla de datos
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Nombre", "Apellido", "DNI", "CUIT", "Estado", "Sueldo"])
        layout.addWidget(self.table)

        # Establecer el esquema de color verde esmeralda
        self.set_green_palette()

    def set_green_palette(self):
        palette = QPalette()
        green = QColor(46, 204, 113)  # Verde esmeralda: RGB(46, 204, 113)
        palette.setColor(QPalette.Window, green)
        self.setPalette(palette)

    def search_data(self):
        dni = self.line_edit.text()
        empleado_dao = EmpleadoDao()  # Crear una instancia de EmpleadoDao
        empleado = empleado_dao.buscar_por_dni(dni)  # Llamar al método en la instancia
        if empleado:
            self.table.setRowCount(1)
            self.table.setItem(0, 0, QTableWidgetItem(empleado.nombre))
            self.table.setItem(0, 1, QTableWidgetItem(empleado.apellido))
            self.table.setItem(0, 2, QTableWidgetItem(empleado.dni))
            self.table.setItem(0, 3, QTableWidgetItem(str(empleado.sueldo)))
        else:
            self.table.setRowCount(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 