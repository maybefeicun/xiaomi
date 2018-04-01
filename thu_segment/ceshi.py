# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 20:18
# @Author  : chen
# @File    : ceshi.py
# @Software: PyCharm

import re

sentence = 'chen\tnan chen nan\tchen'
split_pattern = re.compile(r"\t| ") # 这里使用了多个分隔符
text = re.split(split_pattern, sentence)
print(text)

import thulac

sentence = '8月12日23:30左右，天津滨海新区第五大街与跃进路交叉口的一处集装箱码头发生爆炸。'
thu = thulac.thulac(filt=True)

sentence = '中国政府将会对美国的制裁行动采取相应的措施'
words = thu.cut(sentence)
print(words)