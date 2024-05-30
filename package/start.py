from TheWindow import TheWindow

from PyQt6.QtWidgets import QApplication

import sys

app = QApplication(sys.argv)
wnd = TheWindow()
wnd.show()

sys.exit(app.exec())