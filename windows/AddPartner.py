from interface.AddPartner import Ui_MainWindow
from PyQt6 import QtWidgets


class AddPartner(QtWidgets.QMainWindow):
    def __init__(self, partner_info):
        super().__init__()
        self.partner_info = partner_info
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
