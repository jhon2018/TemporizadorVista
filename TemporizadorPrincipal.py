from PyQt5 import QtWidgets
from TemporizarVista_ui import *
from PyQt5.QtWidgets import QApplication
from conexion.FuncionesSQL import *
import sys,time
from PyQt5.QtCore import QTimer

# Clase principal de la aplicación
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MonitorVista()
        self.ui.setupUi(self)
        self.SQLfunciones=FuncionesSQL()


        # Inicializar y configurar el temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.TiempoReal_TBL_VISTA)
        self.timer.start(4000)  # Intervalo en milisegundos (en este caso, 4 segundos)

        self.ui.btnBorrar.clicked.connect(self.limpiar_tblVista)
        self.VistaDatosCinta()

    def VistaDatosCinta(self):
        self.ui.btnMostrar.clicked.connect(self.MOSTRAR_TBL_CINTA)

        
        self.ui.tblVista.setColumnWidth(0,90)
        self.ui.tblVista.setColumnWidth(1,110)
        self.ui.tblVista.setColumnWidth(2,110)
        self.ui.tblVista.setColumnWidth(3,81)

        

    def MOSTRAR_TBL_CINTA(self):
         Vercinta=self.SQLfunciones.MOSTRAR_CINTA()
         
         i=len(Vercinta)
         #print(Vercinta)
         self.ui.tblVista.setRowCount(i)
         tableRow=0
         for row in Vercinta:
            self.ui.tblVista.setItem(tableRow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tblVista.setItem(tableRow,1,QtWidgets.QTableWidgetItem(str(row[1])))
            self.ui.tblVista.setItem(tableRow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tblVista.setItem(tableRow,3,QtWidgets.QTableWidgetItem(str(row[3])))
           
            tableRow+=1
    # def limpiar_tblVista(self):
    #     # Obtener el número de filas actual en la tabla
    #     num_filas = self.ui.tblVista.rowCount()

    #     # Eliminar todas las filas
    #     for i in range(num_filas):
    #         self.ui.tblVista.removeRow(0)

    def limpiar_tblVista(self):
        try:
         # Resto del código
                 # Limpiar la tabla
            self.ui.tblVista.clearContents()
            self.ui.tblVista.setRowCount(0)
            QApplication.processEvents()
            print("Limpiando la tabla...")
        except Exception as e:
            print(f"Error al limpiar la tabla: {e}")


    def TiempoReal_TBL_VISTA(self):
        self.limpiar_tblVista()
        time.sleep(1)
        # Esta función se ejecutará cada vez que el temporizador alcance su intervalo
        self.MOSTRAR_TBL_CINTA()






if __name__=='__main__':
   app= QtWidgets.QApplication(sys.argv)
   mi_app = MyApp()
   mi_app.show()
   sys.exit(app.exec_())
