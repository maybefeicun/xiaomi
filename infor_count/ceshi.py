# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 21:26
# @Author  : chen
# @File    : ceshi.py
# @Software: PyCharm

import snownlp
import re
import os
import random
import textteaser
import sumy

def read_texts(input_path):
    texts = ''
    with open(input_path, encoding='utf-8', errors='ignore') as file_read:
        sentences = file_read.readlines()
        for sentence in sentences:
            split_pattern = re.compile(r"\t| ")  # 这里使用了多个分隔符
            text = re.split(split_pattern, sentence)[2]  # 微博内容在句子的第三个位置
            if text == '' or text == '\n':
                continue
            texts = texts + str(text) + '\n'
    file_read.close()
    return texts

def write_texts(output_path, texts):
    with open(output_path, 'w', encoding='utf-8') as file_write:
        file_write.write(texts)
    file_write.close()

def read_weibo_texts(output_path):
    with open(output_path, 'r', encoding='utf-8') as file_read:
        texts = file_read.readlines()
    file_read.close()
    return texts

# input_path = os.path.join('../input', '天津爆炸.txt')
# texts = read_texts(input_path)
output_path = os.path.join('../output', 'texts.txt')
# write_texts(output_path, texts)
weibo_texts = read_weibo_texts(output_path) # weibo_texts 为list类型
random.shuffle(weibo_texts) # 将微博打乱
weibo_texts_new = weibo_texts[:1000] # 取前一万条微博做测试
weibo_texts_new = ''.join(weibo_texts_new)

# 这个方法不能进行因为会出现内存报错
print('#####    snownlp    ######')
snow = snownlp.SnowNLP(weibo_texts_new)
summarys = snow.summary()
print(summarys)

print('#####    textteaser  #####')
tt = textteaser.TextTeaser()
sentences = tt.summarize(weibo_texts_new)
for sentence in sentences:
    print(sentence)

print('#####    sumy      #####')
