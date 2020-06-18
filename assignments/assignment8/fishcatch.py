# -*- coding:utf-8 -*-
# @Description: python assignment8(1)
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def fish_dict_from_file(filename):
    fishmap = {'1': 'Bream', '2': 'Whitefish', '3': 'Roach', '4': '?',
               '5': 'Smelt', '6': 'Pike', '7': 'Perch'}
    fish_dict = {}
    openfile = open(filename, 'r')
    for line in openfile:
        splited = line.split(" ")
        # print(splited)
        # without_list = filter(lambda x: x != "", splited)
        # print(without_list) # 需要用list接住被过滤的元素
        filtered = list(filter(lambda x: x != "", splited))
        # print(filter(lambda x: x != "", splited))
        # print(filtered)


        the_name = fishmap[filtered[1]] # filtered[1]是key
        #print(the_name)

        if the_name not in fish_dict.keys():
            if filtered[2] != 'NA':
                fish_dict[the_name] = [float(filtered[2])]
        else:
            if filtered[2] != 'NA':
                fish_dict[the_name].append(float(filtered[2]))
    return fish_dict
    #print(fish_dict)



def main():
    fish_dict = fish_dict_from_file('fishcatch.dat')

    first = '#'
    second = 'NAME'
    third = 'MEAN WT'
    print(f"{first.rjust(4)} {second.ljust(10)}{third.rjust(11)}")
    for key, val in sorted(fish_dict.items()):  # sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
        print(f'{str(len(val)).rjust(4)} {str(key).ljust(10)}{str(round(sum(val) / len(val), 1)).rjust(10)}g')




if __name__ == '__main__':
    main()