# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:30:47 2022

@author: luisa
"""
#Read file
file= open("C:\\Users\\luisa\\Documents\\Spring 2022\\Bio Structures\\sequence.fasta", "r")
sequence1 = file.read()
#Remove queader
def get_sequence(sequence):
    sequence_list= sequence.splitlines()
    parsed_sequence= [] 
    for line in sequence_list: 
        parsed_sequence.append(line.split())
    i=0
    seq= "" 
    for line in parsed_sequence:
        if i > 0:
            seq += seq.join(line)
        i += 1
    return seq

seq= get_sequence(sequence1)

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

#part (d)
avg_hydrophobicity= calc_hydrophobicity(seq, 0, 10, kd_hydrophobicity)
avg_Q121 = calc_hydrophobicity(seq, 120, 10, kd_hydrophobicity)
print(avg_hydrophobicity)
print(avg_Q121)


#Place function in a loop to do parts (e) and (f)
kd_avgs= []
start = 0
w_len= 20
for i in range(len(seq)):
    avg = calc_hydrophobicity(seq, start, w_len, kd_hydrophobicity)
    kd_avgs.append(avg)
    start +=10
    if start > len(seq)-w_len:
        break
    
#print list
for item in kd_avgs:
    print(item)