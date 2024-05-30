from PyQt6.QtWidgets import QMenuBar, QMenu, QWidget
from PyQt6.QtGui import QAction

class TheMenu (QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setMinimumSize(10000,1)

        #self.fileMenu = QMenu("File")
        self.stateMenu = QMenu("State")
        self.editMenu = QMenu("Edit")
        
        
        #self.addMenu(self.fileMenu)
        self.addMenu(self.stateMenu)
        self.addMenu(self.editMenu)
        
        self.loadMenuAction = QAction("Load")
        self.stateMenu.addAction(self.loadMenuAction)
        self.saveMenuAction = QAction("Save")
        self.stateMenu.addAction(self.saveMenuAction)

        self.loadColorsAction = QAction("Load colors")
        self.editMenu.addAction(self.loadColorsAction)
        self.editSaveAction = QAction("Save")
        self.editMenu.addAction(self.editSaveAction)
    
    def addLoadMenuActionHandler(self, handler):
        self.loadMenuAction.triggered.connect(handler)

    def addSaveMenuActionHandler(self, handler):
        self.saveMenuAction.triggered.connect(handler)


