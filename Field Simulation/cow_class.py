"""
This is a test
"""

from animal_class import *


class Cow(Animal):
    """
    This class represents a Cow derived from the animal class. The attributes
    that need to be changed are growth, food_needs and water_needs
    """

    def __init__(self):
        super().__init__(1, 4, 4)
        self._name = 'Bessy'
        self._type = 'Cow'

    # override grow method for subclass
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
            self._weight += 1
        # increment days growing
        self._days_growing += 1
        # update status
        self._update_status()


def main():
    # create a new Cow crop
    Cow_crop = Cow()
    print(Cow_crop.report())
    # manually grow the crop
    manual_grow(Cow_crop)
    print(Cow_crop.report())
    manual_grow(Cow_crop)
    print(Cow_crop.report())


if __name__ == "__main__":
    main()
