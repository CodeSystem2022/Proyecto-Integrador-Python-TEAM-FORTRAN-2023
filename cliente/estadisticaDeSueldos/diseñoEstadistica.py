import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel, QDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen, QFont
from PyQt5.QtCore import Qt, QSize



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from model.empleado_Dao import EmpleadoDao

class FancyFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Raised)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Establecer color y grosor del borde
        border_color = QColor(50, 50, 50)
        border_thickness = 2

        # Establecer el color de fondo
        background_color = QColor(168, 216, 185)  # Tonos de verde claro pastel

        # Dibujar el fondo de la interfaz
        painter.setBrush(QBrush(background_color))
        painter.drawRect(self.rect())

        # Dibujar el recuadro con borde redondeado
        painter.setPen(QPen(border_color, border_thickness))
        painter.drawRoundedRect(
            self.rect().adjusted(border_thickness, border_thickness, -border_thickness, -border_thickness),
            10,
            10
        )


class ModaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Moda")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #3CB371;")  # Color verde esmeralda

        layout = QVBoxLayout()

        label = QLabel("Calculo de la Moda de todos los sueldos:")
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        button = QPushButton("Calcular")
        button.clicked.connect(self.calcular_moda)
        button.setStyleSheet(
            "background-color: #01CD01; border-radius: 10px; font-size: 18px; font-weight: bold; padding: 10px; color: white;")
        layout.addWidget(button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setFont(QFont("Arial", 12))

    def calcular_moda(self):
        sueldos = EmpleadoDao.calcular_moda()
        self.result_label.setText(f"Moda: {sueldos}")



class MediaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Media")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #3CB371;")  # Color verde esmeralda

        layout = QVBoxLayout()

        label = QLabel("Calculo de la Media de todos los sueldos:")
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        button = QPushButton("Calcular")
        button.clicked.connect(self.calcular_media)
        button.setStyleSheet(
            "background-color: #18D19C; border-radius: 10px; font-size: 18px; font-weight: bold; padding: 10px; color: white;")
        layout.addWidget(button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setFont(QFont("Arial", 12))

    def calcular_media(self):
        sueldos = EmpleadoDao.calcular_media()

        self.result_label.setText(f"Media: {sueldos}")


class MedianaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Mediana")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #3CB371;")  # Color verde esmeralda

        layout = QVBoxLayout()

        label = QLabel("Calculo de la Mediana de todos los sueldos:")
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)


        button = QPushButton("Calcular")
        button.clicked.connect(self.calcular_mediana)
        button.setStyleSheet(
            "background-color: #13906C; border-radius: 10px; font-size: 18px; font-weight: bold; padding: 10px; color: white;")
        layout.addWidget(button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setFont(QFont("Arial", 12))

    def calcular_mediana(self):
        sueldos = EmpleadoDao.calcular_mediana()

        self.result_label.setText(f"Mediana: {sueldos}")


class EstadisticaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Estadistica")
        self.setGeometry(100, 100, 500, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Título
        titulo = QLabel("Estadistica", self)
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo) 

        # Frame superior
        frame_superior = FancyFrame(self)  # Usamos nuestro FancyFrame en lugar de QFrame
        frame_superior.setStyleSheet("background-color: #A8D8B9;")
        layout.addWidget(frame_superior)

        layout_superior = QHBoxLayout(frame_superior)
        layout_superior.setContentsMargins(0, 0, 0, 0)

        bt_moda = QPushButton("Moda", self)
        bt_moda.setStyleSheet(
            """
            QPushButton {
                background-color: #2ECC71;
                border-radius: 20px;
                color: #FFFFFF;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            """
        )
        layout_superior.addWidget(bt_moda)
        bt_moda.clicked.connect(self.abrir_moda_window)

        bt_mediana = QPushButton("Mediana", self)
        bt_mediana.setStyleSheet(
            """
            QPushButton {
                background-color: #2ECC71;
                border-radius: 20px;
                color: #FFFFFF;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            """
        )
        layout_superior.addWidget(bt_mediana)
        bt_mediana.clicked.connect(self.abrir_mediana_window)

        bt_media = QPushButton("Media", self)
        bt_media.setStyleSheet(
            """
            QPushButton {
                background-color: #2ECC71;
                border-radius: 20px;
                color: #FFFFFF;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
            """
        )
        layout_superior.addWidget(bt_media)
        bt_media.clicked.connect(self.abrir_media_window)

        # Resto del contenido de la interfaz
        frame_contenido = FancyFrame(self)  # Usamos nuestro FancyFrame en lugar de QFrame
        layout.addWidget(frame_contenido)

        layout_contenido = QHBoxLayout(frame_contenido)
        layout_contenido.setContentsMargins(0, 0, 0, 0)

        self.show()

    def abrir_moda_window(self):
        dialog = ModaWindow()
        dialog.exec_()

    def abrir_mediana_window(self):
        dialog = MedianaWindow()
        dialog.exec_()

    def abrir_media_window(self):
        dialog = MediaWindow()
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = EstadisticaGUI()
    sys.exit(app.exec_())  
