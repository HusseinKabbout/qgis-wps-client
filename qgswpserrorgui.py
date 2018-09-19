# -*- coding: utf-8 -*-

"""
Module implementing ErrorGUI.
"""

from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtWidgets import *

from .Ui_qgswpserrorgui import Ui_Dialog


class ErrorGUI(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        QMessageBox.information(None, '', 'Hallo')
        self.buttonBox.rejected.connect(self.buttonBox_rejected)

    def buttonBox_rejected(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
