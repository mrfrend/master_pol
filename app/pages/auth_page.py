from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QFormLayout,
    QPushButton,
    QMessageBox,
    QLineEdit,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from res.colors import ACCENT_COLOR, SECONDARY_COLOR, ACCENT_COLOR_HOVER
from res.fonts import MAIN_FONT
from database.db import db


class AuthPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.init_ui()
        self.set_styles()

    def setup_window(self):
        self.setWindowTitle("Авторизация")
        self.setFixedSize(400, 250)

    def init_ui(self):
        self.main_layout = QVBoxLayout()
        self.form_layout: QFormLayout = QFormLayout()

        self.title = QLabel("Авторизация")
        self.title.setObjectName("title")

        self.username_label = QLabel("Логин:")
        self.password_label = QLabel("Пароль:")

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Войти")

        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)
        self.form_layout.addRow(self.login_button)

        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.main_layout.addStretch()
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addStretch()

        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        if db and db.authorize_user(username, password):
            from pages.partners_page import PartnersPage

            self.partners_page = PartnersPage()
            self.partners_page.show()
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль.")

    def set_styles(self):
        self.setStyleSheet(
            """QLabel { font-size: 16px; font-family: %(MAIN_FONT)s} 
                #title {
                    font-size: 24px; 
                    font-weight: bold; 
                    color: %(ACCENT_COLOR)s;
                    }
                QPushButton { 
                    background-color: %(ACCENT_COLOR)s;
                    border: 1px solid black;
                    color: %(SECONDARY_COLOR)s;
                    font-weight: bold;
                    padding: 5px;
                }
                QPushButton:hover { 
                    background-color: %(ACCENT_COLOR_HOVER)s;
                }
            """
            % {
                "ACCENT_COLOR": ACCENT_COLOR,
                "SECONDARY_COLOR": SECONDARY_COLOR,
                "MAIN_FONT": MAIN_FONT,
                "ACCENT_COLOR_HOVER": ACCENT_COLOR_HOVER,
            }
        )
