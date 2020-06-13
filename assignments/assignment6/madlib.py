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


def main():
    print_report('tortoise.txt')
if __name__ == '__main__':
    main()