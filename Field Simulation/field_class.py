__author__ = 'Kor'

from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *


class Field:
    """Simulate a field that can contain animals and crops"""

    # constructor
    def __init__(self, max_animals, max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self):
        """
        :return: True or False
        """


def main():
    new_field = Field(5, 2)
    new_field._crops
    print(new_field._crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)


if __name__ == "__main__":
    main()