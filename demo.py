#!/usr/bin/env python3
# coding: utf-8
# File: demo.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-24
from pypinyin import *

class WordCorrect:
    def __init__(self):
        self.char_path = 'char.txt'
        self.model_path = 'pinyin2word.model'
        self.charlist = [word.strip() for word in open(self.char_path) if word.strip()]
        self.pinyin_dict = self.load_model(self.model_path)

    def load_model(self, model_path):
        f = open(model_path, 'r')
        a = f.read()
        word_dict = eval(a)
        f.close()
        return word_dict

    def edit1(self, word):
        n = len(word)
        return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
                   [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
                   [word[0:i]+c+word[i+1:] for i in range(n) for c in self.charlist] + # alteration
                   [word[0:i]+c+word[i:] for i in range(n+1) for c in self.charlist])  # insertion

def build_model():
    word_dict = {}
    count = 0
    for line in open('dict.txt'):
        count += 1
        print(count)
        line = line.strip().split(' ')
        word = line[0]
        word_count = line[1]
        word_pinyin = ','.join(lazy_pinyin(word))
        if word_pinyin not in word_dict:
            word_dict[word_pinyin] = word + '_' + word_count
        else:
            word_dict[word_pinyin] += ';' + word + '_' + word_count

    data = {}
    for pinyin, words in word_dict.items():
        tmp = {}
        for word in words.split(';'):
            word_word = word.split('_')[0]
            word_count = int(word.split('_')[1])
            tmp[word_word] = word_count
        data[pinyin] = tmp


    f = open('pinyin2word.model', 'w')
    f.write(str(data))
    f.close()

def test():
    corrector = WordCorrect()
    word = '我门'
    word_pinyin = ','.join(lazy_pinyin(word))
    candiwords = corrector.edit1(word)
    print(candiwords)
    print(word_pinyin)
    print(corrector.pinyin_dict.get(word_pinyin, 'na'))

test()
