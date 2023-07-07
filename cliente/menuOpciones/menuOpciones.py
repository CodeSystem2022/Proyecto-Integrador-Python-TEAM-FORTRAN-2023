import sys
from PyQt6.QtWidgets import QApplication,QWidget
from menuOpciones import Ui_from
class Ui_from(QWidget):
    def __init__(self,form):
        super(Ui_from, self).__init__()
        self.ui=Ui_from
        self.ui.setupUi(self)
        self.show()
       #Botones
        self.ui.registrar.clicked.connect(self.registrar)
        self.ui.categoria.clicked.connect(self.categoria)
        self.ui.estadistica.clicked.connect(self.estadistica)
        #redirreccionar
        self.setWindowTitle("RegistroPersonal")
        self.setWindowTitle("Categoria")
        self.setWindowTitle("Estadistica")


        def registrar(self):
            print("registrar")
        def categoria(self):
            print("categoria")
        def estadistica():
            print("estadistica")



if __name__=="__main__":
    app=QApplication(sys.argv)
    menuOpciones=Ui_from()
    sys.exit(app.exec())










