from PyQt5 import QtCore, QtGui, QtWidgets
from ventana2 import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow
import pymysql

db = pymysql.connect("localhost","root","rootPass.123","banco")
cursor = db.cursor()
accion = 'prueba'

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(215, 233)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #comboBox
        self.cBox = QtWidgets.QComboBox(self.centralwidget)
        self.cBox.setGeometry(QtCore.QRect(10, 10, 79, 23))
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
        
    def nivelAislamiento(self):
        var = str(self.cBox.currentText())
        if var == 'Lectura no Confirmada':
            sql = "set transaction isolation level READ UNCOMMITTED;"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
        elif var == 'Lectura Confirmada':
            sql = "set transaction isolation level READ COMMITTED;"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
        elif var == 'Lectura Repetible':
            sql = "set transaction isolation level REPEATABLE READ;"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
        elif var == 'Serializable':
            sql = "set transaction isolation level SERIALIZABLE;"
            cursor.execute(sql)
            cursor.fetchone()
            sql = "begin;"
            cursor.execute(sql)
            cursor.fetchone()
            print(var)
    
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