# -*- coding:utf-8 -*-
# @Description: draft
# @Author: Shimin
# @Copyright
# @Version:0.0.1


fishmap = {1:"Bream", 2: "whatever"}
print(fishmap)
print(fishmap[1])


# 创建词典
person = {}

person['name'] = 'Tom'  # 字典名person[key] = 'value'
person['age'] = 22
person['city'] = 'Shanghai'
person['ID'] = '12345'

print(person) # {'name': 'Tom', 'age': 22, 'city': 'Shanghai', 'ID': '12345'}得到一个字典

print(person.keys()) # dict_keys(['name', 'age', 'city', 'ID'])得到一个全是key的列表
# 遍历字典
for key, value in person.items():
    print(f'key: {key}  ,  value: {value}')
for key in person.items():
    print(key)   # 可以运行但得到的是每一对(key,value)
for key in person.keys():
    print(key)   # 遍历只有key的列表



words = ['sun', 'moon', 'star', 'star',
         'star', 'moon', 'sun', 'star']
freq_dict = {}
for word in words:
    if word not in freq_dict.keys():   # 如果列表中的单词不在只有key的列表里
        freq_dict[word] = 1            # 字典名[key] = value
    else:
        freq_dict[word] += 1
print(freq_dict)                       # {'sun': 2, 'moon': 2, 'star': 4}
for key, val in freq_dict.items():
    print(key, val)