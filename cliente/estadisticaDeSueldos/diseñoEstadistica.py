import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel
from PyQt5.QtCore import Qt

class EstadisticaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estadistica")
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
        frame_superior = QFrame(self)
        frame_superior.setStyleSheet("background-color: rgb(0, 0, 0);")
        frame_superior.setFrameShape(QFrame.StyledPanel)
        frame_superior.setFrameShadow(QFrame.Raised)
        layout.addWidget(frame_superior)

        layout_superior = QHBoxLayout(frame_superior)
        layout_superior.setContentsMargins(0, 0, 0, 0)

        bt_moda = QPushButton("Moda", self)
        bt_moda.setStyleSheet(
            """
            QPushButton {
                background-color: #FF0000;
                border-radius: 20px;
                color: #FFFFFF;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #FF9999;
            }
            """
        )
        layout_superior.addWidget(bt_moda)

        bt_mediana = QPushButton("Mediana", self)
        bt_mediana.setStyleSheet(
            """
            QPushButton {
                background-color: #00FF00;
                border-radius: 20px;
                color: #000000;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #99FF99;
            }
            """
        )
        layout_superior.addWidget(bt_mediana)

        bt_media = QPushButton("Media", self)
        bt_media.setStyleSheet(
            """
            QPushButton {
                background-color: #0000FF;
                border-radius: 20px;
                color: #FFFFFF;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #9999FF;
            }
            """
        )
        layout_superior.addWidget(bt_media)

        # Resto del contenido de la interfaz
        frame_contenido = QFrame(self)
        frame_contenido.setFrameShape(QFrame.StyledPanel)
        frame_contenido.setFrameShadow(QFrame.Raised)
        layout.addWidget(frame_contenido)

        layout_contenido = QHBoxLayout(frame_contenido)
        layout_contenido.setContentsMargins(0, 0, 0, 0)

        # Aquí puedes agregar más widgets o elementos de la interfaz

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = EstadisticaGUI()
    sys.exit(app.exec_())


