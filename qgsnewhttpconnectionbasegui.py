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
from wps import version
from Ui_qgsnewhttpconnectionbase import Ui_QgsNewHttpConnectionBase
from urlparse import urlparse


class QgsNewHttpConnectionBaseGui(QDialog,
                                  QObject, Ui_QgsNewHttpConnectionBase):
    MSG_BOX_TITLE = "WPS"

    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.parent = parent
        self.flags = fl
        self.setupUi(self)
        self.setWindowTitle('QGIS WPS-Client ' + version())

    @pyqtSignature("on_buttonBox_accepted()")
    def on_buttonBox_accepted(self):
        settings = QSettings()
        myURL = urlparse(str(self.txtUrl.text()))
        mySettings = "/WPS/" + self.txtName.text()
        #    settings.setValue("WPS/connections/selected", QVariant(name) )
        settings.setValue(mySettings + "/scheme", myURL.scheme)
        settings.setValue(mySettings + "/server", myURL.netloc)
        settings.setValue(mySettings + "/path", myURL.path)
        settings.setValue(mySettings + "/method", "GET")
        settings.setValue(mySettings + "/version", "1.0.0")
        settings.setValue(mySettings + "/url",
                          self.txtUrl.text()).rstrip().lstrip()

        self.parent.initQgsWpsGui()
