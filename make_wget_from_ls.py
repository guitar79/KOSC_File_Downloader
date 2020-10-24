#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:56:43 2020

@author: guitar79

# Open the file with read only permit



"""

#import os
#dir_name = "../L2_SST_MODIS/"
#filename_lst = sorted(os.listdir(dir_name))
 

f = open("MODIS_aqua_CHL_filenames.txt", "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
# close the file after reading the lines.
f.close()

 
url1 = "wget -T 300 -t 1 -r -nd -np -l 1 -N --no-if-modified-since -P ./  http://222.236.46.45/nfsdb/"

urls = ""
level = "L2/"
for line in lines :
    line = line.rstrip()
    if line[-4:] == ".zip" :
        filename_el = line.split(".")
        if filename_el[-3] == "aqua-1" : url2 = "MODISA/"
        elif filename_el[-3] == "terra-1": url2 = "MODIST/"
        
        urls += "{0}{1}{2}/{3}/{4}/{7}{8}\n".\
            format(url1, url2, filename_el[1],\
                   filename_el[2][:2], filename_el[2][2:],\
                   filename_el[3][2:], filename_el[3][:2],\
                   level, line)
        print(urls)

with open("wget_all.sh", 'w') as f2:
        f2.write(urls)
