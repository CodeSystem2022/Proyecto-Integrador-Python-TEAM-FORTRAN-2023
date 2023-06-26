from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from database.empleado import Empleado

class iniciar:
    def __init__(self):
        app = QtWidgets.QApplication([])
        # ventana principal de la opcion registrar persona   
        self.ventana = uic.loadUi("cliente\\registroPersona\diseñoResitroPersona.ui")
        self.ventana.show()
        
        # asignacion funcionalidad a botones que llevan a diferentes secciones
        self.ventana.bt_datos.clicked.connect(self.seccionMostrarBaseDatos)
        self.ventana.bt_registrar.clicked.connect(self.seccionRegistrar)
        self.ventana.bt_actualizar.clicked.connect(self.seccionActualizar)
        self.ventana.bt_eliminar_2.clicked.connect(self.seccionEliminar)
        
        # asignacion funcionalidad a botones en cada seccion
        self.ventana.bt_agregar.clicked.connect(self.agregarEmpleado)
        
        # apenas ingresa a la opcion registroPersona carga y muestra la base de datos
        mostrarEmpleados(self)
        
        app.exec()
    # funcionalidades de botones que llevan a diferentes secciones
    def seccionMostrarBaseDatos(self):
        self.ventana.stackedWidget.setCurrentIndex(0)
        mostrarEmpleados(self)
        
    def seccionRegistrar(self):
        self.ventana.stackedWidget.setCurrentIndex(1)
        
    def seccionActualizar(self):
        self.ventana.stackedWidget.setCurrentIndex(2)

    def seccionEliminar(self):
        self.ventana.stackedWidget.setCurrentIndex(3)
     # metodo para cargar un empleado
    def agregarEmpleado(self):
        nombre = self.ventana.reg_nombre.text()
        apellido = self.ventana.reg_apellido.text()
        dni = self.ventana.reg_dni.text()
        cuit = self.ventana.reg_cuit.text()
        categoria = self.ventana.reg_categoria.text()
        sueldo = self.ventana.reg_sueldo.text()
        
        datosEmpleado = Empleado(1, nombre, apellido, dni, cuit, categoria, sueldo)
        # realiza la consulta correspondiente a la base de datos
        insertarEmpleado(datosEmpleado)
        
        self.ventana.reg_nombre.setText('')
        self.ventana.reg_apellido.setText('')
        self.ventana.reg_dni.setText('')
        self.ventana.reg_cuit.setText('')
        self.ventana.reg_categoria.setText('')
        self.ventana.reg_sueldo.setText('')
    