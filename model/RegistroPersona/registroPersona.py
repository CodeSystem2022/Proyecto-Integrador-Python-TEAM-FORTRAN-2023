from PyQt5 import QtWidgets, uic

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