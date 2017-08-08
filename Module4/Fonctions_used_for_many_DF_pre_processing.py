
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd

def getDF(DF):
    D_Indexc=np.arange(0,DF.shape[0])
    D_Indexc=np.ones(D_Indexc.shape[0])
    D_Indexc=D_Indexc.reshape(-1,1)
    for i in range(0, DF.shape[0]):
        D_Indexc[i]=i*D_Indexc[i]
    D_Indexc
    DFS=DF
    DFS['indice']=D_Indexc
    return(DFS)



def Switch_Indices(DF):
    (DF.index)=(DF.indice)[:]
    return(DF)


def exclure(dfin,weight,height):
    "Borders conditions to exclude data"
    a=dfin.loc[dfin.X>=(weight/2)]
    b=a.loc[a.Y!=2446] # POUR NOTRE CAS
    c=b.loc[b.Y>=(height/2)]
    d=c.loc[c.Y<=(max(c.Y)-height/2)]
    dfout=d.loc[d.X<=(max(d.X)-weight/2)]
    return(dfout)

# Exclure les x et y negatifs sinon ca ne fonctionne pas! 
def exclure_Bc(dfin,weight,height):
    d=dfin.loc[dfin.Y<=(np.max([dfin.Y])-height/2)]
    dfout=d.loc[d.X<=(max(d.X)-weight/2)]
    return(dfout)