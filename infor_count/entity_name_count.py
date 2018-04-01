# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 16:59
# @Author  : chen
# @File    : entity_name_count.py
# @Software: PyCharm

import os
import pickle

with open(os.path.join('../output', 'segment.txt'), 'rb') as file_read:
    lines = pickle.load(file_read)
file_read.close()

np = {} # 存储人名
ns = {} # 存储地名
ni = {} # 存储机构名
nz = {} # 存储其他专业名词
t = {} # 存储时间词
v = {} # 存储动词

def construct_dict(dictionary, word):
    if word in dictionary.keys():
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    return dictionary

def dict_sort(dict):
    return sorted(dict.iteritems(), key=lambda d: d[1], reverse=True)

word_count = 0
for line in lines:
    for word_type in line:
        word_count += 1
        word = word_type[0] # 词本身
        type = word_type[1] # 词的词性
        if type == 'np':
            np = construct_dict(np, word)
        elif type == 'ns':
            ns = construct_dict(ns, word)
        elif type == 'ni':
            ni = construct_dict(ni, word)
        elif type == 't': # 这里记得处理下，时间的处理要小心
            t = construct_dict(t, word)
        elif type == 'v':
            v = construct_dict(v, word)
        else:
            continue

np_file = os.path.join('../output', 'np_dict')
with open(np_file, 'wb') as write:
    pickle.dump(np, write)
write.close()
del np

ns_file = os.path.join('../output', 'ns_dict')
with open(ns_file, 'wb') as write:
    pickle.dump(ns, write)
write.close()
del ns

ni_file = os.path.join('../output', 'ni_dict')
with open(ni_file, 'wb') as write:
    pickle.dump(ni, write)
write.close()
del ni

nz_file = os.path.join('../output', 'nz_dict')
with open(nz_file, 'wb') as write:
    pickle.dump(nz, write)
write.close()
del nz

t_file = os.path.join('../output', 't_dict')
with open(t_file, 'wb') as write:
    pickle.dump(t, write)
write.close()
del t

v_file = os.path.join('../output', 'v_dict')
with open(v_file, 'wb') as write:
    pickle.dump(v, write)
write.close()
del v

word_count_path = os.path.join('../output', 'word_count')
with open(word_count_path, 'w') as write:
    write.write(str(word_count))
write.close()