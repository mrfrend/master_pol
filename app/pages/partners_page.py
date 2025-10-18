from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QVBoxLayout
from PyQt6.QtCore import Qt
from database.db import db
from components.partner_card import PartnerCard, PartnersInfo
from res.colors import ACCENT_COLOR


class PartnersPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.init_ui()
        self.load_partners()

    def setup_window(self):
        self.setWindowTitle("Партнеры")
        self.resize(800, 600)

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Заголовок
        title = QLabel("Партнеры")
        title.setObjectName("title")
        title.setStyleSheet(
            f"""
            #title {{
                font-size: 24px;
                font-weight: bold;
                color: {ACCENT_COLOR};
                margin-bottom: 20px;
            }}
        """
        )
        main_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Создаем область прокрутки
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.partners_layout = QVBoxLayout(scroll_content)
        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

    def handle_partner_double_click(self, partner_info: PartnersInfo):
        from components.edit_partner_dialog import EditPartnerDialog

        dialog = EditPartnerDialog(partner_info, self)
        dialog.exec()

    def load_partners(self):
        # Получаем данные о партнерах из БД
        if db:
            partners_data = db.execute_select("SELECT * FROM show_partners")
            for partner in partners_data:
                # Получаем скидку для партнера
                discount = db.get_disc(partner["partner_name"])

                # Создаем объект с информацией о партнере
                partner_info = PartnersInfo(
                    id=partner["id"],
                    type_name=partner["type_name"],
                    partner_name=partner["partner_name"],
                    first_name_director=partner["first_name_director"],
                    last_name_director=partner["last_name_director"],
                    middle_name_director=partner["middle_name_director"],
                    phone_partner=partner["phone_partner"],
                    rating=partner["rating"],
                    discount=discount,
                )

                # Создаем и добавляем карточку партнера
                partner_card = PartnerCard(partner_info)
                partner_card.doubleClicked.connect(self.handle_partner_double_click)
                self.partners_layout.addWidget(partner_card)

        self.partners_layout.addStretch()
