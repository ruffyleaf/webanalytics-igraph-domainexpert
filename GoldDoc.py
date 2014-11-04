#!/usr/local/bin/python
# This file takes in 1 argument and searches the gold list and returns the domain.
# Usage :- python GoldDoc.py <doi>
# coding: utf-8

# In[41]:

import csv
from igraph import *
from sys import argv

def get_doc(doc_id):
    file1 = open("../P2/sresults/1.dois.txt", "rb")
    file2 = open("../P2/sresults/2.dois.txt", "rb")
    file3 = open("../P2/sresults/3.dois.txt", "rb")
    file4 = open("../P2/sresults/4.dois.txt", "rb")
    file5 = open("../P2/sresults/5.dois.txt", "rb")
    file6 = open("../P2/sresults/6.dois.txt", "rb")
    file7 = open("../P2/sresults/7.dois.txt", "rb")
    file8 = open("../P2/sresults/8.dois.txt", "rb")
    file9 = open("../P2/sresults/9.dois.txt", "rb")
    file10 = open("../P2/sresults/10.dois.txt", "rb")
    file11 = open("../P2/sresults/11.dois.txt", "rb")
    file12 = open("../P2/sresults/12.dois.txt", "rb")
    file13 = open("../P2/sresults/13.dois.txt", "rb")

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
            gold_list[(w.split()[0])] = "Boosting"

    for row in cv:
        for w in row:
            gold_list[(w.split()[0])] = "Computer Vision"

    for row in crypto:
        for w in row:
            gold_list[(w.split()[0])] = "Cryptography"

    for row in dm:
        for w in row:
            gold_list[(w.split()[0])] = "Data-Mining"

    for row in ie:
        for w in row:
            gold_list[(w.split()[0])] = "Information Extraction"

    for row in ia:
        for w in row:
            gold_list[(w.split()[0])] = "Intelligent Agents"

    for row in ml:
        for w in row:
            gold_list[(w.split()[0])] = "Machine Learning"

    for row in nlp:
        for w in row:
            gold_list[(w.split()[0])] = "Natural Language Processing"

    for row in nn:
        for w in row:
            gold_list[(w.split()[0])] = "Neural Networks"
    for row in oa:
        for w in row:
            gold_list[(w.split()[0])] = "Ontology Alignment"
    for row in pl:
        for w in row:
            gold_list[(w.split()[0])] = "Planning"
    for row in sw:
        for w in row:
            gold_list[(w.split()[0])] = "Semantic Web"
    for row in svm:
        for w in row:
            gold_list[(w.split()[0])] = "Support Vector Machine"

    try:
        print gold_list[str(doc_id)]
    except KeyError:
        print "No such doc in Gold List"

