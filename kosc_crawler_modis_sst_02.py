import requests

import sys
from sys import argv

script, year = argv # Input year   

def file_exists(url):
    response = requests.head(url)
    if response.status_code == 200:
        return True
    else :
        return False

yr = int(year)

#</nfsdb/MODIST/2016/05/08/L2/MODOCT.2016.0508.1436.terra-1.hdf.zip>
#</nfsdb/MODIST/2016/05/09/L2/MODOCBOX.2016.0509.0236.terra-1.hdf.zip>

url1 = "http://222.236.46.45/nfsdb/"

url2s = [("MODISA/", "MYDOCT", "aqua-1"),
         ("MODISA/", "MYDOCSST", "aqua-1"),
         ("MODIST/", "MODOCT", "terra-1"),
         ("MODIST/", "MODOCSSTT", "terra-1")]
#url2s = ['MODIST/']

levels = [#'L1B/',
'L2/' 
#'L3/'
]

level = "L2/"

urls = ""
for url2 in url2s :
    for mo in range(1, 13) : 
        for da in range(1, 32) : 
            for hr in range(0, 24) : 
                for mi in range(0, 60) : 
                    url = "{0}{1}{2:04d}/{3:02d}/{4:02d}/{7}{8}.{2:04d}.{3:02d}{4:02d}.{5:02d}{6:02d}.{9}.hdf.zip\n".\
                                format(url1, url2[0], yr, mo, da, hr, mi, level, url2[1], url2[2])
                    if file_exists(url):
                        urls += url
                        print(url)
                        with open("KOSC_L2_SST_urls_add_{}.txt".format(str(yr)), 'a') as f:
                            f.write(url)
                    else :
                        print("url is not exist : {}".format(url))
                        
    with open("KOSC_L2_SST_urls_finish_{}.txt".format(str(yr)), 'w') as f:
        f.write(url)