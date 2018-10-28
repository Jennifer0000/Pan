#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:06:57 2018

@author: panjianfei
"""

import scipy as sp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import time
import operator

table_sz=pd.read_csv('/Users/panjianfei/Desktop/data/标普500161125.SZ.csv')

#data clear
def clear(table):
    date=table['_date']
    n=len(date)
    date=[pd.Timestamp(date[i]) for i in range(0,n)]
    close=table['match']
    ratio=list(range(n))
    ratio[0]=1
    for i in range(1,n):
        ratio[i]=close[i]/close[i-1]
    df=pd.DataFrame(columns=['date','close','ratio'])
    df['date']=date
    df['close']=close
    df['ratio']=ratio
    df=df.set_index('date')
    return df   

df_sz=clear(table_sz)
n=len(df_sz.ratio)
ini=list(range(n))
ini[0]=1
for i in range(1,n-1):
    if df_sz.ratio[i]<0.93:
       ini[i+1]=ini[i]*df_sz.ratio[i+1]
    else:
       ini[i+1]=ini[i]
df_sz['ini']=ini
a=ini[n-1]/n*252
#writer = pd.ExcelWriter('output.xlsx')
#df_sz.to_excel(writer,'sheet1')
#writer.save()     
    
df_sz['ini'].plot()
        
