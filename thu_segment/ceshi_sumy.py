# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 14:49
# @Author  : chen
# @File    : ceshi_sumy.py
# @Software: PyCharm

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import os

LANGUAGE = "czech"
SENTENCES_COUNT = 10

if __name__ == "__main__":
    # url = "http://www.zsstritezuct.estranky.cz/clanky/predmety/cteni/jak-naucit-dite-spravne-cist.html"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # texts = parser.document
    # or for plain text files
    file_path = os.path.join('../output', 'document.txt')
    with open(file_path, encoding='utf-8', errors='ignore') as file_read:
        lines = file_read.readlines()
    file_read.close()
    texts = ''.join(lines)
    parser = PlaintextParser.from_string(texts, Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_file('document.txt', Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
