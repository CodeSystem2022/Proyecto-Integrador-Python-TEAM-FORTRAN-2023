import sys
from PyQt6.QtWidgets import QApplication, QWidget
from menuOpcionesGUI import Ui_Form

class Ui_iniciar(QWidget):
    def __init__(self):
        super(Ui_iniciar, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Botones
        self.ui.bt_registrar.clicked.connect(self.registrar)
        self.ui.bt_categoria.clicked.connect(self.categoria)
        self.ui.bt_estadistica.clicked.connect(self.estadistica)

        self.show()

    def registrar(self):
        print("registrar")

    def categoria(self):
        print("categoria")

    def estadistica(self):
        print("estadistica")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_iniciar = Ui_iniciar()
    sys.exit(app.exec())
