from PyQt5 import QtCore, QtGui, QtWidgets
from ventana2 import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow

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
        #Botonos de consultar
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(70, 60, 80, 23))
        self.btnConsultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnConsultar.clicked.connect(self.abrirVentana2)
        #boton depositar
        self.btnDeposito = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeposito.setGeometry(QtCore.QRect(70, 100, 80, 23))
        self.btnDeposito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDeposito.setObjectName("btnDeposito")
        self.btnDeposito.clicked.connect(self.abrirVentana2)
        #boton retirar
        self.btnRetiro = QtWidgets.QPushButton(self.centralwidget)
        self.btnRetiro.setGeometry(QtCore.QRect(70, 140, 80, 23))
        self.btnRetiro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRetiro.setObjectName("btnRetiro")
        self.btnRetiro.clicked.connect(self.abrirVentana2)
        #boton cajero
        self.btnCajero = QtWidgets.QPushButton(self.centralwidget)
        self.btnCajero.setGeometry(QtCore.QRect(70, 180, 80, 23))
        self.btnCajero.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCajero.setObjectName("btnCajero")
        self.btnCajero.clicked.connect(self.abrirVentana2)
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

    def abrirVentana2(self):
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui
        self.window.show()