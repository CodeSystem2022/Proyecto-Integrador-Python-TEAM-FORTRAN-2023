from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindowfrom(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 333)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.label.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.in_dni = QtWidgets.QLineEdit(parent=self.frame)
        self.in_dni.setGeometry(QtCore.QRect(110, 40, 121, 22))
        self.in_dni.setText("")
        self.in_dni.setPlaceholderText("")
        self.in_dni.setObjectName("in_dni")
        self.bt_buscar = QtWidgets.QPushButton(parent=self.frame)
        self.bt_buscar.setGeometry(QtCore.QRect(240, 40, 75, 24))
        self.bt_buscar.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.bt_buscar.setObjectName("bt_buscar")
        self.bt_salir = QtWidgets.QPushButton(parent=self.frame)
        self.bt_salir.setGeometry(QtCore.QRect(320, 40, 75, 24))
        self.bt_salir.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.bt_salir.setObjectName("bt_salir")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INGRESE SU DNI"))
        self.bt_buscar.setText(_translate("MainWindow", "BUSCAR"))
        self.bt_salir.setText(_translate("MainWindow", "LIMPIAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowfrom()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
