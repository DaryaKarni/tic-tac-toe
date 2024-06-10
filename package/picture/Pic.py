from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QMainWindow, QPushButton, QGridLayout, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize

import sys


class Image(QWidget):
    def __init__(self):
        super().__init__()
        

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,100,0,0)

        self.picture = QLabel()
        self.picture.setFixedSize(200,200)
       
        self.loadButton = QPushButton("Load Image")
        self.loadButton.setFixedSize(100,25)
        
        self.playerButton = QPushButton()
        self.playerButton.setContentsMargins(150, 200, 150, 0)
        self.playerButton.setFixedSize(100,25)
        self.playerButton.setText("Player Х")

        self.lineEdit = QLineEdit()
        self.lineEdit.setFixedWidth(100)
        self.layout.addWidget(self.playerButton, alignment = Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit.hide()
        self.layout.addWidget(self.lineEdit, alignment = Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.picture,0, alignment = Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.loadButton, 0, alignment = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
    
        self.setLayout(self.layout)
        self.LoadButtonClicked(self.ShowImage)
        self.PlayerButtonClicked(self.EditPlayer)
        self.LineEditReturn(self.RenameButton)
       
        self.setGeometry(200,100,1000,500)
        self.setWindowTitle("PyQT show image")
        self.show()

    def ShowImage(self):
        self.file = QFileDialog()
        self.fileName = self.file.getOpenFileName()[0]
        self.pixmap = QPixmap(self.fileName)
        picWidth = self.picture.width()
        picHeight = self.picture.height()

        self.pixmap = self.pixmap.scaled(picWidth, picHeight, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.picture.setPixmap(self.pixmap)
    
    def LoadButtonClicked(self, handler):
        self.loadButton.clicked.connect(handler)
    
    def PlayerButtonClicked(self, handler):
        self.playerButton.clicked.connect(handler)
    
    def LineEditReturn(self, handler):
        self.lineEdit.returnPressed.connect(handler)
    
    def EditPlayer(self):
        self.playerButton.hide()
        self.lineEdit.setText(self.playerButton.text())
        self.lineEdit.show()
        self.lineEdit.setFocus()

    def RenameButton(self):
        self.playerButton.setText(self.lineEdit.text())
        self.lineEdit.hide()
        self.playerButton.show()
     
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Image()
    sys.exit(app.exec())

    

    
       
