# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:01:13 2022

@author: luisa
"""
file= open("C:\\Users\\luisa\\Documents\\Spring 2022\\Bio Structures\\sequences.fasta", "r")
sequences = file.read()

#Dictionary to store kd hydrophobicity scores
kd_hydrophobicity= {
    "I":4.5, "V":4.2, "L":3.8, "F":2.8,
    "C":2.5, "M":1.9, "A":1.8, "G":-0.4,
    "T":-0.7, "S":-0.8, "W":-0.9, "Y":-1.3,
    "P":-1.6, "H":-3.2, "E":-3.5, "Q":-3.5,
    "D":-3.5, "N":-3.5, "K":-3.9, "R":-4.5,
    }

def calc_hydrophobicity(sequence, start, w_len, dct):
    i= start
    add = 0
    window= ""
    for aa in sequence:
        if len(window) < w_len:
            window += sequence[i]
            i+=1
    for aa in window:
        key= aa
        add += dct[key]
    avg = add/w_len
    return round(avg,2)

#
sequences_list= sequences.splitlines()

results= []
seq_txt= ""
for item in sequences_list:
    if not item.startswith(">"):
        seq_txt += item
        
        if item == sequences_list[-1]:
            results.append(seq_txt)
    else:
        if len(seq_txt) >0:
            results.append(seq_txt)
            seq_txt= ""


#Place function in a loop
d_kd_avgs= {}
start = 0
w_len= 20
for i in range(len(results)):
    d_kd_avgs["list{0}".format(i)] = []
    for j in range(len(results[i])):
        avg = calc_hydrophobicity(results[i], start, w_len, kd_hydrophobicity)
        d_kd_avgs["list{0}".format(i)].append(avg)
        start +=10
        if start > len(results[i])-w_len:
            start=0
            break
    
kd_avgs_list= list(d_kd_avgs.values())

avgs= {}
for i in range(len(kd_avgs_list)):
    addition =0
    avgs["sequence{0}".format(i)] = 0
    for j in range(len(kd_avgs_list[i])):
        addition+= kd_avgs_list[i][j]
    line_avg= addition/ len(kd_avgs_list)
    avgs["sequence{0}".format(i)] = (round(line_avg,2))


import matplotlib.pyplot as plt
keys = list(avgs.keys())
values = list(avgs.values())
plt.bar(range(len(avgs)), values, tick_label=keys)
plt.show()
