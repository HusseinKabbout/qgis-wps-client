# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QgsWpsDockWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QgsWpsDockWidget(object):
    def setupUi(self, QgsWpsDockWidget):
        QgsWpsDockWidget.setObjectName("QgsWpsDockWidget")
        QgsWpsDockWidget.resize(285, 190)
        QgsWpsDockWidget.setMinimumSize(QtCore.QSize(285, 190))
        QgsWpsDockWidget.setMaximumSize(QtCore.QSize(524287, 190))
        QgsWpsDockWidget.setBaseSize(QtCore.QSize(0, 0))
        QgsWpsDockWidget.setFloating(False)
        QgsWpsDockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        QgsWpsDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusLabel = QtWidgets.QLabel(self.groupBox)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.btnConnect = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnConnect.setObjectName("btnConnect")
        self.gridLayout.addWidget(self.btnConnect, 0, 0, 1, 1)
        self.btnKill = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnKill.setEnabled(False)
        self.btnKill.setObjectName("btnKill")
        self.gridLayout.addWidget(self.btnKill, 0, 1, 1, 1)
        QgsWpsDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(QgsWpsDockWidget)
        QtCore.QMetaObject.connectSlotsByName(QgsWpsDockWidget)

    def retranslateUi(self, QgsWpsDockWidget):
        _translate = QtCore.QCoreApplication.translate
        QgsWpsDockWidget.setWindowTitle(_translate("QgsWpsDockWidget", "QGIS WPS-Client"))
        self.btnConnect.setText(_translate("QgsWpsDockWidget", "connect"))
        self.btnKill.setText(_translate("QgsWpsDockWidget", "kill process"))

