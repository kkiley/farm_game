"""
__author__ = 'Kor'
"""
import random


class Animal:
    """
    Represents characteristics (attributes) of all animals:
    weight
    days_growing
    growth_rate
    food_need
    water_need
    status
    type
    name
        and methods:
    needs
    report
    update_status
    grow
    """

    def __init__(self, growth_rate, food_need, water_need):
        """
        :param growth_rate:
        :param food_need:
        :param water_need:
        :return:
        """

        self._growth = 0
        self._days_growing = 0
        self._weight = 0
        self._name = ''
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Embryo"
        self._type = "Generic"

    def needs(self):
        """
        :return: a dictionary containing food and water needs
        """
        return {'food need': self._food_need, 'water need': self._water_need}

    def report(self):
        """
        :return:a dictionary containing the type, status, growth and days
        growing
        """
        return {'type': self._type, 'status': self._status,
                'growth': self._growth, 'days growing': self._days_growing,
                'weight': self._weight}

    def _update_status(self):
        """
        :return: Update status of the animal depending on the amount of growth
        """
        if self._growth > 1440:
            self._status = "Old"
        elif self._growth >= 730:
            self._status = "2 year old"
        elif self._growth >= 360:
            self._status = "Yearling"
        elif self._growth >= 180:
            self._status = "6 Month Old"
        elif self._growth > 0:
            self._status = "Newborn"

    def grow(self, food, water):
        """
        :param food:
        :param water:
        Updates parameters showing growth which dpends on the amount of food
        and water given to the animal
        """
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
            self._weight += 1
        # increment days growing
        self._days_growing += 1
        # update status
        self._update_status()


def auto_grow(animal, days):
    """
    raise the animal
    :param animal:
    :param days:
    :return:
    """

    for day in range(days):
        food = random.randint(1, 10)
        water = random.randint(1, 10)
        animal.grow(food, water)


def manual_grow(animal):
    """
    get the food and water values from the user
    :param animal:
    :return:
    """
    valid = False
    while not valid:
        try:
            food = int(input("Enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered is invalid...enter a value between "
                      "1 and 10")
        except ValueError:
            print("Value entered is invalid...enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is invalid. Enter a value between"
                      "1 and 10")
        except ValueError:
            print("Value entered is invalid...enter a value between 1 and 10")

    # raise the animal
    animal.grow(food, water)


def display_menu():
    """
    display manage crop menu
    :return:
    """
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select option from the above menu")


def get_menu_choice():
    """
    :return: choice
    """

    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Enter a valid option")
        except ValueError:
            print("Enter a valid option")
    return choice


def manage_animal(animal):
    """
    :param animal:
    :return:
    """
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal, 360)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program!")


def main():
    """
    work with an animal
    :return:
    """
    new_animal = Animal(1, 5, 5)
    manage_animal(new_animal)


main()