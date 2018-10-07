#!/usr/bin/env python
import pandas as pd
import glob
import re
def build(files_dir):
    all_files = glob.glob(files_dir+'/*.csv')
    fdf = []
    keys = []
    newid={1: 22, 2: 24, 3: 23, 4: 25, 5: 3, 6: 4, 7: 8, 8: 19,
     9: 20, 10: 21, 11: 9, 12: 26, 13: 10,
     14: 11, 15: 12, 16: 13, 17: 14, 18: 15, 19: 16,
     20: 27, 21: 17, 22: 18, 23: 6, 24: 1, 25: 2, 26: 7, 27: 5}
    for f in all_files:
         df = pd.read_csv(f,' ',names = ['year', 'week','1','VCI','TCI','VHI',] ,index_col=False, skiprows=[0], header=None, skipinitialspace=True)
         keys.append(str(newid[int(re.findall('\d+',f)[0])]))
         df=df[:-1].drop('1', axis=1)
         fdf.append(df)
    result = pd.concat(fdf)

    return result


def buildtwo(files_dir):
    all_files = glob.glob(files_dir+'/*.csv')
    fdf = []
    for f in all_files:
        df = pd.read_csv(f,index_col=False, skiprows=1,
        sep=r'\s+,*|,\s*',
        names=['year', 'week', 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70,75, 80, 85, 90, 95, 100],engine = 'python')
        df = df[:-1]
        fdf.append(df)
        result = pd.concat(fdf)
    return result


firstdf = build('data')
seconddf = buildtwo('data2')
result = pd.concat([firstdf.iloc[:,:],seconddf.iloc[:,2:]], axis=1)
fin = result[(result[0]+result[5]+result[10]+result[15])>50]
print fin
# c = ''
# while c!='q':
#     c = raw_input("select province by id> ")
#     y = raw_input("select year> ")
#     sframe = frame.loc[c]
#     sframe = sframe.loc[sframe['year']==y]
#     print sframe.loc[sframe['VHI'].idxmax()]
#     print sframe.loc[sframe['VHI'].idxmin()]
