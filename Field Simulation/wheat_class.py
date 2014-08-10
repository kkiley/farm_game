__author__ = 'Kor'

from crop_class import *


class Wheat(Crop):
    """
    A Wheat crop
    Child of Crop class
    """
    # constructor
    def __init__(self):
        # call the parent calss constructor with default values for Wheat
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1, 4, 5)
        self._type = "Wheat"

    # override grow method for subclass
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water >= self._water_need:
                self._growth += self._growth_rate * 2
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        # increment day growing
        self._days_growing += 1
        # update the status
        self._update_status()


def main():
    # create a new wheat crop
    wheat_crop = Wheat()
    print(wheat_crop.report())
    # manually grow the crop
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())


if __name__ == "__main__":
    main()