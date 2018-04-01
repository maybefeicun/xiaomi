# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 21:57
# @Author  : chen
# @File    : other_weibo.py
# @Software: PyCharm

'''
本代码是进行其他文档的分词处理来计算已经聚类的微博高频词的tf-idf值
我的想法是提取大概一百万条微博来进行分词处理已得到相应的外部数据集
'''

import os
import csv
import thulac

def read_stopwords(filepath):
    # stopwords = []
    with open(filepath, encoding='utf-8') as file_read:
        words = file_read.readlines()
        stopwords = [word.strip('\n') for word in words]
    file_read.close()
    return stopwords

def segment(input_path, output_path, stopwords):
    thu = thulac.thulac(seg_only=True)
    with open(input_path, encoding='utf-8', errors='ignore') as file_read:
        with open(output_path, 'w', encoding='utf-8') as file_write:
            lines = csv.reader(file_read)
            # csv_write = csv.writer(file_write) # 创建一个csv的读指针
            for line in lines:
                weibo_txt = line[5]  # 微博正文内容
                segments = thu.cut(weibo_txt)
                seg_result = []
                for seg in segments:
                    if seg[0] in stopwords or seg[0] == ' ':
                        continue
                    else:
                        seg_result.append(seg[0])
                if len(seg_result) < 8:
                    continue
                text = ' '.join(seg_result)
                file_write.write(text + '\n') # 利用csv写一行

stopwords_filepath = os.path.join('../stopwords', 'CNstopwords.txt') # 注意文件的书写格式
stopwords = read_stopwords(stopwords_filepath)
input_path = os.path.join('../input', 'outside_data.csv')
output_path = os.path.join('../output', 'outside_seg.txt')
segment(input_path, output_path, stopwords)