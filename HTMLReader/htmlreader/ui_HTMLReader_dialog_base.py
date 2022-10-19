# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kenriquez/Documentos/Pruebas/HTMLReader/htmlreader/HTMLReader_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HTMLReaderDialogBase(object):
    def setupUi(self, HTMLReaderDialogBase):
        HTMLReaderDialogBase.setObjectName("HTMLReaderDialogBase")
        HTMLReaderDialogBase.resize(620, 227)
        self.gridLayout = QtWidgets.QGridLayout(HTMLReaderDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(HTMLReaderDialogBase)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(HTMLReaderDialogBase)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 2, 1)
        self.pushButton = QtWidgets.QPushButton(HTMLReaderDialogBase)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.webView = QtWebKitWidgets.QWebView(HTMLReaderDialogBase)
        self.webView.setUrl(QtCore.QUrl("www.google.com"))
        self.webView.setObjectName("webView")
        self.gridLayout.addWidget(self.webView, 2, 0, 1, 2)
        self.button_box = QtWidgets.QDialogButtonBox(HTMLReaderDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 3, 0, 1, 2)

        self.retranslateUi(HTMLReaderDialogBase)
        self.button_box.accepted.connect(HTMLReaderDialogBase.accept)
        self.button_box.rejected.connect(HTMLReaderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(HTMLReaderDialogBase)

    def retranslateUi(self, HTMLReaderDialogBase):
        _translate = QtCore.QCoreApplication.translate
        HTMLReaderDialogBase.setWindowTitle(_translate("HTMLReaderDialogBase", "HTML Reader"))
        self.pushButton_2.setText(_translate("HTMLReaderDialogBase", "Siguiente"))
        self.pushButton_3.setText(_translate("HTMLReaderDialogBase", "Abrir 360"))
        self.pushButton.setText(_translate("HTMLReaderDialogBase", "Anterior"))
from PyQt5 import QtWebKitWidgets
