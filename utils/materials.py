# Метод должен принимать идентификатор типа продукции,
# идентификатор типа материала, количество получаемой продукции – целые
# числа, параметры продукции (два параметра) – вещественные, положительные
# числа, а возвращать целое число – количество необходимого материала с
# учетом возможного брака материала.

from database.Database import db
from decimal import Decimal


def calculate_materials(
    product_type_id: int,
    material_type_id: int,
    width: float,
    height: float,
    amount: int,
):
    if width <= 0 or height <= 0 or amount <= 0:
        return -1

    product_type = db.get_product_type(product_type_id)
    if product_type is None:
        return -1

    material_type = db.get_material_type(material_type_id)
    if material_type is None:
        return -1

    product_coeff: float = product_type["coefficent"]
    material_defect_percent: float = material_type["defect_percent"]
    width = Decimal(width)
    height = Decimal(height)
    product_consumption = product_coeff * width * height
    products_consumption = product_consumption * amount * (1 + material_defect_percent)
    return round(products_consumption)
