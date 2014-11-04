#!/usr/local/bin/python
# This file takes in 1 argument and searches the gold list and returns
# the Author and the Domain
# Usage :- python GoldDoc.py <doi>
# coding: utf-8

# In[41]:

import csv
from igraph import *
from sys import argv

def get_author(auth_id):
    file1 = open("../P2/gold/1.txt", "rb")
    file2 = open("../P2/gold/2.txt", "rb")
    file3 = open("../P2/gold/3.txt", "rb")
    file4 = open("../P2/gold/4.txt", "rb")
    file5 = open("../P2/gold/5.txt", "rb")
    file6 = open("../P2/gold/6.txt", "rb")
    file7 = open("../P2/gold/7.txt", "rb")
    file8 = open("../P2/gold/8.txt", "rb")
    file9 = open("../P2/gold/9.txt", "rb")
    file10 = open("../P2/gold/10.txt", "rb")
    file11 = open("../P2/gold/11.txt", "rb")
    file12 = open("../P2/gold/12.txt", "rb")
    file13 = open("../P2/gold/13.txt", "rb")

    bst = csv.reader(file1, dialect=csv.excel_tab)
    cv = csv.reader(file2, dialect=csv.excel_tab)
    crypto = csv.reader(file3, dialect=csv.excel_tab)
    dm = csv.reader(file4, dialect=csv.excel_tab)
    ie = csv.reader(file5, dialect=csv.excel_tab)
    ia = csv.reader(file6, dialect=csv.excel_tab)
    ml = csv.reader(file7, dialect=csv.excel_tab)
    nlp = csv.reader(file8, dialect=csv.excel_tab)
    nn = csv.reader(file9, dialect=csv.excel_tab)
    oa = csv.reader(file10, dialect=csv.excel_tab)
    pl = csv.reader(file11, dialect=csv.excel_tab)
    sw = csv.reader(file12, dialect=csv.excel_tab)
    svm = csv.reader(file13, dialect=csv.excel_tab)

    gold_list = {}

    for row in bst:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1:],"Boosting")

    for row in cv:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Computer Vision")

    for row in crypto:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Cryptography")

    for row in dm:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Data-Mining")

    for row in ie:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Information Extraction")

    for row in ia:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Intelligent Agents")

    for row in ml:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Machine Learning")

    for row in nlp:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Natural Language Processing")

    for row in nn:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Neural Networks")
    for row in oa:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Ontology Alignment")
    for row in pl:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Planning")
    for row in sw:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Semantic Web")
    for row in svm:
        for w in row:
            gold_list[(w.split()[0])] = (w.split()[1],"Support Vector Machine")
    print len(gold_list)
    try:
        return gold_list[str(auth_id)]
    except KeyError:
        print "No such Author in Gold List"

get_author('123456')
