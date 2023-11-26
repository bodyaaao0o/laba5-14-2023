"""Це модуль laba_5.

Цей модуль містить класи та функції, пов'язані з ...
(тут ви можете дати короткий опис вашого модулю та його функціоналу)

"""

from enum import Enum

class Taste(Enum):
    """Class for take Taste """
    SWEET = 1
    SOUR = 2
    NEUTRAL = 3

# pylint: disable=R0903

class Fruit():

    """Клас, що представляє фрукт.

    Attributes:
        name (str): Ім'я фрукту.
        size (str): Розмір фрукту.
        color (str): Колір фрукту.
        taste (Taste): Смак фрукту (екземпляр перерахування Taste).
    """
    def __init__(self, name, size, color, taste):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color}, {self.taste.name})"

class Topping:
    """Class for take toppping."""
    def __init__(self, taste):
        self.taste = taste


class FruitSalad:
    """Class for FruitSalad"""
    def __init__(self):
        self.ingredients = []
        self.topping = None
    def add_fruit(self, fruit):
        """ Take ingrediends """
        self.ingredients.append(fruit)
    def choose_topping(self):
        """Choose the toppings"""
        fruit_tastes = [fruit.taste for fruit in self.ingredients]
        if all(taste == Taste.SWEET for taste in fruit_tastes):
            self.topping = Topping(Taste.SWEET)
        elif all(taste == Taste.SOUR for taste in fruit_tastes):
            self.topping = Topping(Taste.SOUR)
        else:
            self.topping = Topping(Taste.NEUTRAL)
    def mix_ingredients(self):
        """ Mixing ingrediends """
        print("Mixing the fruit salad.")



    def __str__(self):
        ingredients_str = "\n".join(str(fruit) for fruit in self.ingredients)
        if self.topping:
            return f"Fruit Salad with {self.topping.taste} topping:\n{ingredients_str}"
        return f"Fruit Salad:\n{ingredients_str}"

def main():
    """Головна функція програми.

    Створює object фруктів, додає їх до салату, обирає топінг та мішає інгредієнти.
    Виводить результат y консоль.
    """
    apple = Fruit("Apple", "Medium", "Red", Taste.SWEET)
    orange = Fruit("Orange", "Large", "Orange", Taste.SOUR)
    banana = Fruit("Banana", "Medium", "Yellow", Taste.SWEET)

    salad = FruitSalad()
    salad.add_fruit(apple)
    salad.add_fruit(orange)
    salad.add_fruit(banana)

    salad.choose_topping()
    salad.mix_ingredients()

    print(salad)

if __name__ == "__main__":
    main()
