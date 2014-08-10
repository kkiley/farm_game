"""
__author__ = 'Kor'
"""

from animal_class import *


class Sheep(Animal):
    """
    Subclass of Animal
    """

    def __init__(self):
        # call the parent class constructor with default values for sheep.
        # growth rate = 2; food = 4, water = 4
        super().__init__(2, 4, 4)
        self._name = 'Baby Lamb'
        self._type = 'Sheep'

    def grow(self, food, water):
        # Modify the grow algorithm to reflect the growth of a sheep
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
            self._weight += 1
        # increment days growing
        self._days_growing += 1
        # update status
        self._update_status()



