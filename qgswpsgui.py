# -*- coding: utf-8 -*-
"""
 /***************************************************************************
   QGIS Web Processing Service Plugin
  -------------------------------------------------------------------
 Date                 : 09 November 2009
 Copyright            : (C) 2009 by Dr. Horst Duester
 email                : horst dot duester at kappasys dot ch

  ***************************************************************************
  *                                                                         *
  *   This program is free software; you can redistribute it and/or modify  *
  *   it under the terms of the GNU General Public License as published by  *
  *   the Free Software Foundation; either version 2 of the License, or     *
  *   (at your option) any later version.                                   *
  *                                                                         *
  ***************************************************************************/
"""
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtNetwork import *
from qgis.core import *
from . import version
from .wpslib.wpsserver import WpsServer
from .Ui_qgswpsgui import Ui_QgsWps
from .qgswpsbookmarks import Bookmarks
from .doAbout import DlgAbout


class QgsWpsGui(QDialog, QObject, Ui_QgsWps):
    MSG_BOX_TITLE = "WPS"
    getDescription = pyqtSignal(str, QTreeWidgetItem)
    newServer = pyqtSignal()
    editServer = pyqtSignal(str)
    deleteServer = pyqtSignal(str)
    connectServer = pyqtSignal(list)
    pushDefaultWPSServer = pyqtSignal(str)
    requestDescribeProcess = pyqtSignal(str, str)

    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.fl = fl
        self.setWindowTitle('QGIS WPS-Client ' + version())
        self.dlgAbout = DlgAbout(parent)
        self.filterText = ''
        self.lneFilter.setText('')

        self.buttonBox.rejected.connect(self.buttonBox_rejected)
        self.buttonBox.accepted.connect(self.buttonBox_accepted)
        self.btnConnect.clicked.connect(self.btnConnect_clicked)
        self.btnBookmarks.clicked.connect(self.btnBookmarks_clicked)
        self.btnNew.clicked.connect(self.btnNew_clicked)
        self.btnEdit.clicked.connect(self.btnEdit_clicked)
        self.cmbConnections.activated.connect(self.cmbConnections_activated)
        self.btnDelete.clicked.connect(self.btnDelete_clicked)
        self.btnAbout.clicked.connect(self.btnAbout_clicked)
        self.treeWidget.itemDoubleClicked.connect(
            self.treeWidget_itemDoubleClicked)
        self.lneFilter.textChanged.connect(self.lneFilter_textChanged)

        self.btnDelete.setEnabled(False)

    def initQgsWpsGui(self):
        self.btnConnect.setEnabled(False)
        settings = QSettings()
        settings.beginGroup("WPS")
        connections = settings.childGroups()
        self.cmbConnections.clear()
        self.cmbConnections.addItems(list(set(connections)))
        self.treeWidget.clear()

        if self.cmbConnections.count() > 0:
            self.btnConnect.setEnabled(True)
            self.btnEdit.setEnabled(True)
            self.btnDelete.setEnabled(True)

        try:
            settings = QSettings()
            myIndex = pyint(settings.value("WPS-lastConnection/Index",
                                           "Index"))
            self.cmbConnections.setCurrentIndex(myIndex)
        except:
            pass

        return 1

    def getBookmark(self, item):
        self.requestDescribeProcess.emit(item.text(0), item.text(1))

    def buttonBox_rejected(self):
        self.close()

    # see http://www.riverbankcomputing.com/Docs/PyQt4/pyqt4ref.html#connecting-signals-and-slots
    # without this magic, the on_btnOk_clicked will be called two times: one clicked() and one clicked(bool checked)

    def buttonBox_accepted(self):
        if self.treeWidget.topLevelItemCount() == 0:
            QMessageBox.warning(None, 'WPS Warning', 'No Service connected!')
        else:
            try:
                self.getDescription.emit(self.cmbConnections.currentText(),
                                         self.treeWidget.currentItem())
            except:
                QMessageBox.information(None, self.tr('Error'), self.tr(
                    'Please select a process!'))

    # see http://www.riverbankcomputing.com/Docs/PyQt4/pyqt4ref.html#connecting-signals-and-slots
    # without this magic, the on_btnOk_clicked will be called two times: one clicked() and one clicked(bool checked)

    def btnConnect_clicked(self):
        self.treeWidget.clear()
        self.filterText = ''
        self.lneFilter.setText('')
        selectedWPS = self.cmbConnections.currentText()
        self.server = WpsServer.getServer(selectedWPS)
        self.server.capabilitiesRequestFinished.connect(
            self.createCapabilitiesGUI)
        self.server.requestCapabilities()

    def btnBookmarks_clicked(self):
        self.dlgBookmarks = Bookmarks(self.fl)
        self.dlgBookmarks.getBookmarkDescription.connect(self.getBookmark)
        #      self.dlgBookmarks.bookmarksChanged.connect(bookmarksChanged())
        self.dlgBookmarks.show()

    def btnNew_clicked(self):
        self.newServer.emit()
        if self.cmbConnections.currentText():
            self.btnDelete.setEnabled(True)

    def btnEdit_clicked(self):
        self.editServer.emit(self.cmbConnections.currentText())

    def cmbConnections_activated(self, index):
        settings = QSettings()
        settings.setValue("WPS-lastConnection/Index", index)
        self.btnDelete.setEnabled(True)

    def btnDelete_clicked(self):
        res = QMessageBox.question(
            self, self.tr("Delete server"),
            self.tr("Are you sure you want to delete {0}?".format(
                self.cmbConnections.currentText())))
        if res == QMessageBox.No:
            return
        self.deleteServer.emit(self.cmbConnections.currentText())
        if not self.cmbConnections.currentText():
            self.btnDelete.setEnabled(False)

    def initTreeWPSServices(self, taglist):
        self.treeWidget.clear()
        self.treeWidget.setColumnCount(self.treeWidget.columnCount())
        itemList = []

        for items in taglist:
            if self.filterText == '':
                item = QTreeWidgetItem()
                ident = items[0]
                title = items[1]
                abstract = items[2]
                item.setText(0, ident.strip())
                item.setText(1, title.strip())
                item.setText(2, abstract.strip())
                itemList.append(item)
            else:
                if self.filterText in items[0] or self.filterText in items[1] or self.filterText in items[2]:
                    item = QTreeWidgetItem()
                    ident = items[0]
                    title = items[1]
                    abstract = items[2]
                    item.setText(0, ident.strip())
                    item.setText(1, title.strip())
                    item.setText(2, abstract.strip())
                    itemList.append(item)

        self.treeWidget.addTopLevelItems(itemList)

    def btnAbout_clicked(self):
        self.dlgAbout.show()

    def treeWidget_itemDoubleClicked(self, item, column):
        self.getDescription.emit(self.cmbConnections.currentText(),
                                 self.treeWidget.currentItem())

    def createCapabilitiesGUI(self):
        self.treeWidget.clear()
        self.itemListAll = self.server.parseCapabilitiesXML()
        self.initTreeWPSServices(self.itemListAll)

    def lneFilter_textChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.filterText = p0
        self.initTreeWPSServices(self.itemListAll)
