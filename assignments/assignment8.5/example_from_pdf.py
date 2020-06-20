# -*- coding:utf-8 -*-
# @Description: example from pdf: class and RegEx
# @Author: Shimin
# @Copyright
# @Version:0.0.1

class Car:
    """ After defining a class, you need to define the initializer, __init__.(init method)"""

    def __init__(self, name, make, year, mileage, color=None):
        """  In the initializer we can define and initialize instance variables. Instance variables are
         variables that are defined in a class. They will always have the prefix of self."""

        self.color = None
        self.name = name
        self.price = input("How much did it cost? ")
        self.make = make
        self.yr = year
        self.miles = mileage
        if color == None:
            self.set_color()

    def set_color(self):
        while True:
            info = input("Do you know the EXACT color (Y/N)? ")
            if info.upper() == "Y":

                self.color = input("What color is your car? ")
                break

            elif info.upper() == "N":
                print("Too bad :(")
                self.color = None
                break

            else:

                print("I don't understand try again.")
                break
    def get_mileage(self):

        return self.miles

    """The __repr__ method (short for representation) is a method that tells python how
to represent your class as a string.
The repr method only has self as a parameter. Calling the print function on a class
object will implicitly call repr.
repr should always return a string."""

    def __repr__(self):
        result = "\n"

        result += "NAME:".ljust(7) + self.name + "\n"
        result += "MAKE:".ljust(7) + self.make + "\n"
        result += "YEAR:".ljust(7) + str(self.yr) + "\n"
        result += "MILES:".ljust(7) + str(self.miles) + "\n"
        if self.color != None:
            result += "COLOR:".ljust(7) + str(self.color) + "\n"
        return result

    """Methods are invoked using the dot operator. When the method
is invoked, object.method(), the argument corresponding to
self is the object."""


def main():
    mustang = Car("Mustang GT", "Ford", 2014, 41000)
    print(mustang)  # Same as print(mustang.__repr__())
    if mustang.color == None:
        mustang.set_color()
    print(mustang)


if __name__ == "__main__":
    main()
