# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 16:18
# @Author  : chen
# @File    : thulac_segment.py
# @Software: PyCharm

'''本代码使用THULAC来进行分词处理，做了两种分词结果一种是词性标注另一种没有'''
'''
本代码的经验在于文件格式的问题文件的分隔符均为：/
同时以后尽量别用.txt进行文件存储这样不好读取
'''

import thulac
import re
import os
import pickle

def read_stopwords(filepath):
    # stopwords = []
    with open(filepath, encoding='utf-8') as file_read:
        words = file_read.readlines()
        stopwords = [word.strip('\n') for word in words]
    file_read.close()
    return stopwords

def segment(input_path, output_path, stopwords):
    # thu = thulac.thulac(seg_only=True)
    thu = thulac.thulac()
    segment_result = []
    count = 1
    with open(input_path, encoding='utf-8') as file_read:
        sentences = file_read.readlines()
        file_read.close()
        for sentence in sentences:
            split_pattern = re.compile(r"\t| ")  # 这里使用了多个分隔符
            text = re.split(split_pattern, sentence)[2]  # 微博内容在句子的第三个位置
            segments = thu.cut(text)  # 这个分词结果带有词性标注的结果，所以要对词性标注进行处理
            seg_result = []
            for seg in segments:
                if seg[0] in stopwords:
                    continue
                else:
                    seg_result.append(seg)
            segment_result.append(seg_result)
            print(count)
            count += 1
    with open(output_path, 'wb') as file_write:
        pickle.dump(segment_result, file_write)
    file_write.close()

stopwords_filepath = os.path.join('../stopwords', 'CNstopwords.txt') # 注意文件的书写格式
input_filepath = os.path.join('../input', '天津爆炸.txt')

if not os.path.exists('../output'):
    os.makedirs('../output')
output_filepath = os.path.join('../output', 'segment.txt')
stopwords = read_stopwords(stopwords_filepath)
segment(input_filepath, output_filepath, stopwords)