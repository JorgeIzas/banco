from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Banco"))
        self.label.setText(_translate("Dialog", "Saldo: "))
        self.label_2.setText(_translate("Dialog", "Monto:"))

