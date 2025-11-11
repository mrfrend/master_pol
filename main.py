import sys
from windows.AuthMain import AuthWindow
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec())
