from menu.TheMenu import TheMenu
from picture.Pic import Image
from gameGrid.GameGrid_copy import GameGrid
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt 

class TheWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setGeometry(200,100,1000,600)
       # self.createCentalWidget()
        self.menuBar = TheMenu(self)
        #self.menuBar.addLoadMenuActionHandler(self.setLoadText)
        #self.menuBar.addSaveMenuActionHandler(self.setSaveText)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(50,0,50,0)
        self.leftImage = Image()
        self.layout.addWidget(self.leftImage)

        self.gameGrid = GameGrid()
        self.layout.addStretch()
        self.layout.addWidget(self.gameGrid, Qt.AlignmentFlag.AlignCenter)

        self.rightImage = Image()
        self.rightImage.playerButton.setText("Player O")
        self.layout.addStretch()
        self.layout.addWidget(self.rightImage)

        self.central_widget.setLayout(self.layout)

        
        #self.layout2.setContentsMargins(50,0,50,0)
       
        
        
        
       
        
       

   
