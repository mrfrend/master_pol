from dataclasses import dataclass
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtCore import Qt, pyqtSignal
from res.colors import ACCENT_COLOR, SECONDARY_COLOR
from res.fonts import MAIN_FONT
from dto.partners_dto import PartnersInfo




class PartnerCard(QFrame):
    doubleClicked = pyqtSignal(PartnersInfo)

    def __init__(self, info: PartnersInfo):
        super().__init__()
        self.info = info

        self.init_ui()
        self.set_styles()

    def mouseDoubleClickEvent(self, a0):
        self.doubleClicked.emit(self.info)
        return super().mouseDoubleClickEvent(a0)

    def init_ui(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Верхняя строка: Тип | Наименование и скидка
        header_layout = QHBoxLayout()
        header_text = QLabel(f"{self.info.type_name} | {self.info.partner_name}")
        header_text.setObjectName("partnerHeader")
        discount_text = QLabel(f"{self.info.discount}%")
        discount_text.setObjectName("partnerDiscount")

        header_layout.addWidget(header_text)
        header_layout.addWidget(discount_text, alignment=Qt.AlignmentFlag.AlignRight)

        # Информация о директоре
        director_text = QLabel(f"Директор")
        director_text.setObjectName("fieldLabel")
        director_name = QLabel(
            f"{self.info.last_name_director} {self.info.first_name_director} {self.info.middle_name_director}"
        )

        # Контактная информация
        phone_text = QLabel(f"+{self.info.phone_partner}")

        # Рейтинг
        rating_layout = QHBoxLayout()
        rating_label = QLabel("Рейтинг:")
        rating_label.setObjectName("fieldLabel")
        rating_value = QLabel(str(self.info.rating))
        rating_layout.addWidget(rating_label)
        rating_layout.addWidget(rating_value)
        rating_layout.addStretch()

        # Добавляем все элементы в главный layout
        main_layout.addLayout(header_layout)
        main_layout.addWidget(director_text)
        main_layout.addWidget(director_name)
        main_layout.addWidget(phone_text)
        main_layout.addLayout(rating_layout)

    def set_styles(self):
        self.setStyleSheet(
            """
            PartnerCard {
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 10px;
                margin: 5px;
                background-color: white;
            }
            QLabel {
                font-family: %s;
            }
            #partnerHeader {
                font-size: 18px;
                font-weight: bold;
                color: %s;
            }
            #partnerDiscount {
                font-size: 18px;
                font-weight: bold;
                color: %s;
            }
            #fieldLabel {
                color: gray;
                font-size: 14px;
            }
        """
            % (MAIN_FONT, ACCENT_COLOR, SECONDARY_COLOR)
        )
