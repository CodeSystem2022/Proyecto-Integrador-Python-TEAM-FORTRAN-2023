import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel,  QDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class FancyFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

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

        label = QLabel("Ingrese los Saldos separados por comas:")
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        button = QPushButton("Calcular")
        button.clicked.connect(self.calcular_moda)
        button.setStyleSheet("background-color: #01CD01; border-radius: 10px; font-size: 18px; font-weight: bold; padding: 10px; color: white;")
        layout.addWidget(button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setFont(QFont("Arial", 12))

    def calcular_moda(self):
        valores = self.input_line.text().split(',')
        valores = [float(valor) for valor in valores]

        contador = {}
        for valor in valores:
            if valor in contador:
                contador[valor] += 1
            else:
                contador[valor] = 1

        moda = max(contador, key=contador.get)

        self.result_label.setText(f"Moda: {moda}")
    

class MediaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Media")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #3CB371;")  # Color verde esmeralda

        layout = QVBoxLayout()

        label = QLabel("Ingrese los Saldos separados por comas:")
        label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(label)

        self.input_line = QLineEdit()
        layout.addWidget(self.input_line)

        button = QPushButton("Calcular")
        button.clicked.connect(self.calcular_media)
        button.setStyleSheet("background-color: #18D19C; border-radius: 10px; font-size: 18px; font-weight: bold; padding: 10px; color: white;")
        layout.addWidget(button)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setFont(QFont("Arial", 12))


    def calcular_media(self):
        valores = self.input_line.text().split(',')
        valores = [float(valor) for valor in valores]
        media = sum(valores) / len(valores)

        self.result_label.setText(f"Media: {media}")


