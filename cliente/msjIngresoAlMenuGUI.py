# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'correct.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowMsj(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 391, 331))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgba(0,0,0,130);\n"
"\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgba(0,0,0,150);\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"background-color: rgba(0,0,0,170);\n"
"border-radius: 15px;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 301))
        self.label.setStyleSheet("background-color: rgba(0,0,0,120);\n"
"border-bottom-left-radius: 40px;\n"
"border-bottom-right-radius: 40px;\n"
"border-top-left-radius: 40px;\n"
"border-top-right-radius: 40px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 241, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 301, 121))
        self.label_2.setStyleSheet("font: italic 28pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Has ingresado</p><p align=\"center\">correctamente</p></body></html>"))

