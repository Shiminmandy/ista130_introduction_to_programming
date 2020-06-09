# -*- coding:utf-8 -*-
# @Description: python second assignment
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def print_word(int, str):
    for i in range(int):
        print(f"{i + 1} --> {str}")


def bacteria(num_mints, num_bacteria):
    for j in range(num_bacteria):
        print(f"after {(j + 1) * num_mints} minutes:  {2 ** (j + 1)} bacteria")


def convert_to_copper(num_gold_coins, num_silver_coins, num_copper_coins):
    converted_cp = num_gold_coins * 50 + num_silver_coins * 5 + num_copper_coins
    print(f"{num_gold_coins } gp, {num_silver_coins} sp, {num_copper_coins} cp converted to copper is: {converted_cp} cp")


def convert_from_copper(num_cp):
    num_gp = num_cp // 50
    num_sp = num_cp % 50 // 5
    rest_cp = num_cp - num_gp * 50 - num_sp * 5
    print(f"{num_cp} copper pieces is: {num_gp} gp, {num_sp} sp, {rest_cp} cp")





def main():
    print_word(3, 'banana')
    print_word(4, 'mississippi')
    bacteria(10, 5)
    bacteria(21, 3)
    convert_to_copper(5, 10, 7)
    convert_to_copper(15, 23, 12)
    convert_from_copper(200)
    convert_from_copper(1107)
    convert_from_copper(3242)

if __name__ == '__main__':
    main()
