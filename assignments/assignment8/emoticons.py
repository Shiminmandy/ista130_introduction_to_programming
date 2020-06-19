# -*- coding:utf-8 -*-
# @Description: assignment8(2)
# @Author: Shimin
# @Copyright
# @Version:0.0.1


def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    openfile = open(filename, 'r')
    for line in openfile:
        splited = line.split(" ")
        # print(splited[0].strip('"'))
        # print(splited)
        # emoticon = splited[0].strip('"')
        emoticon = splited[0][1:-1]
        userID = splited[2][1:-1]
        # print(emoticon)
        if emoticon not in emoticons_to_ids.keys():
            emoticons_to_ids[emoticon] = [userID]
            # print(emoticons_to_ids)
        else:
            emoticons_to_ids[emoticon].append(userID)
    # print(emoticons_to_ids)

        if userID not in ids_to_emoticons.keys():
            ids_to_emoticons[userID] = [emoticon]
        else:
            ids_to_emoticons[userID].append(emoticon)
    # print(ids_to_emoticons)
"""
    设定最小值为-1，（list长度不可能小于-1），取变量名为max_length,设定最后的结果表情名字为""
    , 取变量名字为result_emo
    
    循环字典的key和value：
        如果value的长度大于max_length：
            那么max_length = value的长度
            并且，这个key赋值给result_emo
        (没有否则)
    打印
"""

def find_most_common(dict_name):
    max_length = -1
    result_emo = ""
    for key, val in dict_name.items():
        # length.append(len(val))
        # print(key, max(length))
        # print(key, val)
        if len(val) > max_length:
            max_length = len(val)
            result_emo = key
    print(f'{result_emo.ljust(21)}occurs{str(max_length).rjust(9)} times')
    return result_emo





def main():
    load_twitter_dicts_from_file("twitter_emoticons.dat", {}, {})
    dct = {'a': [1, 2, 3], 'b': [1, 2, 3, 4], 'c': [1, 2, 3, 4, 5], 'd':[1,2]}
    find_most_common(dct)
if __name__ == '__main__':
    main()