import csv
import os.path
from builtins import str


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):
        cls.all = []
        dir_ = os.path.dirname(__file__)
        file_path = os.path.join(dir_, file_name)
        with open(file_path, encoding="cp1251") as file:
            content = csv.DictReader(file)
            for dict_ in content:
                name = dict_['name']
                price = cls.string_to_number(dict_['price'])
                quantity = cls.string_to_number(dict_['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string_num):
        return int(float(string_num))


