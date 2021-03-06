# -*- coding:utf-8 -*-
# @Description: python assignment7
# @Author: Shimin
# @Copyright
# @Version:0.0.1
# import csv
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

    csv_file = open('BrainBodyWeightKilos.csv', 'r')
    for line in csv_file:
        splited = line[0:-1].split(',')
        #print(splited)
        names.append(splited[0].title())
        body_weights.append(float(splited[1]))
        brain_weights.append(float(splited[2]))

    csv_file.close()
    #return names, body_weights, brain_weights we do not return list

    # with open('BrainBodyWeightKilos.csv') as csv_file:
    #     readCSV = csv.reader(csv_file, delimiter=',')
    #     for line in readCSV:
    #         names.append(line[0].title())
    #         body_weights.append(line[1])
    #         brain_weights.append(line[2])
    # #print(csv_file)


"""
1.体重列表中的数据*2.205
2.脑重列表中的数据*0.0022
3.创建并打开新文件
4.因为每个列表的length相同，所以直接循环一个列表
    4.2 write()加入三个列表中同一个index的三个值，改成指定模式
5. 关上文件
"""
def write_converted_csv(filename, lst_names,BodyWeights ,BrainWeights):
    lst_body = []
    for i in BodyWeights:
        lst_body.append(round(i * 2.205, 2))
    lst_brain = []
    for i in BrainWeights:
        lst_brain.append(round(i*0.0022, 2))
    fname = filename
    new_file = open(fname, 'w')
    for i in range(len(lst_names)):
        new_file.write(f"{lst_names[i].title()},")
        new_file.write(f"{lst_body[i]},")
        new_file.write(f"{lst_brain[i]}\n")
    new_file.close()

    # writeCSV = csv.writer(new_file, delimiter=',')
    # writeCSV.writerows(lst_names)
    # writeCSV.writerows(lst_body)
    # writeCSV.writerows(lst_brain)
    # new_file.close()
"""
1.设定三个空列表：动物名，体重，脑重
2.input三个列表到方程populat_lists(),得到三个从文件中提取的新列表
3. 设定answer = 'q'
4. 定while循环，如果answer不为q
    4.1用户输入动物名
    4.2如果输入动物名不在列表中
        4.21打印没有这个名字
        4.22询问是否在三个列表中加入
            4.221如果是则按字母表顺序加入动物名
            4.222第一个函数找到位置
            4.223在同一位置输入体重
            4.224同一位置输入脑重
        4.23如果不是重新输入动物名
    4.3如果动物名在列表中，
        4.31 第一个函数提取动物名的体重和脑重
        4.32打印动物名所在列表的三个值
        4.33询问是否从列表中删除数据
            4.331如果是，则依次删除输入动物名在列表中的数据
5.如果answer==q
    5.1直接将提取出的三个列表写进另一个新的文件夹中
    
"""


def main():
    names = []
    body_weights = []
    brain_weights = []
    populate_lists(names, body_weights, brain_weights)
    # write_converted_csv('whatever.csv', ['apple', 'banana', 'orange'], [10, 20, 30], [1.2, 2.3, 4.5])
    answer = 'q'
    while True:
        answer = input(f'\nEnter animal name (or "q" to quit) : ').title()
        if answer == 'q' or answer == 'Q':
            write_converted_csv('BrainBodyWeightPounds.csv', names, body_weights, brain_weights)
            break
        else:

            if answer not in names:
                print(f'File does not contain "{answer}".')
                ask = input(f'Add "{answer}" to file? (y|n) ')
                if ask == 'y' or ask == 'Y':
                    # names.append(answer)
                    # names.sort()
                    position = find_insert_position(answer, names)
                    names.insert(position, answer)
                    body_weights.insert(position, float(input(f'Enter body weight for "{answer}" in kilograms: ')))
                    brain_weights.insert(position, float(input(f'Enter brain weight for "{answer}" in grams: ')))
            elif answer in names:
                index = find_insert_position(answer, names)
                print(f"{answer}: body = {body_weights[index]}, brain = {brain_weights[index]}")
                del_or_not = input(f'Delete "{answer}"? (y|n) ')
                if del_or_not == 'y' or del_or_not == 'Y':
                    del names[index]
                    del body_weights[index]
                    del brain_weights[index]


if __name__ == '__main__':
    main()

