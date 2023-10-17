from src.phone import Phone, Item

def test_number_of_sim():
    """Тестируем кол-во sim-карт"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add_method():
    """Тестируем метод add"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 11", 80_000, 3, 1)
    item1 = Item("Fridge", 25000, 4)
    item2 = Item("Microwave", 15000, 2)
    assert item1 + item2 == 6
    assert item1 + phone1 == 9
    assert phone1 + phone2 == 8