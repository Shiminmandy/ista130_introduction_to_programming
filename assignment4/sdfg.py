# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1

# print ('"{}"'.format("s"))
# while True:
#     a = input("Roll again, zaggy? (Y/N):")
#     if a == "y" or a == "Y":
#         break
#     elif a == "n" or a == "N":
#
#         break
#
#     else:
#
#         print("I don't understand:"+' "{}". Please enter either "{}" or "{}".'.format(a, "Y", "N"))
#
import random
print(f"---------- Ziggy's turn ----------")
points = 0
number = random.randint(1, 6)
print(f"\t<<< ziggy rolls a {number} >>>")
def roll_again(name):
    '''
    roll_again that has a single string parameter to hold a player's name.
    :param name: string
    :return: boolean
    '''
    while True:
        wanna_roll_again = input(f"Roll again, {name}? (Y/N) ")
        if wanna_roll_again.upper() == "Y":
            return True
        elif wanna_roll_again.upper() == "N":
            return False
        else:
            print(f"I don't understand: \"{wanna_roll_again}\". Please enter either \"Y\" or \"N\".")

def play_turn(name):
    '''
    play_turn that has a single string parameter , which holds a player’s name
    :param name: string
    :return: boolean
    '''
    print(f"---------- {name}'s turn ----------")
    score = 0
    while True:
        roll = random.randint(1, 7)
        print(f"\t<<< {name} rolls a {roll} >>>")
        if roll == 1:
            print(f"\t!!! PIG! No points earned, sorry {name} !!!\n")
            score = 0
            input("(enter to continue)")
            return score
        elif roll > 1:
            score += roll
            print(f"\tPoints: {score}")
            if not roll_again(name):
                return score


def main():
    play_turn('ziggy')
if __name__ == '__main__':
    main()