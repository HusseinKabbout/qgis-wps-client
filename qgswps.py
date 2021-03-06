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
# Import the PyQt and the QGIS libraries
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.core import *
from .QgsWpsDockWidget import QgsWpsDockWidget
from .doAbout import DlgAbout
from . import resources_rc


DEBUG = False

# Our main class for the plugin


class QgsWps:
    MSG_BOX_TITLE = "WPS Client"

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.localePath = ""

        # Initialise the translation environment
        userPluginPath = QFileInfo(
            QgsApplication.qgisUserDatabaseFilePath()).path() + "/python/plugins/wps"
        systemPluginPath = QgsApplication.prefixPath() + "/share/qgis/python/plugins/wps"
        myLocale = QSettings().value("locale/userLocale")[0:2]
        if QFileInfo(userPluginPath).exists():
            self.pluginPath = userPluginPath
            self.localePath = userPluginPath + "/i18n/wps_" + myLocale + ".qm"
        elif QFileInfo(systemPluginPath).exists():
            self.pluginPath = systemPluginPath
            self.localePath = systemPluginPath + "/i18n/wps_" + myLocale + ".qm"

        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):

        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/wps/images/wps-add.png"), "WPS-Client",
            self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.actionAbout = QAction("About", self.iface.mainWindow())
        self.actionAbout.triggered.connect(self.doAbout)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)

        if hasattr(self.iface, "addPluginToWebMenu"):
            self.iface.addPluginToWebMenu("WPS-Client", self.action)
            self.iface.addPluginToWebMenu("WPS-Client", self.actionAbout)
        else:
            self.iface.addPluginToMenu("WPS", self.action)
            self.iface.addPluginToWebMenu("WPS", self.action)

        self.myDockWidget = QgsWpsDockWidget(self.iface)
        self.myDockWidget.setWindowTitle('WPS')
        self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.myDockWidget)
        self.myDockWidget.show()

    def unload(self):
        if hasattr(self.iface, "addPluginToWebMenu"):
            self.iface.removePluginWebMenu("WPS-Client", self.action)
            self.iface.removePluginWebMenu("WPS-Client", self.actionAbout)
        else:
            self.iface.removePluginToMenu("WPS", self.action)
            self.iface.removePluginToMenu("WPS", self.actionAbout)

        self.iface.removeToolBarIcon(self.action)

        if self.myDockWidget:
            self.myDockWidget.close()

        self.myDockWidget = None

    def run(self):
        if self.myDockWidget.isVisible():
            self.myDockWidget.hide()
        else:
            self.myDockWidget.show()

    def doAbout(self):
        self.dlgAbout = DlgAbout()
        self.dlgAbout.show()
