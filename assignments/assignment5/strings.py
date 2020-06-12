# -*- coding:utf-8 -*-
# @Description: python assignment5
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def US_to_EU(str_from_int):
    date = str_from_int
    num_date = date.split('/')
    return f"{num_date[1]}.{num_date[0]}.{num_date[2]}"


def is_phone_num(possible_num):
    num_lst = possible_num.split('-')
    if len(num_lst) == 3:
        if len(num_lst[0]) == 3 and len(num_lst[1]) == 3 and len(num_lst[2]) == 4:
            if num_lst[0].isdigit() == num_lst[1].isdigit() == num_lst[2].isdigit():
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# def redact_line(old_string):
#     splited_line = old_string.split()
#
#     for i in range(len(splited_line)):
#         i = 0
#         if is_phone_num(splited_line[i-1]):
#             splited_line[i] = 'XXX-XXX-XXXX'
#             i += 1
#     print(" ".join(splited_line))
def redact_line(fline):
    # can't use replace only because it always starts at 0
    for i in range(len(fline) - 12):
        if ((i == 0 or fline[i - 1] == ' ') and fline[i + 12] in ' \n' and is_phone_num(fline[i:i + 12])):

            fline = fline[:i] + fline[i:].replace(fline[i:i + 12], "XXX-XXX-XXXX", 1)

    return fline


def redact_file(fname):
    fp = open(fname, 'r')
    name = fname[:-4] + "_redacted.txt"
    fp_out = open(name, 'w')
    for line in fp:
        fp_out.write(redact_line(line))
        # print(line)
    fp.close()
    fp_out.close()
def main():
    US_to_EU('3/13/18')
    is_phone_num('123-456-7890b')
    redact_line('123-456-7890 123-456-78901 123-456-7890\n')
    redact_file("redact_in.txt")
if __name__ == '__main__':
    main()
