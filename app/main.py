from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from pages.auth_page import AuthPage

app = QApplication([])

app.setWindowIcon(QIcon("app/res/imgs/master_pol.ico"))
start_page = AuthPage()
start_page.show()

app.exec()
