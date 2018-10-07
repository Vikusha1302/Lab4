#!/usr/bin/env python
import pandas as pd
import urllib2
import os
import datetime
import time

def save(id):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=%d&year1=1981&year2=2018&type=Mean"%(id,)
    vhi_url = urllib2.urlopen(url)
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    out = open('cvs_files/datetime_' + now + '_vhi_id_%d.csv'%(id,),'wb')
    out.write(vhi_url.read())
    out.close()
    print "[ OK ] Vhi %d downloaded ..."%(id,)

os.mkdir("cvs_files")
for id in range(1,28):
    save(id)
