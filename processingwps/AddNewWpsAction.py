from processing.gui.ToolboxAction import ToolboxAction
from processing.core.Processing import Processing
import os
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *


class AddNewWpsAction(ToolboxAction):

    def __init__(self, wpsDockWidget):
        self.name = "Connect to WPS servers"
        self.group = "Tools"
        self.wpsDockWidget = wpsDockWidget
        self.wpsDockWidget.bookmarksChanged.connect(Processing.updateAlgsList)

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + "/../images/script.png")

    def execute(self):
        self.wpsDockWidget.on_btnConnect_clicked()
