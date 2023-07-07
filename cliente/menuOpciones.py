import sys
from PyQt6.QtWidgets import QApplication, QWidget
from menuOpcionesGUI import Ui_Form
import registroPersona

from estadisticaDeSueldos.diseñoEstadistica import EstadisticaGUI


class Ui_iniciar(QWidget):
    def __init__(self):
        super(Ui_iniciar, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Botones
        self.ui.bt_registrar.clicked.connect(self.abrir_registro)
        self.ui.bt_categoria.clicked.connect(self.categoria)
        self.ui.bt_estadistica.clicked.connect(self.estadistica)
        self.ui.pushButton_4.clicked.connect(self.salir)

        self.show()

    def abrir_registro(self):

        self.hide()
        self.registro_persona = registroPersona.Iniciar()
        self.registro_persona.show()

    def registrar(self):
        print("registrar")


    def categoria(self):
        print("categoria")

    def estadistica(self):

        self.ventana_estadistica = EstadisticaGUI()
        self.ventana_estadistica.show()
        self.hide()

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_iniciar = Ui_iniciar()
    sys.exit(app.exec())
