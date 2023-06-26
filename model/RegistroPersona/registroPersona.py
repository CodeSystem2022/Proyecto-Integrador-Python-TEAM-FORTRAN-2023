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
        self.ventana.bt_refrescar.clicked.connect(self.seccionMostrarBaseDatos)
        self.ventana.bt_actualizar_tabla.clicked.connect(self.actualizarEmpleado)
        self.ventana.bt_actualizar_buscar.clicked.connect(self.buscarActualizarEmpleado)
        self.ventana.bt_buscar_borrar.clicked.connect(self.buscarEliminarEmpleado)
        self.ventana.bt_eliminar.clicked.connect(self.botonEliminarEmpleado)
        
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
    
    # funcionalidad para boton actualizar en seccion actualizar
    def actualizarEmpleado(self):
        # lee los campos de entrada correspondientes
        nombre = self.ventana.act_nombre.text()
        apellido = self.ventana.act_apellido.text()
        dni = self.ventana.act_dni.text()
        cuit = self.ventana.act_cuit.text()
        categoria = self.ventana.act_categoria.text()
        sueldo = self.ventana.act_sueldo.text()
        
        datosEmpleado = Empleado(1, nombre, apellido, dni, cuit, categoria, sueldo)
        # realiza la consulta correspondiente a la base de datos
        actualizarEmpleado(datosEmpleado)
    
        self.ventana.act_nombre.setText('')
        self.ventana.act_apellido.setText('')
        self.ventana.act_dni.setText('')
        self.ventana.act_cuit.setText('')
        self.ventana.act_categoria.setText('')
        self.ventana.act_sueldo.setText('')
        
    # funcionalidad boton buscar en seccion actualizar
    def buscarActualizarEmpleado(self):
        dniBuscado = self.ventana.act_buscar.text()
        dniEncontrado = buscarEmpleado(dniBuscado)
        
        self.ventana.act_nombre.setText(dniEncontrado[0])
        self.ventana.act_apellido.setText(dniEncontrado[1])
        self.ventana.act_dni.setText(str(dniEncontrado[2]))
        self.ventana.act_cuit.setText(str(dniEncontrado[3]))
        self.ventana.act_categoria.setText(dniEncontrado[4])
        self.ventana.act_sueldo.setText(str(dniEncontrado[5]))
        
    # metodo para buscar empleado en seccion eliminar
    def buscarEliminarEmpleado(self):
        # lee el dni buscado
        dniBuscado = self.ventana.eliminar_buscar.text()
        # realiza la consulta a la base de datos
        dniEncontrado = buscarEmpleado(dniBuscado)
        
        tabla = self.ventana.tabla_eliminar
        tabla.setRowCount(1)
        tabla.setColumnCount(6)
        # muestra el empleado buscado
        tabla.setItem(0, 0, QTableWidgetItem(dniEncontrado[0])) 
        tabla.setItem(0, 1, QTableWidgetItem(dniEncontrado[1]))  
        tabla.setItem(0, 2, QTableWidgetItem(str(dniEncontrado[2])))  
        tabla.setItem(0, 3, QTableWidgetItem(str(dniEncontrado[3])))  
        tabla.setItem(0, 4, QTableWidgetItem(dniEncontrado[4]))  
        tabla.setItem(0, 5, QTableWidgetItem(str(dniEncontrado[5])))
        
    # funcionalidad boton eliminar en seccion eliminar empleado
    def botonEliminarEmpleado(self):
        tabla = self.ventana.tabla_eliminar
        
        # lee los datos de la tabla
        nombre = tabla.item(0,0).text()
        apellido = tabla.item(0,1).text()
        dni = tabla.item(0,2).text()
        cuit = tabla.item(0,3).text()
        categoria = tabla.item(0,4).text()
        sueldo = tabla.item(0,5).text()
        # instancia de Empleado con los datos cargados
        datosEmpleado = Empleado(3, nombre, apellido, dni, cuit, categoria, sueldo)
        # realiza la consulta correspondiente a la base de datos
        eliminarEmpleado(datosEmpleado)
        #  limpia los campos de entrada
        tabla.setItem(0, 0, QTableWidgetItem('')) 
        tabla.setItem(0, 1, QTableWidgetItem(''))  
        tabla.setItem(0, 2, QTableWidgetItem(''))  
        tabla.setItem(0, 3, QTableWidgetItem(''))  
        tabla.setItem(0, 4, QTableWidgetItem(''))  
        tabla.setItem(0, 5, QTableWidgetItem(''))
        self.ventana.eliminar_buscar.setText('')