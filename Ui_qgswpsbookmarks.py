# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qgswpsbookmarks.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bookmarks(object):
    def setupUi(self, Bookmarks):
        Bookmarks.setObjectName("Bookmarks")
        Bookmarks.resize(753, 422)
        self.gridLayout = QtWidgets.QGridLayout(Bookmarks)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Bookmarks)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(250)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnRemove = QtWidgets.QPushButton(Bookmarks)
        self.btnRemove.setObjectName("btnRemove")
        self.horizontalLayout_3.addWidget(self.btnRemove)
        self.btnClose = QtWidgets.QPushButton(Bookmarks)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose)
        self.btnOK = QtWidgets.QPushButton(Bookmarks)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_3.addWidget(self.btnOK)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(Bookmarks)
        QtCore.QMetaObject.connectSlotsByName(Bookmarks)

    def retranslateUi(self, Bookmarks):
        _translate = QtCore.QCoreApplication.translate
        Bookmarks.setWindowTitle(_translate("Bookmarks", "WPS-Bookmarks"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("Bookmarks", "Service"))
        self.treeWidget.headerItem().setText(1, _translate("Bookmarks", "Identifier"))
        self.treeWidget.headerItem().setText(2, _translate("Bookmarks", "URL"))
        self.btnRemove.setText(_translate("Bookmarks", "Remove"))
        self.btnClose.setText(_translate("Bookmarks", "Close"))
        self.btnOK.setText(_translate("Bookmarks", "Run"))

