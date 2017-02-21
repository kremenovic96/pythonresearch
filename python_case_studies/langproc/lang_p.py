#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:15:36 2017

@author: ranko
"""
import os
import pandas as pd

stats = pd.DataFrame(columns = ("language", "author", "title", "length","unique"))
text = "This is my test text. We're keeping this text short to keep things managable."
def count_words(text):
    """
    Count the number of times each word occurs in text(str)
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1     
    return word_counts        
def read_book(title_path):
    """
    Reads a book and returns it as string 
    """
    with open(title_path, "r", encoding = "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text    
           
def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique, counts)
title_num = 1 
book_dir = "./Books"
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir+"/"+language + "/"+author+"/"+title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts),num_unique
            title_num += 1         
        
    