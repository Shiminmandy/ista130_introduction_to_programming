# -*- coding:utf-8 -*-
# @Description: python second assignment
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def print_word(int, str):
    for i in range(int):
        print(f"{i + 1} --> {str}")


def main():
    print_word(3, 'banana')
    print_word(4, 'mississippi')


if __name__ == '__main__':
    main()
