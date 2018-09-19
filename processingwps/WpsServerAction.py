from processing.gui.ToolboxAction import ToolboxAction
from WpsAlgorithm import WpsAlgorithm
from qgis.PyQt.QtCore import *


class WpsServerAction(ToolboxAction):

    def __init__(self, server):
        self.server = server
        self.processalgs = []
        self.name = "Load processes from server"
        self.group = WpsAlgorithm.groupName(server)

    def execute(self):
        self.server.requestCapabilities()
        self.server.capabilitiesRequestFinished.connect(
            self._capabilitiesRequestFinished)

    def _capabilitiesRequestFinished(self):
        self.processalgs = []
        self.server.parseCapabilitiesXML()
        for process in self.server.processes:
            self.processalgs.append(WpsAlgorithm(process))
        processing.updateAlgsList()
