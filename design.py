# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 441)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.dsb_incident_light = QtWidgets.QDoubleSpinBox(Form)
        self.dsb_incident_light.setMaximumSize(QtCore.QSize(70, 20))
        self.dsb_incident_light.setMinimum(0.0)
        self.dsb_incident_light.setMaximum(360.0)
        self.dsb_incident_light.setProperty("value", 0.0)
        self.dsb_incident_light.setObjectName("dsb_incident_light")
        self.gridLayout.addWidget(self.dsb_incident_light, 0, 1, 1, 1)
        self.grid = QtWidgets.QGridLayout()
        self.grid.setObjectName("grid")
        self.gridLayout.addLayout(self.grid, 2, 0, 5, 4)
        self.cbCornea = QtWidgets.QCheckBox(Form)
        self.cbCornea.setEnabled(True)
        self.cbCornea.setText("")
        self.cbCornea.setChecked(True)
        self.cbCornea.setObjectName("cbCornea")
        self.gridLayout.addWidget(self.cbCornea, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.dsb_cornea_retardance = QtWidgets.QDoubleSpinBox(Form)
        self.dsb_cornea_retardance.setMaximumSize(QtCore.QSize(70, 20))
        self.dsb_cornea_retardance.setMinimum(0.0)
        self.dsb_cornea_retardance.setMaximum(0.35)
        self.dsb_cornea_retardance.setSingleStep(0.01)
        self.dsb_cornea_retardance.setProperty("value", 0.05)
        self.dsb_cornea_retardance.setObjectName("dsb_cornea_retardance")
        self.gridLayout.addWidget(self.dsb_cornea_retardance, 7, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(90, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.cbMacula = QtWidgets.QCheckBox(Form)
        self.cbMacula.setText("")
        self.cbMacula.setChecked(True)
        self.cbMacula.setObjectName("cbMacula")
        self.gridLayout.addWidget(self.cbMacula, 8, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Model: Birefringence of Human Eye"))
        self.label.setText(_translate("Form", "Cornea\'s retardance"))
        self.label_4.setText(_translate("Form", "Incident light azimuth"))
        self.label_3.setText(_translate("Form", "Macula"))

