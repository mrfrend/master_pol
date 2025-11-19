from interface.section_choose import Ui_Form
from PyQt6.QtWidgets import QWidget


class SectionChoose(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_slots()

    def connect_slots(self):
        self.partners_button.clicked.connect(self.handle_partners)
        self.materials_button.clicked.connect(self.handle_materials)

    def handle_partners(self):
        from .Partners import Partners

        self.Partners = Partners()
        self.Partners.show()
        self.close()

    def handle_materials(self):
        pass
