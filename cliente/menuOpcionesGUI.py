from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 432)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(-2, 10, 311, 421))
        self.label.setText("")

        # Modificación para establecer el color de fondo
        color = QColor(176, 190, 197)
        self.label.setStyleSheet(f"background-color: {color.name()};")

        self.label.setObjectName("label")
        self.bt_registrar = QtWidgets.QPushButton(parent=Form)
        self.bt_registrar.setGeometry(QtCore.QRect(100, 120, 131, 24))
        self.bt_registrar.setMinimumSize(QtCore.QSize(40, 0))
        self.bt_registrar.setObjectName("bt_registrar")
        self.bt_categoria = QtWidgets.QPushButton(parent=Form)
        self.bt_categoria.setGeometry(QtCore.QRect(100, 170, 131, 24))
        self.bt_categoria.setMinimumSize(QtCore.QSize(40, 0))
        self.bt_categoria.setObjectName("bt_categoria")
        self.bt_estadistica = QtWidgets.QPushButton(parent=Form)
        self.bt_estadistica.setGeometry(QtCore.QRect(100, 230, 131, 24))
        self.bt_estadistica.setObjectName("bt_estadistica")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 161, 41))
        self.label_2.setStyleSheet("font: 700 10pt \"Segoe UI\";\n"
                                   "color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(164, 310, 101, 24))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_registrar.setText(_translate("Form", "REGISTRAR PERSONAL"))
        self.bt_categoria.setText(_translate("Form", "CATEGORIA"))
        self.bt_estadistica.setText(_translate("Form", "ESTADISTICA"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "        ELIJA UNA OPCION"))
        self.pushButton_4.setText(_translate("Form", "SALIR"))
