#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:56:43 2020

@author: guitar79

# Open the file with read only permit



"""
read_filename = "AVHRR_SST.txt"
f = open("{}".format(read_filename), "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
# close the file after reading the lines.
f.close()

lines = lines[0].split("li")
print("len(lines): {}".format(len(lines))

#gn: middle; user-select: auto;" value="MYDOCBOX.2011.1006.0443.aqua-1.hdf.zip^67346"><a href="#" onc
filenames = ""
for line in lines[:] :
    if line.find("value=") != -1 and line.find(".asc.zip") != -1 :
       filenames += "{}\n".format(line[line.find("value=")+7:line.find(".asc.zip")+8])
       print(filenames)

with open("{}_filenames.txt".format(read_filename[:-4]), 'w') as f2:
    f2.write(filenames)
