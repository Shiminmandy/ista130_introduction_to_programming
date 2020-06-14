# -*- coding:utf-8 -*-
# @Description: python assignment6
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def print_report(filename):
    readfile = open(filename, 'r')
    vowel_count = 0
    consonants_count =0
    whitespace_count =0
    punctuaton_count = 0
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    whitespace = " \t\n"
    x = ["Vowels:", "Consonants:", "Whitespace:", "Punctuation:", "Total:"]
    y = ["Percent vowels:", "Percent consonants:", "Percent spaces:", "Percent punctuation:"]
    # for line in readfile:
    #     for i in range(len(vowels)):
    #          a = line.count(vowels[i])
    #          vowel_count += a
    # print(vowel_count)
    for line in readfile:
        for i in range(len(line)):
            if line[i] in vowels:
                vowel_count += 1
            elif line[i] in consonants:
                consonants_count += 1
            elif line[i] in whitespace:
                whitespace_count += 1
            else:
                punctuaton_count += 1
    readfile.close()
    print("\n"+filename.center(25, "-"))
    print(f"{x[0].ljust(20)}{str(vowel_count).rjust(5)}")
    print(f"{x[1].ljust(20)}{str(consonants_count).rjust(5)}")
    print(f"{x[2].ljust(20)}{str(whitespace_count).rjust(5)}")
    print(f"{x[3].ljust(20)}{str(punctuaton_count).rjust(5)}")
    print("-" * 25)
    total = vowel_count + consonants_count + whitespace_count + punctuaton_count
    print(f"{x[4].ljust(20)}{str(total).rjust(5)}")
    print(f"\n{y[0].ljust(20)}{str(round(vowel_count/total * 100, 1)).rjust(5)}")
    print(f"{y[1].ljust(20)}{str(round(consonants_count/total * 100, 1)).rjust(5)}")
    print(f"{y[2].ljust(20)}{str(round(whitespace_count/total * 100, 1)).rjust(5)}")
    print(f"{y[3].ljust(20)}{str(round(punctuaton_count/total * 100, 1)).rjust(5)}")
    print("=" * 25)
    # for j in range(len(consonants)):
    #     c = line.count(consonants[j])
    #     consonants_count += c
    # print(consonants_count)
"""

1：count被指定单词出现的次数
2：对次数进行循环
    2.1：用input()让用户输入替换词
    2.2：每进行一次循环就用replace()替换一个单词并进行更新
3.返回更新后指定行

"""

def replace_parts_of_speech(line_from_A_file, replace_part):
    count_word = line_from_A_file.count(replace_part)
    for i in range(count_word):
        user_input = input(f"Enter {replace_part.lower()}: ")
        line_from_A_file = line_from_A_file.replace(replace_part,user_input,1)
    return line_from_A_file
    # no_punctuation = line_from_A_file.replace('.',' ')
    # splited = no_punctuation.split()
    # for i in range(len(splited)):
    #     if replace_part in splited[i]:
    #         splited[i] = input(f"Enter {replace_part.lower()}: ")
    #         join_line = " ".join(splited)
    #         new_line = str(join_line)+'.'
    # return new_line
"""
1. 打开指定文件设定“读”模式
2.改名
3.打开改名后文件设定“写”模式
4.设定一个list，包含需要被替换的类型
5.循环list里面每一个元素
    5.1在循环list时同时循环被打开文件里的每一行
        5.11循环列表里的元素和循环行里面的内容成为replace_parts_of_speech()方程里面的input，将文件里的内容替换成用户指定单词
6.循环结束后原文件内容已改变，再次读取改变后文件的每一行
    6.1用 .write()模式将每一行内容导入被改名后新创建的文件中
7.循环后所有内容传入新文件夹，关上原文件夹
8.关上新文件夹

"""
def complete_mad_lib(templete_file):
    openfile = open(templete_file, 'r')
    newfile = 'MAD_'+ templete_file
    newfile_out = open(newfile, 'w')
    replace_part = ['PLURAL NOUN', 'VERB PAST', 'VERB', 'NOUN', 'ADJECTIVE']
    for i in range(len(replace_part)):
        for line in openfile:
            replace_parts_of_speech(line, replace_part[i])

    for line in openfile:
        newfile_out.write(line)
    openfile.close()
    newfile_out.close()


def main():
    print_report('tortoise.txt')
    replace_parts_of_speech("the NOUN VERB PAST the NOUN", "VERB")
    complete_mad_lib('tortoise.txt')
if __name__ == '__main__':
    main()