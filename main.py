import sys
from ui_py.AuthMain import AuthWindow
from PyQt6.QtWidgets import QApplication
from ui_py.PartnerCard import *


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=AuthWindow()
    window.show()
    sys.exit(app.exec())

