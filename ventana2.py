import pymysql
import time
from PyQt5 import QtCore, QtGui, QtWidgets

cursor = None
cuenta = ''
dinero = ''
NoCuenta = ''

class Ui_Dialog(object):
    def setupUi(self, Dialog, accion, c):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 214)
        global cursor
        cursor = c
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
        
        #boton rollbakc
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(10, 180, 80, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnCancelar.clicked.connect(self.rollback)
        
        #boton solo para realizar la operacion
        self.btnRealizar = QtWidgets.QPushButton(Dialog)
        self.btnRealizar.setGeometry(QtCore.QRect(270, 130, 80, 23))
        self.btnRealizar.setObjectName("btnRealizar")
        
        #boton para realizar commit
        self.btnAceptar = QtWidgets.QPushButton(Dialog)
        self.btnAceptar.setGeometry(QtCore.QRect(100, 180, 80, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnAceptar.clicked.connect(self.commit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        """ Quitar elementos extra """
        global dinero
        if accion == 'consulta':
            self.txtMonto.setVisible(False)
            self.label_2.setVisible(False)
            self.btnRealizar.setVisible(False)
        elif accion == 'deposito':
            dinero = self.txtMonto.toPlainText()
            self.btnRealizar.clicked.connect(self.aumentar)
        elif accion == 'retiro':
            dinero = self.txtMonto.toPlainText()
            self.btnRealizar.clicked.connect(self.disminuir)
        elif accion == 'cajero':
            dinero = self.txtMonto.toPlainText()
            self.btnRealizar.clicked.connect(self.disminuir)
                     
    
    """Comprobaciones de operaciones"""

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
        sql = "SELECT id FROM cuenta WHERE cuenta = '" + segunda[1] + "'"
        cursor.execute(sql)
        data = cursor.fetchone()
        self.NoCuenta = data[0]
        prim = str(data).split('(')
        seg = prim[1].split(',')
        global cuenta
        cuenta = seg[0]
        statement1 = 'SELECT cuenta FROM cuenta where id = ' + seg[0]
        cursor.execute(statement1)
        data = cursor.fetchone()
        self.txtCuenta.setText(data[0])
        statement1 = 'SELECT saldo FROM cuenta where id = ' + seg[0]
        cursor.execute(statement1)
        data = cursor.fetchone()
        self.txtSaldo.setText(str(data[0]))
        
    def aumentar(self):
        global dinero
        dinero = self.txtMonto.toPlainText()
        self.txtSaldo.setText('')
        self.txtMonto.setText('')
        sql = 'update cuenta set saldo = (saldo + ' + str(dinero) + ')  where id = ' + str(self.NoCuenta) +';'
        cursor.execute(sql)
        cursor.fetchone
        sql = "select saldo from cuenta where id = '" + str(self.NoCuenta) + "';"
        cursor.execute(sql)
        data = cursor.fetchone()
        self.txtSaldo.setText(str(data[0]))
        f = open("log.txt", "a")
        f.write("       TRANSACCIÓN PARCILAMENTE COMPROMETIDA \n")
        f.write("           " + time.strftime("%c") + "\n")
        f.close
        
    def disminuir(self):
        global dinero
        dinero = self.txtMonto.toPlainText()
        self.txtSaldo.setText('')
        self.txtMonto.setText('')
        sql = 'update cuenta set saldo = (saldo - ' + str(dinero) + ')  where id = ' + str(self.NoCuenta) +';'
        cursor.execute(sql)
        cursor.fetchone()
        sql = "select saldo from cuenta where id = '" + str(self.NoCuenta) + "';"
        cursor.execute(sql)
        data = cursor.fetchone()
        self.txtSaldo.setText(str(data[0]))
        f = open("log.txt", "a")
        f.write("       TRANSACCIÓN PARCILAMENTE COMPROMETIDA \n")
        f.write("           " + time.strftime("%c") + "\n")
        f.close
        
    def commit(self):
        sql = "commit;"
        cursor.execute(sql)
        print('Transacción ejecutada correctamente')
        f = open("log.txt", "a")
        f.write("       TRANSACCIÓN COMPROMETIDA \n")
        f.write("           " + time.strftime("%c") + "\n")
        f.close
        
    def rollback(self):
        sql = "rollback;"
        cursor.execute(sql)
        print('Transacción cancelada')
        f = open("log.txt", "a")
        f.write("       TRANSACCIÓN ABORTADA \n")
        f.write("           " + time.strftime("%c") + "\n")
        f.close