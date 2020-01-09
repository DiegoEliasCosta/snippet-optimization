# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:49:30 2017

@author: musfiqur
"""


"""
This script takes two command line arguments:
arg1 -> File to read (in which Alignment frequency and entropy are saved) Example: ../Data/C1_Title_Data/Alignment/eng2code_alignment.txt
arg2 -> File to write the extracted entropy Example: ../Data/C1_Title_Data/Alignment/title2code_alignment.csv

Command to run the file:
python AlignmentEntropyStat.py arg1 arg2
"""

import codecs, statistics, sys

file_open = codecs.open(sys.argv[1], 'r', encoding = 'utf8')

contents = file_open.readlines()

data_lines = [x.strip() for x in contents]

file_open.close()


data_list = []

for line in contents:
    if "entropy " in line and "nTrans " in line:
        print line
        ent = line.split("entropy ")[1].split("nTrans")[0].replace("\t","")
	print ent
        data_list.append(float(ent))



print "Mean: " + str(statistics.mean(data_list))
print "Median: " + str(statistics.median(data_list))


print len(data_list)

ent_file = open(sys.argv[2], 'a')

for data in data_list:
    ent_file.write(str(data) + "\n")

ent_file.close()

