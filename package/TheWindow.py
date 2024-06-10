from menu.TheMenu import TheMenu
from picture.Pic import Image
from gameGrid.GameGrid_copy import GameGrid
from jsonDic import GameSaveManager
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt 
import os


class TheWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setGeometry(200,100,1000,600)
       
        self.menuBar = TheMenu(self)
        self.setMenuBar(self.menuBar)
        self.menuBar.addLoadMenuActionHandler(self.load_game)
        self.menuBar.addSaveMenuActionHandler(self.save_game)
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
        
        self.default_file_path = os.path.join(os.getcwd(), "game_save.json")

    def save_game(self):
        GameSaveManager.save_game(self.gameGrid, self.default_file_path)

    def load_game(self):
        if os.path.exists(self.default_file_path):
            GameSaveManager.load_game(self.gameGrid, self.default_file_path)
        else:
            print("No saved game file found.")

       
        
        
        
       
        
       

   