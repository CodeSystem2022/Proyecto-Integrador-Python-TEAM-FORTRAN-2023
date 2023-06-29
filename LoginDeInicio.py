from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg2

class RegisterDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Register")
        self.resize(300, 200)
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel("New User Registration")
        self.label.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.layout.addWidget(self.label)

        self.username_label = QtWidgets.QLabel("Username:")
        self.username_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QtWidgets.QLabel("Password:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.button_box = QtWidgets.QDialogButtonBox()
        self.register_button = self.button_box.addButton(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.cancel_button = self.button_box.addButton(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.layout.addWidget(self.button_box)

        self.register_button.clicked.connect(self.register)
        self.cancel_button.clicked.connect(self.reject)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Perform registration logic here
        print("Registering user:", username, "with password:", password)
        self.accept()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 600))
        MainWindow.setMaximumSize(QtCore.QSize(700, 600))
        MainWindow.setBaseSize(QtCore.QSize(700, 600))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "QWidget#centralwidget{\n"
            "\n"
            "font: 75 italic 16pt \"Times New Roman\";\n"
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));}"
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius:10px;\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 180, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 240, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 181, 71))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 190, 191, 20))
        self.lineEdit.setStyleSheet("border-radius:10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 250, 161, 20))
        self.lineEdit_2.setStyleSheet("border-radius:10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 151, 31))
        self.pushButton.setStyleSheet("border-radius:10px;\n"
                                       "font: 87 12pt \"Arial Black\";\n"
                                       "background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 121, 31))
        self.pushButton_2.setStyleSheet("border-radius:10px;\n"
                                         "\n"
                                         "background-color: rgb(85, 255, 127);\n"
                                         "\n"
                                         "font: 87 16pt \"Arial Black\";\n"
                                         "\n"
                                         "")
        self.pushButton_2.setObjectName("pushButton_2")

        # Register button
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 130, 151, 31))
        self.pushButton_3.setStyleSheet("border-radius:10px;\n"
                                         "font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.show_register_dialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" color:#55557f;\">Bienvenidos al Team Fortran</span></p></body></html>"))
        self.label_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#ff0000;\">Ingreso al Sistema</span></p></body></html>"))
        self.label_3.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Usuario:</span></p></body></html>"))
        self.label_4.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Contraseña:</span></p></body></html>"))
        self.label_5.setText(
            _translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Por favor,Registrese:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton_2.setText(_translate("MainWindow", "Ingresar"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))

    def show_register_dialog(self):
        dialog = RegisterDialog(parent=self.centralwidget)
        result = dialog.exec()
        if result == QtWidgets.QDialog.DialogCode.Accepted:
            # Registration successful, perform necessary actions
            username = dialog.username_input.text()
            password = dialog.password_input.text()
            # Save the new user's data or perform other operations
            print("Registered user:", username, "with password:", password)
        else:
            # Registration canceled
            print("Registration canceled")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
