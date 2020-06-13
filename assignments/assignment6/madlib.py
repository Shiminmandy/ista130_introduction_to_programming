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
    print("tortoise.txt".center(25, "-"))
    print(f"Vowels:{vowel_count}")
    print(f"Consonants:{consonants_count}")
    print(f"Whitespace:{whitespace_count}")
    print(f"Punctuation:{punctuaton_count}")
    print("-" * 25)
    print(f"Total:{vowel_count + consonants_count + whitespace_count +punctuaton_count}")




    # for j in range(len(consonants)):
    #     c = line.count(consonants[j])
    #     consonants_count += c
    # print(consonants_count)


def main():
    print_report('tortoise.txt')
if __name__ == '__main__':
    main()