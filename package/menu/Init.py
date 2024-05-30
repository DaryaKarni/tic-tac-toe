from TheMenu import TheMenu

if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
    from PyQt6.QtCore import Qt
    
    import sys

    app = QApplication(sys.argv)
    wnd = QMainWindow()
    wnd.setGeometry(200,200,450,450)

    centralWidget = QLabel("Default Text")
    centralWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
    wnd.setCentralWidget(centralWidget)
    menu = TheMenu(wnd)

    def Click():
      centralWidget.setText("Click")

    menu.addLoadMenuActionHandler(Click)
    menu.addSaveMenuActionHandler(Click)

    wnd.show()

    sys.exit(app.exec())

