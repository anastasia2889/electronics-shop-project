"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_calculate_total_price():
    item = Item('Apple iPhon', 10000, 3)
    assert item.calculate_total_price() == 30000

def test_apply_discount():
     item = Item('Apple iPhon', 10000, 2)
     item.apply_discount()
     assert item.price == 10000