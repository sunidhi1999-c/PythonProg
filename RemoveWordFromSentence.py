# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:27:16 2021

@author: HP
"""

#RemovedWord in a sentence
word_list=input().strip().split()
search_list=input().strip().split()
for word in search_list:
    if word in word_list:
        del word_list[word_list.index(word)]

print(" ".join(word_list))