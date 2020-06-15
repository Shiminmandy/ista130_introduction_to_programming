# -*- coding:utf-8 -*-
# @Description: python assignment7
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import csv
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

"""
1.引入csv
2.打开指定文件夹with open ... as
3.循环文件内每一行
    3.2 append()每一行第一个内容到names
    3.3 加入每一行第二个内容到body
    3.4 加入每一行第三个内容到brain
    #3.5 关上文件
"""
def populate_lists(names, body_weights, brain_weights):

    #csv_file = open('BrainBodyWeightKilos.csv', 'r')
    with open('BrainBodyWeightKilos.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        for line in readCSV:
            names.append(line[0].title())
            body_weights.append(line[1])
            brain_weights.append(line[2])
    #print(csv_file)
    """
    for line in csv_file:
        splited = line[0:-1].split(',')
        print(splited)
        names.append(splited[0].title())
        body_weights.append(splited[1])
        brain_weights.append(splited[2])

    csv_file.close()"""
    #return names, body_weights, brain_weights we do not return list




# def write_converted_csv(filename, lst_names, lst_body, lst_brain):


def main():
    find_insert_position('apple', ['banana', 'orange'])
    populate_lists([],[],[])
if __name__ == '__main__':
    main()

