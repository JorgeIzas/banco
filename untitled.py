from PyQt5 import QtCore, QtGui, QtWidgets
from ventana2 import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
import pymysql
import time
from subprocess import Popen

db = pymysql.connect("localhost","root","rootPass.123","banco")
cursor = db.cursor()
accion = 'prueba'

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(217, 320)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #comboBox
        self.cBox = QtWidgets.QComboBox(self.centralwidget)
        self.cBox.setGeometry(QtCore.QRect(10, 10, 161, 23))
        self.cBox.setEditable(False)
        self.cBox.setObjectName("cBox")
        self.cBox.addItem("Lectura no Confirmada")
        self.cBox.addItem("Lectura Confirmada")
        self.cBox.addItem("Lectura Repetible")
        self.cBox.addItem("Serializable")
        #Botonos de consultar
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(70, 60, 80, 23))
        self.btnConsultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnConsultar.clicked.connect(self.nivelAislamiento)
        self.btnConsultar.clicked.connect(self.consulta)
        #boton depositar
        self.btnDeposito = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeposito.setGeometry(QtCore.QRect(70, 100, 80, 23))
        self.btnDeposito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDeposito.setObjectName("btnDeposito")
        self.btnDeposito.clicked.connect(self.nivelAislamiento)
        self.btnDeposito.clicked.connect(self.deposito)
        #boton retirar
        self.btnRetiro = QtWidgets.QPushButton(self.centralwidget)
        self.btnRetiro.setGeometry(QtCore.QRect(70, 140, 80, 23))
        self.btnRetiro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRetiro.setObjectName("btnRetiro")
        self.btnRetiro.clicked.connect(self.nivelAislamiento)
        self.btnRetiro.clicked.connect(self.retiro)
        #boton cajero
        self.btnCajero = QtWidgets.QPushButton(self.centralwidget)
        self.btnCajero.setGeometry(QtCore.QRect(70, 180, 80, 23))
        self.btnCajero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCajero.setObjectName("btnCajero")
        self.btnCajero.clicked.connect(self.nivelAislamiento)
        self.btnCajero.clicked.connect(self.cajero)

        #boton export
        self.btnExport = QtWidgets.QPushButton(self.centralwidget)
        self.btnExport.setGeometry(QtCore.QRect(10, 230, 80, 23))
        self.btnExport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExport.setObjectName("btnExport")
        self.btnExport.clicked.connect(self.exportar)
        
        #boton import
        self.btnImport = QtWidgets.QPushButton(self.centralwidget)
        self.btnImport.setGeometry(QtCore.QRect(130, 230, 80, 23))
        self.btnImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImport.setObjectName("btnImport")
        self.btnImport.clicked.connect(self.importar)
        
        #boton cambiar de BD
        self.btnCambiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCambiar.setGeometry(QtCore.QRect(10, 270, 80, 23))
        self.btnCambiar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCambiar.setObjectName("btnCambiar")
        
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Banco"))
        self.btnConsultar.setText(_translate("mainWindow", "Consultar"))
        self.btnDeposito.setText(_translate("mainWindow", "Depósito"))
        self.btnRetiro.setText(_translate("mainWindow", "Retiro"))
        self.btnCajero.setText(_translate("mainWindow", "Cajero"))
        self.btnExport.setText(_translate("mainWindow", "Export"))
        self.btnImport.setText(_translate("mainWindow", "Import"))
        self.btnCambiar.setText(_translate("mainWindow", "Cambiar BD"))
        
    def nivelAislamiento(self):
        var = str(self.cBox.currentText())
        if var == 'Lectura no Confirmada':
            sql = "set @@session.tx_isolation = 'READ-UNCOMMITTED';"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
            f = open("log.txt", "a")
            f.write("   TRANSACCIÓN LECTURA NO COMPROMETIDA INICIALIZADA \n")
            f.write("       " + time.strftime("%c") + "\n")
            f.close
        elif var == 'Lectura Confirmada':
            sql = "set @@session.tx_isolation = 'READ-COMMITTED';"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
            f = open("log.txt", "a")
            f.write("   TRANSACCIÓN LECTURA COMPROMETIDA INICIALIZADA \n")
            f.write("       " + time.strftime("%c") + "\n")
            f.close
        elif var == 'Lectura Repetible':
            sql = "set @@session.tx_isolation = 'REPETABLE-READ';"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
            f = open("log.txt", "a")
            f.write("   TRANSACCIÓN LECTURA REPETIBLE INICIALIZADA \n")
            f.write("       " + time.strftime("%c") + "\n")
            f.close
        elif var == 'Serializable':
            sql = "set @@session.tx_isolation = 'SERIALIZABLE';"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
            f = open("log.txt", "a")
            f.write("   TRANSACCIÓN SERIALIZABLE INICIALIZADA \n")
            f.write("       " + time.strftime("%c") + "\n")
            f.close
    
    def consulta(self):
        global accion
        accion = 'consulta'
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, accion, cursor)
        self.ui
        self.window.show()
    
    def deposito(self):
        global accion
        accion = 'deposito'
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, accion, cursor)
        self.ui
        self.window.show()
    
    def retiro(self):
        global accion
        accion = 'retiro'
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, accion, cursor)
        self.ui
        self.window.show()
    
    def cajero(self):
        global accion
        accion = 'cajero'
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, accion, cursor)
        self.ui
        self.window.show()
        
    def exportar(self):
        Popen('mysqldump --user="root" --password="rootPass.123"  banco > data-dump.sql' ,shell=True)
        print('Exportación Exitosa')
        
    def importar(self):
        Popen('mysql --user="root" --password="rootPass.123" banco < data-dump.sql', shell=True)
        print('Importación Exitosa')
        
        
        
        