# -*- coding:utf-8 -*-
# @Description:python assignment4
# @Author: Shimin
# @Copyright
# @Version:0.0.
import random
def print_scores(name1, score1, name2, score2):
    print(f"\n--- SCORES\t{name1}: {score1}\t{name2}: {score2} ---")


def check_for_winner(winner_name, winner_score):
    if winner_score >= 50:
        print(f"THE WINNER IS: {winner_name}!!!!!")
        return True
    else:
        return False
"""
    Write a function called roll_again that has a single string parameter to hold a player's
name. In the function:
a) Enter a while loop which repeats the following steps:
• Ask whether the player would like to roll again, using the following message:
Roll again, Ziggy? (Y/N)
Ø There is a single space after (Y/N).
• If the player answers with Y, y, N, or n, exit from the loop.
• Otherwise print the following message (replacing XXX with the user’s entry):
I don't understand: "XXX". Please enter either "Y" or "N".
b) The function returns either True or False depending on whether the player wants to
roll again.
"""

# difficult one
def roll_again(player):
    while True:
        a = input(f"Roll again, {player}? (Y/N) ")
        if a == "y" or a == "Y":
            return True          # we don't need to use break to exit from the loop
        elif a == "n" or a == "N":

            return False

        else:

            print("I don't understand:"+' "{}". Please enter either "{}" or "{}".'.format(a, "Y", "N"))
            # if we want to output "something", we need to written as '"something"'
            # print(f"I don't understand: \"{wanna_roll_again}\". Please enter either \"Y\" or \"N\".")


def play_turn(player_name):
    print(f"---------- {player_name}'s turn ----------")
    points = 0
    while True:
        number = random.randint(1, 6)
        print(f"\t<<< {player_name} rolls a {number} >>>")
        if number == 1:
            print(f"\t!!! PIG! No points earned, sorry {player_name} !!!")
            points = 0
            input("(enter to continue)")

            return points

        elif number > 1:
            points += number
            print(f"\tPoints: {points}")
            if not roll_again(player_name):
                return points


def main():
    seed_value = input("Enter seed value:")
    random.seed(seed_value)
    print(f"\n\nPig Dice")
    name1 = input("Enter name for player 1:")
    name2 = input("Enter name for player 2:")
    print(f"\tHello {name1} and {name2}, welcome to Pig Dice!")

    # check_for_winner('Ziggy', 50)
    # roll_again('ziggy')
    while True:
        print_scores(name1, 0, name2, 0)
        play_turn(name1)
        points = play_turn(name1)
        print_scores(name1, points, name2, 0)
        check_for_winner(name1, points)
        if check_for_winner(name1, points) is True:
            break

        play_turn(name2)
        points2 = play_turn(name2)
        print_scores(name1, points, name2, points2)
        check_for_winner(name2, points2)







if __name__ == '__main__':
    main()