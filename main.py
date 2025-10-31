import sys
import pymysql as pms
from pymysql import cursors
from AuthMain import Ui_MainWindow
from Database import Database
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())

