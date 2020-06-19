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
def main():
    load_twitter_dicts_from_file("twitter_emoticons.dat", {}, {})

if __name__ == '__main__':
    main()