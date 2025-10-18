from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QComboBox,
    QSpinBox,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from res.colors import ACCENT_COLOR
from database.db import db
from dto.partners_dto import PartnerUpdateDto, PartnersInfo


class EditPartnerDialog(QDialog):
    def __init__(self, partner_data: PartnersInfo, parent=None):
        super().__init__(parent)
        self.partner_data = partner_data
        self.setup_ui()
        self.load_partner_types()
        self.fill_form()
        self.result = None

    def setup_ui(self):
        self.setWindowTitle("Редактирование партнера")
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Создаем поля формы
        self.partner_type = QComboBox()
        self.partner_name = QLineEdit()
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.middle_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.address = QLineEdit()
        self.inn = QLineEdit()
        self.rating = QSpinBox()
        self.rating.setRange(0, 10)

        # Добавляем поля в форму
        form_layout.addRow("Тип партнера:", self.partner_type)
        form_layout.addRow("Название:", self.partner_name)
        form_layout.addRow("Имя директора:", self.first_name)
        form_layout.addRow("Фамилия директора:", self.last_name)
        form_layout.addRow("Отчество директора:", self.middle_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Телефон:", self.phone)
        form_layout.addRow("Адрес:", self.address)
        form_layout.addRow("ИНН:", self.inn)
        form_layout.addRow("Рейтинг:", self.rating)

        # Кнопки
        self.save_button = QPushButton("Сохранить")
        self.cancel_button = QPushButton("Отмена")

        self.save_button.clicked.connect(self.save_changes)
        self.cancel_button.clicked.connect(self.reject)

        layout.addLayout(form_layout)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

        # Стили
        self.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                padding: 8px;
                border-radius: 4px;
            }}
        """
        )

    def load_partner_types(self):
        if db:
            partner_types = db.get_partner_types()
            for pt in partner_types:
                self.partner_type.addItem(pt["name"], pt["id"])

    def fill_form(self):
        # Устанавливаем индекс типа партнера
        index = self.partner_type.findData(self.partner_data.type_name)
        if index >= 0:
            self.partner_type.setCurrentIndex(index)

        rest_info = db.execute_select(
            "SELECT email_partner, address, INN FROM partners WHERE id = %s",
            (self.partner_data.id,),
        )[0]
        print(rest_info)

        # Заполняем остальные поля
        self.partner_name.setText(self.partner_data.partner_name)
        self.first_name.setText(self.partner_data.first_name_director)
        self.last_name.setText(self.partner_data.last_name_director)
        self.middle_name.setText(self.partner_data.middle_name_director or "")
        self.email.setText(rest_info["email_partner"])
        self.phone.setText(self.partner_data.phone_partner)
        self.address.setText(rest_info["address"])
        self.inn.setText(rest_info["INN"])
        self.rating.setValue(self.partner_data.rating)

    def save_changes(self):
        try:
            partner_data = PartnerUpdateDto(
                id=self.partner_data.id,
                partner_type_id=self.partner_type.currentData(),
                partner_name=self.partner_name.text(),
                first_name=self.first_name.text(),
                last_name=self.last_name.text(),
                middle_name=self.middle_name.text(),
                email=self.email.text(),
                phone=self.phone.text(),
                address=self.address.text(),
                inn=self.inn.text(),
                rating=self.rating.value(),
            )
            db.update_partner(partner_data)
            self.accept()
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось сохранить изменения: {str(e)}"
            )
