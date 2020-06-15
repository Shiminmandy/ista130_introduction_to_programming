# -*- coding:utf-8 -*-
# @Description: python assignment7
# @Author: Shimin
# @Copyright
# @Version:0.0.1
"""
1. 如果列表为空，
    1.1 返还0
2. 如果列表不包含动物名
    2.1把名字加入列表list.insert()
    2.2将列表中的名字按顺序排列list.sort()
    2.3list.index()找到动物名位置，储存于变量中
    2.4list.pop(index)去掉加入的动物名
    2.5列表只返还加入动物名的位置
3. 如果列表包含动物名
    3.1直接返回动物名的位置

"""

def find_insert_position(name, string_order):
    if string_order == []:

        return 0
    elif name not in string_order:
        string_order.insert(0, name)
        string_order.sort()
        location = string_order.index(name)
        string_order.pop(location)
        return location

    elif name in string_order:
        return string_order.index(name)
def main():
    find_insert_position('apple', ['banana', 'orange'])
if __name__ == '__main__':
    main()

