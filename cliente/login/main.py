import sys
from res import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from messagebox import msg_error

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login.ui", self)
        self.pushButton.clicked.connect(self.gui_login)
    def gui_login(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(name) == 0 or len(password) == 0:
            msg_error("Error","No hay datos")
        elif name == "UTN" and password == "123":
            self.window_access()
        else:
            msg_error("Error", "Los datos no coinciden")
    def window_access(self):
        ventana_2 = Gui_access()
        widget.addWidget(ventana_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #widget.move(200, 50)
        widget.setFixedHeight(400)
        widget.setFixedWidth(421)

class Gui_access(QMainWindow):
    def __init__(self):
        super(Gui_access, self).__init__()
        loadUi("correct.ui", self)
        self.pushButton.clicked.connect(self.regresar_login)

    def regresar_login(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.move(400, 80)
        widget.setFixedHeight(500)
        widget.setFixedWidth(500)

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


















