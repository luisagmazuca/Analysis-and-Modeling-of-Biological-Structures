# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:49:21 2022

@author: luisa
"""
import csv
from collections import Counter
import matplotlib.pyplot as plt

with open("C:\\Users\\luisa\\Documents\\Spring 2022\\Bio Structures\\human_gpcrs.tsv") as file:
    tsv_file= csv.reader(file, delimiter="\t")

    #for line in tsv_file:
            #print(line[12])
            
    tsv_list= []
    for line in tsv_file:
        if line[12] in ["GRAFS (Family)","-"]:
            continue
        else:
            tsv_list.append(line[12])

    
    gpcrs_dict= Counter(tsv_list)
    print(gpcrs_dict)
    
    labels = []
    sizes = []

    for x, y in gpcrs_dict.items():
        labels.append(x)
        sizes.append(y)

    #Plot without percentages
    plt.pie(sizes, labels=labels)
    
    plt.axis('equal')
    plt.show()
    
    #Plot with percentages
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()