from interface.material_calculate import Ui_Form
from PyQt6.QtWidgets import QWidget, QMessageBox
from database.Database import db
from utils.materials import calculate_materials


class MaterialWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data()
        self.calculate_button.clicked.connect(self.handle_calculate_click)
        self.back_button.clicked.connect(self.handle_back)

    def handle_back(self):
        from .section_choose import SectionChoose

        self.SectionChoose = SectionChoose()
        self.SectionChoose.show()
        self.close()

    def load_data(self):
        products_types = db.get_products_types()
        materials_types = db.get_materials_types()

        for p in products_types:
            self.product_type_combobox.addItem(
                p["name"], {"id": p["id"], "coefficent": p["coefficent"]}
            )

        for m in materials_types:
            self.material_type_combobox.addItem(
                m["name"], {"id": m["id"], "defect_percent": m["defect_percent"]}
            )

    def handle_calculate_click(self):
        product_type_id = self.product_type_combobox.currentData()["id"]
        material_type_id = self.material_type_combobox.currentData()["id"]
        width = self.width_spinbox.value()
        height = self.height_spinbox.value()
        amount: int = self.spinBox.value()

        result = calculate_materials(
            product_type_id, material_type_id, width, height, amount
        )

        if result == -1:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        message = f"Для производства {amount} продукций типа {self.product_type_combobox.currentText()} требуется {result} материала {self.material_type_combobox.currentText()}"
        QMessageBox.information(self, "Количество материала", message)
