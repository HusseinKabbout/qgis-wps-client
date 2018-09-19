# -*- coding: utf-8 -*-
"""
***************************************************************************
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
  ***************************************************************************
"""
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.core import *
from . import version
from .Ui_qgsedithttpconnectionbase import Ui_QgsEditHttpConnectionBase
from urllib.parse import urlparse


class QgsEditHttpConnectionBaseGui(QDialog,
                                  QObject, Ui_QgsEditHttpConnectionBase):
    MSG_BOX_TITLE = "WPS"

    def __init__(self, parent, fl, old_name):
        QDialog.__init__(self, parent, fl)
        self.old_name = old_name
        self.parent = parent
        self.flags = fl
        self.setupUi(self)
        self.setWindowTitle('QGIS WPS-Client ' + version())
        self.buttonBox.button(QDialogButtonBox.Apply).setText("Ok")
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(
            self.buttonBox_accepted)

    def buttonBox_accepted(self):
        settings = QSettings()
        myURL = urlparse(self.txtUrl.text())
        mySettings = "/WPS/" + self.txtName.text()
        settings.beginGroup(mySettings)
        dpl_name_list = settings.allKeys()
        settings.endGroup()
        if self.txtName.text() is "":
            QMessageBox.information(self,
                                    self.tr("Name Error"),
                                    self.tr("Connection name is missing."))
        elif self.txtUrl.text() is "":
            QMessageBox.information(self,
                                    self.tr("Url Error"),
                                    self.tr("Connection url is missing."))
        else:
            if self.old_name != self.txtName.text():
                settings.remove("/WPS/" + self.old_name)
                if len(dpl_name_list) > 1:
                    QMessageBox.information(self,
                                            self.tr("Name Error"),
                                            self.tr("Connection name is already"
                                                    " used.\nPlease provide"
                                                    " another name."))
                    self.txtName.selectAll()
                    return
            settings.setValue(mySettings + "/scheme", myURL.scheme)
            settings.setValue(mySettings + "/server", myURL.netloc)
            settings.setValue(mySettings + "/path", myURL.path)
            settings.setValue(mySettings + "/method", "GET")
            settings.setValue(mySettings + "/version", "1.0.0")
            settings.setValue(mySettings + "/url", self.txtUrl.text())

            self.parent.initQgsWpsGui()
            self.close()
