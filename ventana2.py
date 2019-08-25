import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
action = ""
global valor
valor = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog, accion, valor1, c):
        Dialog.setObjectName("Dialog")
        global cursor
        cursor = c
        global valor 
        valor = valor1
        print(accion)
        Dialog.resize(400, 214)
        self.conectar()

        if valor1 == 2:
            self.deposito()
        elif valor1 == 3:
            self.retiro()

        #botones aceptar y cancelar
        self.btnBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBox.setGeometry(QtCore.QRect(210, 180, 167, 24))
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBox.setObjectName("btnBox")
        self.btnBox.accepted.connect(self.confirmar)
        self.btnBox.rejected.connect(self.cancelar)
        
        #comboBox de las cuentras creadas
        self.cBox2 = QtWidgets.QComboBox(Dialog)
        self.cBox2.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.cBox2.setObjectName("cBox2")
        """ Cambiar datos de la cuenta """
        listaCuentas = []

        cursor.execute("SELECT cuenta, nombre FROM cuenta")
        data = cursor.fetchall()
        self.cBox2.addItem('----------')
        for row in data:
            listaCuentas.append(row)
            self.cBox2.addItem(str(row))
        self.cBox2.currentTextChanged.connect(self.changeAccount)
        #text area para mostrar el numero de cuenta
        self.txtCuenta = QtWidgets.QTextEdit(Dialog)
        self.txtCuenta.setEnabled(False)
        self.txtCuenta.setGeometry(QtCore.QRect(190, 20, 191, 31))
        self.txtCuenta.setObjectName("txtCuenta")

        #text area para mostrar el saldo
        self.txtSaldo = QtWidgets.QTextEdit(Dialog)
        self.txtSaldo.setEnabled(False)
        self.txtSaldo.setGeometry(QtCore.QRect(190, 70, 191, 31))
        self.txtSaldo.setObjectName("txtSaldo")

        #labels
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 60, 51, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 57, 15))
        self.label_2.setObjectName("label_2")
        
        #text area para ingresar el monto
        self.txtMonto = QtWidgets.QTextEdit(Dialog)
        self.txtMonto.setGeometry(QtCore.QRect(70, 120, 191, 31))
        self.txtMonto.setObjectName("txtMonto")
        """ bandera = self.txtMonto.textChanged.connect(self.comenzar) """

        #boton rollbakc
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(10, 180, 80, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        
        #boton solo para realizar la operacion
        self.btnRealizar = QtWidgets.QPushButton(Dialog)
        self.btnRealizar.setGeometry(QtCore.QRect(270, 130, 80, 23))
        self.btnRealizar.setObjectName("btnRealizar")
        self.btnRealizar.clicked.connect(self.comenzar)
        #boton para realizar commit
        self.btnAceptar = QtWidgets.QPushButton(Dialog)
        self.btnAceptar.setGeometry(QtCore.QRect(100, 180, 80, 23))
        self.btnAceptar.setObjectName("btnAceptar")




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def conectar(self):
        
        conn.autocommit = False

    def comenzar(self):
        
        if valor == 2:
            self.deposito1()
        elif valor == 3:
            self.retiro1()

    def confirmar(self):
        conn.commit()
        conn.close()
        print("conexion terminada")

    def cancelar(self):
        conn.rollback()
        conn.close()
        print("conexion terminada")

    def deposito(self):
        global valor
        valor = 2

    def retiro(self):
        global valor
        valor = 3

    def deposito1(self):
        cursor = conn.cursor() 
        var = self.txtSaldo.toPlainText() 
        var1 = self.txtMonto.toPlainText()
        vart = float(var) + float(var1)
        print(vart)
        id1 = self.txtCuenta.toPlainText()
        upda = "Update cuenta set saldo = " + str(vart) + " where cuenta = " + id1 
        cursor.execute(upda)
        print ("Deposito ")

    def retiro1(self):
        cursor = conn.cursor() 
        var = self.txtSaldo.toPlainText() 
        var1 = self.txtMonto.toPlainText()
        vart = float(var) - float(var1)
        print(vart)
        id1 = self.txtCuenta.toPlainText()
        upda = "Update cuenta set saldo = " + str(vart) + " where cuenta = " + id1 
        cursor.execute(upda)
        print ("Retiro ")    















    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Banco"))
        self.label.setText(_translate("Dialog", "Saldo: "))
        self.label_2.setText(_translate("Dialog", "Monto:"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.btnRealizar.setText(_translate("Dialog", "Realizar"))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar"))

    def changeAccount(self, value):
        primera = value.split(',')
        segunda = primera[0].split("'")
        print('Cambio', segunda[1])
        
        sql = "SELECT id FROM cuenta WHERE cuenta = '" + segunda[1] + "'"
        cursor.execute(sql)
        data = cursor.fetchone()
        prim = str(data).split('(')
        seg = prim[1].split(',')
        statement1 = 'SELECT cuenta FROM cuenta where id = ' + seg[0]
        cursor.execute(statement1)
        data = cursor.fetchone()
        self.txtCuenta.setText(data[0])
        statement1 = 'SELECT saldo FROM cuenta where id = ' + seg[0]
        cursor.execute(statement1)
        data = cursor.fetchone()
        self.txtSaldo.setText(str(data[0]))





