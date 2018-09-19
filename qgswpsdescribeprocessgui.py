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
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *
from wps import version
from Ui_qgswpsdescribeprocessgui import Ui_QgsWpsDescribeProcessGUI


class QgsWpsDescribeProcessGui(QDialog, QObject, Ui_QgsWpsDescribeProcessGUI):
    MSG_BOX_TITLE = "QGIS WPS Client"

    def __init__(self, parent, fl):
        QDialog.__init__(self, parent, fl)
        self.setupUi(self)
        self.setWindowTitle('QGIS WPS-Client ' + version())
        self.selectedServiceName = parent.cmbConnections.currentText()

    def currentServiceName(self):
        return self.selectedServiceName
