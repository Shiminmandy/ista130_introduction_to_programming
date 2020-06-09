# -*- coding:utf-8 -*-
# @Description: python second assignment
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import math


def print_word(int, str):
    for i in range(int):
        print(f"{i + 1} --> {str}")


def bacteria(num_mints, num_bacteria):
    for j in range(num_bacteria):
        print(f"after {(j + 1) * num_mints} minutes:  {2 ** (j + 1)} bacteria")


def convert_to_copper(num_gold_coins, num_silver_coins, num_copper_coins):
    converted_cp = num_gold_coins * 50 + num_silver_coins * 5 + num_copper_coins
    print(
        f"{num_gold_coins} gp, {num_silver_coins} sp, {num_copper_coins} cp converted to copper is: {converted_cp} cp")


def convert_from_copper(num_cp):
    num_gp = num_cp // 50
    num_sp = num_cp % 50 // 5
    rest_cp = num_cp - num_gp * 50 - num_sp * 5
    print(f"{num_cp} copper pieces is: {num_gp} gp, {num_sp} sp, {rest_cp} cp")


def repeat_word(a_string, num_rows, num_col):
    i = 0
    while i < num_rows:
        print(a_string * num_col)
        i += 1


def text_triangle(int6):
    for i in range(int6):
        print('x' * (i + 1))


def surface_area_of_cylinder(radius, height):
    SA = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
    print(f"The surface area of a cylinder with radius {radius} and height {height} is {SA}")


def tree_height(distance, length):
    Height = math.sqrt(length ** 2 - distance ** 2)
    print(f"Kite string: {length}")
    print(f"Distance: {distance}")
    print(f"Height: {Height}")


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
    repeat_word('Goblin', 3, 5)
    repeat_word('Kobold', 5, 3)
    text_triangle(3)
    text_triangle(10)
    text_triangle(0)
    surface_area_of_cylinder(10.0, 10.0)
    surface_area_of_cylinder(0.0, 1.0)
    tree_height(300, 500)
    tree_height(100, 141.421356)



if __name__ == '__main__':
    main()
