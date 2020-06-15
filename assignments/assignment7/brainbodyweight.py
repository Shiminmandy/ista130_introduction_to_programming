# -*- coding:utf-8 -*-
# @Description: python assignment7
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def find_insert_position(name, string_order):
    for i in string_order:
        string_order.insert(i, name)
        print(string_order.index(name))
def main():
    find_insert_position('apple', ['banana', 'orange'])
if __name__ == '__main__':
    main()

