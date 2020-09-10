#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : word2vec
# @Author   : 张志毅
# @Time     : 2020/9/10 9:41

from gensim.models import word2vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"D:\\Python\\WorkSpace\\word2vec\\Data\\text8")  # 加载语料
model = word2vec.Word2Vec(sentences, size=32)  # 训练skip-gram模型; 默认window=5





# 保存模型，以便重用
model.save("text8.model")
# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")

# 以一种C语言可以解析的形式存储词向量
model.wv.save_word2vec_format('embedding1.txt',binary = False)
# 对应的加载方式
# model_3 = word2vec.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)

if __name__ == "__main__":
    pass