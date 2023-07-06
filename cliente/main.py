import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from messagebox import msg_error
from loginGUI import Ui_MainWindow
from msjIngresoAlMenuGUI import Ui_MainWindowMsj
import menuOpciones

class WelcomeScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        try:
            self.setupUi(self)
        except Exception as e:
            print("Error al cargar el archivo UI:", str(e))

        self.pushButton.clicked.connect(self.gui_login)
        self.pushButton_2.clicked.connect(self.salir_app)

    def gui_login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(name) == 0 or len(password) == 0:
            msg_error("Error","No hay datos")
        elif name == "UTN" and password == "1234":
            self.window_access()
        else:
            msg_error("Error", "Los datos no coinciden")

    def window_access(self):
        ventana_2 = Gui_access()
        widget.addWidget(ventana_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(400)
        widget.setFixedWidth(421)

    def salir_app(self):
        sys.exit()

class Gui_access(QMainWindow, Ui_MainWindowMsj):
    def __init__(self):
        super(Gui_access, self).__init__()
        try:
            self.setupUi(self)
        except Exception as e:
            print("Error al cargar los archivos UI:", str(e))

        self.pushButton.clicked.connect(self.regresar_login)

    def regresar_login(self):
        self.menu_principal = menuOpciones.Ui_iniciar()
        self.menu_principal.show()

# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.move(400, 80)
widget.setFixedHeight(500)
widget.setFixedWidth(500)
widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")
