# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qgsnewhttpconnectionbase.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsNewHttpConnectionBase(object):
    def setupUi(self, QgsNewHttpConnectionBase):
        QgsNewHttpConnectionBase.setObjectName("QgsNewHttpConnectionBase")
        QgsNewHttpConnectionBase.resize(569, 160)
        QgsNewHttpConnectionBase.setSizeGripEnabled(True)
        QgsNewHttpConnectionBase.setModal(True)
        self.gridlayout = QtWidgets.QGridLayout(QgsNewHttpConnectionBase)
        self.gridlayout.setContentsMargins(11, 11, 11, 11)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.GroupBox1 = QtWidgets.QGroupBox(QgsNewHttpConnectionBase)
        self.GroupBox1.setObjectName("GroupBox1")
        self.gridlayout1 = QtWidgets.QGridLayout(self.GroupBox1)
        self.gridlayout1.setContentsMargins(11, 11, 11, 11)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.TextLabel1_2 = QtWidgets.QLabel(self.GroupBox1)
        self.TextLabel1_2.setObjectName("TextLabel1_2")
        self.gridlayout1.addWidget(self.TextLabel1_2, 0, 0, 1, 1)
        self.txtName = QtWidgets.QLineEdit(self.GroupBox1)
        self.txtName.setMinimumSize(QtCore.QSize(0, 0))
        self.txtName.setFrame(True)
        self.txtName.setObjectName("txtName")
        self.gridlayout1.addWidget(self.txtName, 0, 1, 1, 2)
        self.TextLabel1 = QtWidgets.QLabel(self.GroupBox1)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridlayout1.addWidget(self.TextLabel1, 1, 0, 1, 1)
        self.txtUrl = QtWidgets.QLineEdit(self.GroupBox1)
        self.txtUrl.setObjectName("txtUrl")
        self.gridlayout1.addWidget(self.txtUrl, 1, 1, 1, 2)
        self.gridlayout.addWidget(self.GroupBox1, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QgsNewHttpConnectionBase)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.TextLabel1_2.setBuddy(self.txtName)
        self.TextLabel1.setBuddy(self.txtUrl)

        self.retranslateUi(QgsNewHttpConnectionBase)
        self.buttonBox.accepted.connect(QgsNewHttpConnectionBase.accept)
        self.buttonBox.rejected.connect(QgsNewHttpConnectionBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QgsNewHttpConnectionBase)
        QgsNewHttpConnectionBase.setTabOrder(self.txtName, self.txtUrl)

    def retranslateUi(self, QgsNewHttpConnectionBase):
        _translate = QtCore.QCoreApplication.translate
        QgsNewHttpConnectionBase.setWindowTitle(_translate("QgsNewHttpConnectionBase", "Create a new WPS connection"))
        self.GroupBox1.setTitle(_translate("QgsNewHttpConnectionBase", "Connection details"))
        self.TextLabel1_2.setText(_translate("QgsNewHttpConnectionBase", "&Name"))
        self.txtName.setToolTip(_translate("QgsNewHttpConnectionBase", "Name of the new connection"))
        self.TextLabel1.setText(_translate("QgsNewHttpConnectionBase", "&URL"))
        self.txtUrl.setToolTip(_translate("QgsNewHttpConnectionBase", "HTTP address of the Web Map Server"))

