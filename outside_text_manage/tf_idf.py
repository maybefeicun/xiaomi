# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 22:40
# @Author  : chen
# @File    : tf_idf.py
# @Software: PyCharm

'''
这个计算tf-idf的值，从而判断哪些关键词的权重从而对于关键字进行取舍
'''

import pickle
import os

sum = 0 # 提取关键词的文档的总词数

'''
读取存储5个类型词的文件
'''
np_path = os.path.join('../output', 'np_dict')
with open(np_path, 'rb') as file:
    np = pickle.load(file)
file.close()

ns_path = os.path.join('../output', 'ns_dict')
with open(ns_path, 'rb') as file:
    ns = pickle.load(file)
file.close()

ni_path = os.path.join('../output', 'ni_dict')
with open(np_path, 'rb') as file:
    ni = pickle.load(file)
file.close()

nz_path = os.path.join('../output', 'nz_dict')
with open(nz_path, 'rb') as file:
    nz = pickle.load(file)
file.close()

t_path = os.path.join('../output', 't_dict')
with open(t_path, 'rb') as file:
    t = pickle.load(file)
file.close()

v_path = os.path.join('../output', 'v_dict')
with open(np_path, 'rb') as file:
    v = pickle.load(file)
file.close()

def init_idf(dict_tf, dict_idf):
    for key in dict_tf.keys():
        dict_idf[key] = 0

    return dict_idf

def count_idf(dict_idf, words):
    for key in dict_idf.keys():
        if key in words:
            dict_idf[key] += 1
    return dict_idf


outside_seg = os.path.join('../output', 'outside_seg.txt')
document_count = 0 # 文档计数
np_idf = init_idf(np, {}) # 初始化每个单词的逆文档的值
ns_idf = init_idf(ns, {})
ni_idf = init_idf(ni, {})
t_idf = init_idf(t, {})
v_idf = init_idf(v, {})

count = 0
with open(outside_seg, 'r', encoding='utf-8') as file_read:
    while True:
        print(str(count))
        count += 1
        line = file_read.readline().strip()
        if not line: # 跳出标志服了自己了
            break
        words = line.split(' ') # 将单词分开
        # 对每个单词在文档中的
        np_idf = count_idf(np_idf, words)
        ns_idf = count_idf(ns_idf, words)
        ni_idf = count_idf(ni_idf, words)
        t_idf = count_idf(t_idf, words)
        v_idf = count_idf(v_idf, words)

np_file = os.path.join('../output', 'np_idf_dict')
with open(np_file, 'wb') as write:
    pickle.dump(np_idf, write)
write.close()
del np

ns_file = os.path.join('../output', 'ns_idf_dict')
with open(ns_file, 'wb') as write:
    pickle.dump(ns_idf, write)
write.close()
del ns

ni_file = os.path.join('../output', 'ni_idf_dict')
with open(ni_file, 'wb') as write:
    pickle.dump(ni_idf, write)
write.close()
del ni

t_file = os.path.join('../output', 't_idf_dict')
with open(t_file, 'wb') as write:
    pickle.dump(t_idf, write)
write.close()
del t

v_file = os.path.join('../output', 'v_idf_dict')
with open(v_file, 'wb') as write:
    pickle.dump(v_idf, write)
write.close()
del v

