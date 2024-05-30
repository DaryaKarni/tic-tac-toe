from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QFrame, QWidget, QMessageBox, QMainWindow
from PyQt6.QtGui import QFont, QPixmap,QPainter, QPen 
from PyQt6.QtCore import Qt

import sys
class GameGrid(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.width = 520
        self.height = 520
        self.canvas = QPixmap(self.width + 30, self.height +30)
        self.canvas.fill(Qt.GlobalColor.darkRed)
        self.painter = QPainter(self.canvas)
        self.pen = QPen(Qt.GlobalColor.black)
        self.pen.setWidth(10)
        self.painter.setPen(self.pen)


        self.painter.drawLine(self.width // 3 + 15, 0, self.width // 3 + 15, self.height + 25)
        self.painter.drawLine(2 *self.width // 3 + 20, 0, 2 * self.width // 3 + 20, self.height + 25)
        self.painter.drawLine(0, self.height // 3 + 15, self.width + 25, self.height // 3 + 15)
        self.painter.drawLine(0, 2 * self.height // 3 + 15, self.width + 25, 2 * self.height // 3 + 15)
        self.setPixmap(self.canvas)
        self.width = 520
        self.height = 520
        self.setFixedSize(self.width + 30, self.height + 30)

        
        self.currentPlayer = "X"
        self.nextGrid = None
        
        self.mainGrid = QGridLayout(self)
        
        self.frames = [[QFrame(self) for _ in range(3)] for _ in range(3)]
        self.buttons = [[QPushButton("") for _ in range(9)] for _ in range(9)]
        self.subGrids = [[None for _ in range(3)] for _ in range(3)]
        self.subGridStatus = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                frame = self.frames[i][j]
                frame.setFixedSize(self.width // 3, self.height // 3)
                subGrid = QGridLayout(frame)
                self.subGridStatus[i][j] = None

                for k in range(3):
                    for l in range(3):
                        index = k * 3 + l
                        button = self.buttons[i * 3 + j][index]
                        button.setFixedSize((self.width // 9) - 5, (self.height // 9) - 5)
                        button.setStyleSheet("font-size: 24px;")
                        subGrid.addWidget(button, k, l)
                        button.clicked.connect(self.makeMove(i, j, k, l))
                        
                self.subGrids[i][j] = subGrid
                self.mainGrid.addWidget(frame, i, j)
        
        self.setLayout(self.mainGrid)
        self.updateButtonStyles()
        self.show()

    def makeMove(self, i, j, k, l):
        def move():
            if self.nextGrid and (i, j) != self.nextGrid and self.subGridStatus[self.nextGrid[0]][self.nextGrid[1]] is None:
                return  

            button = self.buttons[i * 3 + j][k * 3 + l]

            if button.text() == "" and self.subGridStatus[i][j] is None:
                button.setText(self.currentPlayer)
                if self.checkWin(i, j):
                    self.subGridStatus[i][j] = self.currentPlayer
                    self.markSubgridWin(i, j)
                    if self.checkWinOverall():
                         self.showWinner(self.currentPlayer)
                         return
                elif self.checkDraw(i, j):
                    self.subGridStatus[i][j] = 'D'
                    self.markSubgridDraw(i, j)
                
                self.currentPlayer = "O" if self.currentPlayer == "X" else "X"
                self.nextGrid = (k, l)

                if self.subGridStatus[k][l] is not None:
                    self.nextGrid = None
                
                if self.checkDrawOverall():
                    self.showDraw()
                    return
                
                self.updateButtonStyles()
                
        return move

    def checkWin(self, i, j):
        buttons = self.buttons[i * 3 + j]
        lines = [
            [buttons[0], buttons[1], buttons[2]],  
            [buttons[3], buttons[4], buttons[5]],  
            [buttons[6], buttons[7], buttons[8]],  
            [buttons[0], buttons[3], buttons[6]],  
            [buttons[1], buttons[4], buttons[7]],  
            [buttons[2], buttons[5], buttons[8]],  
            [buttons[0], buttons[4], buttons[8]],  
            [buttons[2], buttons[4], buttons[6]]   
        ]
        for line in lines:
            if all(button.text() == self.currentPlayer for button in line):
                return True
        return False

    def checkDraw(self, i, j):
        buttons = self.buttons[i * 3 + j]
        return all(button.text() != "" for button in buttons)

    def checkWinOverall(self):
        lines = [
            [self.subGridStatus[i][j] for i in range(3)] for j in range(3)  
        ] + [
            [self.subGridStatus[i][j] for j in range(3)] for i in range(3)  
        ] + [
            [self.subGridStatus[i][i] for i in range(3)],  
            [self.subGridStatus[i][2 - i] for i in range(3)],  
        ]

        for line in lines:
            if all(status == self.currentPlayer for status in line):
                return True
        return False

    def checkDrawOverall(self):
        for row in self.subGridStatus:
            for status in row:
                if status is None:
                    return False
        return True

    def showWinner(self, winner):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Game Over")
        msgBox.setText(f"Player {winner} wins the global board!")
        msgBox.exec()
        self.resetGame()

    def showDraw(self):
        x_wins = sum(row.count("X") for row in self.subGridStatus)
        o_wins = sum(row.count("O") for row in self.subGridStatus)
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Game Over")
        
        if x_wins > o_wins:
            msgBox.setText("Player X wins!")
        elif o_wins > x_wins:
            msgBox.setText("Player O wins!")
        else:
            msgBox.setText("It's a draw!")
        
        msgBox.exec()
        self.resetGame()

    def resetGame(self):
        self.currentPlayer = "X"
        self.nextGrid = None
        self.clear_labels() 
        for i in range(9):
            for button in self.buttons[i]:
                button.setText("")
                button.setStyleSheet("font-size: 24px;")
                button.setEnabled(True)
        self.subGridStatus = [[None for _ in range(3)] for _ in range(3)]
        self.updateButtonStyles()

    def updateButtonStyles(self):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        button = self.buttons[i * 3 + j][k * 3 + l]
                        if self.subGridStatus[i][j] is not None:
                            button.setStyleSheet("font-size: 24px; background-color: lightgray;")
                            button.setEnabled(False)
                        elif self.nextGrid is None or (i, j) == self.nextGrid:
                            if button.text() == "":
                                button.setStyleSheet("font-size: 24px; background-color: pink;")
                                button.setEnabled(True)
                            else:
                                button.setStyleSheet("font-size: 24px;")
                                button.setEnabled(False)
                        else:
                            button.setStyleSheet("font-size: 24px;")
                            button.setEnabled(False)

    
    def markSubgridWin(self, i, j):
        for k in range(3):
            for l in range(3):
                button = self.buttons[i * 3 + j][k * 3 + l]
                button.setText(self.currentPlayer)
                button.setStyleSheet("font-size: 24px; background-color: lightgray;")
                button.setEnabled(False)

    def markSubgridDraw(self, i, j):
        for k in range(3):
            for l in range(3):
                button = self.buttons[i * 3 + j][k * 3 + l]
                button.setStyleSheet("font-size: 24px; background-color: lightgray;")
                button.setEnabled(False)

    def clear_labels(self):
        for i in range(3):
            for j in range(3):
                frame = self.frames[i][j]
                for child in frame.children():
                    if isinstance(child, QLabel):
                        frame.layout().removeWidget(child)
                        child.deleteLater()




