# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kenriquez/Documentos/Pruebas/ExportarCsv/exportlayers/exportLayers_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportLayersDialogBase(object):
    def setupUi(self, ExportLayersDialogBase):
        ExportLayersDialogBase.setObjectName("ExportLayersDialogBase")
        ExportLayersDialogBase.resize(400, 203)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExportLayersDialogBase)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(ExportLayersDialogBase)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(ExportLayersDialogBase)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(ExportLayersDialogBase)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(ExportLayersDialogBase)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ExportLayersDialogBase)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(ExportLayersDialogBase)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.button_box = QtWidgets.QDialogButtonBox(ExportLayersDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(ExportLayersDialogBase)
        self.button_box.accepted.connect(ExportLayersDialogBase.accept)
        self.button_box.rejected.connect(ExportLayersDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportLayersDialogBase)

    def retranslateUi(self, ExportLayersDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ExportLayersDialogBase.setWindowTitle(_translate("ExportLayersDialogBase", "ExportLayers"))
        self.pushButton.setText(_translate("ExportLayersDialogBase", "Exportar"))
        self.label.setText(_translate("ExportLayersDialogBase", "Selecciona la capa que quieres exportar y da click en \'Exportar\'"))
