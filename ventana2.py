import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, accion):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 214)

        #botones aceptar y cancelar
        self.btnBox = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBox.setGeometry(QtCore.QRect(210, 180, 167, 24))
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBox.setObjectName("btnBox")
        
        #comboBox de las cuentras creadas
        self.cBox2 = QtWidgets.QComboBox(Dialog)
        self.cBox2.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.cBox2.setObjectName("cBox2")
        """ Cambiar datos de la cuenta """
        listaCuentas = []
        db = pymysql.connect("localhost","root","rootPass.123","banco")
        cursor = db.cursor()
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
        self.label_2.setGeometry(QtCore.QRect(130, 130, 57, 15))
        self.label_2.setObjectName("label_2")
        
        #text area para ingresar el monto
        self.txtMonto = QtWidgets.QTextEdit(Dialog)
        self.txtMonto.setGeometry(QtCore.QRect(190, 120, 191, 31))
        self.txtMonto.setObjectName("txtMonto")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        """ Quitar elementos extra """
        if accion == 'consulta':
            self.txtMonto.setVisible(False)
            self.label_2.setVisible(False)
    
    """Comprobaciones de operaciones"""

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Banco"))
        self.label.setText(_translate("Dialog", "Saldo: "))
        self.label_2.setText(_translate("Dialog", "Monto:"))

    def changeAccount(self, value):
        primera = value.split(',')
        segunda = primera[0].split("'")
        print('Cambio', segunda[1])
        db = pymysql.connect("localhost","root","rootPass.123","banco")
        cursor = db.cursor()
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