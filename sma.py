import Bakker
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import math
import csv
import json
import pandas as pd
def momentum(df, n):
    """

    :param df: pandas.DataFrame
    :param n:
    :return: pandas.DataFrame
    """
    M = pd.Series(df['MA_1'].diff(n), name='Momentum_' + str(n))
    df = df.join(M)
    return df
xaxis=[]
plist=[]
mlist=[]
mdlist=[]
smalist=[]
spydata=si.get_data('spy' , start_date = '12/27/2008')
smapd=Bakker.moving_average(spydata,1)
mpd=momentum(smapd,12)

for x in range (len(mpd.index)):
    smalist.append(mpd.iloc[x,7])
for x in range (len(mpd.index)):
    plist.append(mpd.iloc[x,3])
for x in range (len(mpd.index)):
    mlist.append(mpd.iloc[x,8])
for x in range (len(mlist)):
    xaxis.append(x)
for x in range (1,len(mlist)):
    mdlist.append(mlist[x]-mlist[x-1])
plt.subplot(2, 1, 1)
plt.plot(xaxis, plist)
plt.plot(xaxis, smalist)
plt.title('Trading')
shares=0
money=100000
shares=math.floor(money/plist[0])
money=money-plist[0]*shares
dist=1
"""for x in range (len(mlist)):
    if mlist[x]>0 and shares==0:
        shares=math.floor(money/plist[x])
        money=money-plist[x]*shares
        plt.plot(x,plist[x], 'go')
    if mlist[x]<0 and shares!=0:
        money=money+plist[x]*shares
        shares=0
        plt.plot(x,plist[x], 'ro')"""
for x in range (2,len(smalist)):
    #if smalist[x-1]<smalist[x] and smalist[x-1]<smalist[x-2] and shares==0:
    #if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and shares==0:
    if mlist[x-1]<mlist[x] and mlist[x-1]<mlist[x-2] and  smalist[x-1]<smalist[x] and smalist[x-1]<smalist[x-2] and shares==0:
    #if smalist[x-1]<smalist[x] and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and mlist[x-dist]>0 and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and mdlist[x-dist]>0 and shares==0:
    #if smalist[x-dist]<smalist[x] and smalist[x-dist]<smalist[x-2*dist] and shares==0:
        #print("up")
        shares=math.floor(money/plist[x])
        money=money-plist[x]*shares
        plt.plot(x,plist[x], 'go')
    #if smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    #if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and shares!=0:
    if mlist[x-1]>mlist[x] and mlist[x-1]>mlist[x-2] and smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    #if smalist[x-1]>smalist[x] and smalist[x-1]>smalist[x-2] and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and mlist[x-dist]<0 and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and mdlist[x-dist]<0 and shares!=0:
    #if smalist[x-dist]>smalist[x] and smalist[x-dist]>smalist[x-2*dist] and shares!=0:
        #print("down")
        money=money+plist[x]*shares
        shares=0
        plt.plot(x,plist[x], 'ro')
money=money+plist[len(plist)-1]*shares
print("Momentum",money)
print("Holding ",math.floor(100000/plist[0])*plist[len(plist)-1]+(100000-math.floor(100000/plist[0])*plist[0]))

#print(mpd)
plt.subplot(2, 1, 2)
plt.plot(xaxis, mlist)


plt.show()
