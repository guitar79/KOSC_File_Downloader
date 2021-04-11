#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:56:43 2020

@author: guitar79

# Open the file with read only permit

</nfsdb/COMS/GOCI/1.2/2011/05/04/L2/COMS_GOCI_L2A_GA_20110504041642.CHL.he5.zip>
http://222.236.46.45/nfsdb/COMS/GOCI/1.2/2011/11/04/L2/COMS_GOCI_L2A_GA_20111104021640.CHL.he5.zip
http://222.236.46.45/nfsdb/COMS/GOCI/1.2/2011/05/04/L2/COMS_GOCI_L2A_GA_20110504041642.CHL.he5.zip

"""

#import os
#dir_name = "../L2_SST_MODIS/"

#filename_lst = sorted(os.listdir(dir_name))

file_name = "MODIS_aqua_SST_filenames.txt"
file_name = "GOCI_CHL_filenames.txt"

f = open("{}".format(file_name), "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
# close the file after reading the lines.
f.close()

print("len(lines) :{}".format(len(lines)))

url1 = "wget -T 300 -t 1 -r -nd -np -l 1 -N --no-if-modified-since -P ./  http://222.236.46.45/nfsdb/"

urls = ""
level = "L2/"
for line in lines[:] :
    line = line.rstrip()
    print("line :{}".format(line))
    print("line[-4] :{}".format(line[-4]))
    if line[-4:] == ".zip" :
        filename_el = line.split("_")
        if filename_el[1] == "GOCI" : url2 = "COMS/GOCI/2.0/"
        urls += "{0}{1}{2}/{3}/{4}/L2/{5}\n".\
            format(url1, url2, \
            filename_el[-1][:4], filename_el[-1][4:6], filename_el[-1][6:8], line)

        '''
        urls += "{0}{1}{2}/{3}/{4}/{7}{8}\n".\
            format(url1, url2, filename_el[1],\
                   filename_el[2][:2], filename_el[2][2:],\
                   filename_el[3][2:], filename_el[3][:2],\
                       level, line)
        '''
        print(urls)

with open("{}_wget.sh".format(file_name[:-14]), 'w') as f2:
	f2.write(urls)
