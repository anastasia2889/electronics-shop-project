"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

def test_calculate_total_price():
    item = Item('Apple iPhon', 10000, 3)
    assert item.calculate_total_price() == 30000

def test_apply_discount():
     item = Item('Apple iPhon', 10000, 2)
     item.apply_discount()
     assert item.price == 10000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам


def test_string_to_number():
    # Проверяем, что строка преобразуется в число правильно
    result = Item.string_to_number("5.2")
    assert result == 5