'''
Define a class called Dog.  The initializer takes 4 arguments: a breed (such as 'Australian Cattle Dog'), the dog's
name (also a string), an age (integer), and a weight (float).  Set instance variables for each of the arguments. repr
returns a string that prints (remember, repr itself does not print) like this:


----- Rocket -----

  Breed: Australian Cattle Dog

  Age: 8

  Weight: 42.3 lbs.



This is just an example, use the data in the Dog instance, which may not 'Rocket', etc.  Write an instance method called
 dogfight that takes another Dog object as an argument. If one of the dogs is at least 10 years old and the other is
 less than 10, the younger dog wins.  Otherwise, the heavier dog wins. If they have the same weight, return 'Tie'.
 Return the name of the dog that wins.
'''


class Dog:
    def __int__(self, breed, name, age, weight):
        """
        Todo: The initializer takes 4 arguments: a breed (such as 'Australian Cattle Dog'),
         the dog's name (also a string), an age (integer), and a weight (float).  Set instance variables for each of
         the arguments.
         :param breed: string
         :param name: string
         :param age: integer
         :param weight: float
        :return: None
        """

    def __repr__(self):
        """
        Todo: Set instance variables for each of the arguments. __repr__ method returns a string that prints
         (remember, repr itself does not print) like this:

            ----- Rocket -----

              Breed: Australian Cattle Dog

              Age: 8

              Weight: 42.3 lbs.
        :param: None
        :return: String
        """

    def dogfight(self, other):
        """
        Todo: Write an instance method called dogfight that takes another Dog object as an argument. If one of the dogs
         is at least 10 years old and the other is less than 10, the younger dog wins.  Otherwise, the heavier dog wins.
          If they have the same weight, return 'Tie'. Return the name of the dog that wins.
        :param other: Dog Object
        :return: String
        :hint: make sure to clear all the if conditions
        """




def main():
    """Create two dogs, and let them fight to each other"""

if __name__ == '__main__':
    main()