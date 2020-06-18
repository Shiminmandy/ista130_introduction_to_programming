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
        #print(splited)
        filtered = list(filter(lambda x: x != "", splited))
        #print(filter(lambda x: x != "", splited))
        print(filtered)
        #the_name = fishmap[filtered[1]]
        #print(the_name)

def main():
    fish_dict_from_file('fishcatch.dat')
if __name__ == '__main__':
    main()