
# coding: utf-8


import numpy as np
import pandas as pd
#global Data_frame

def Get_Dataframe(imageId, Data_frame):
    
    " index the Clones "
    ROI_Index=np.arange(0,Data_frame.shape[0])
    ROI_Index=np.zeros(ROI_Index.shape[0])
    ROI_Index=ROI_Index.reshape(-1,1)
    
    for k in range(1,Data_frame.shape[0]) :
        if Data_frame.Name[k]=='r' :
            ROI_Index[k]=ROI_Index[k-1]+1
        else :
            ROI_Index[k]=ROI_Index[k-1]
        ROI_Index
    
    Data_frame['Clone']=ROI_Index
    np.concatenate((Data_frame,ROI_Index), axis=1)
     
    " index the Type "
    index_Type=np.arange(0,Data_frame.shape[0])
    index_Type=np.zeros(index_Type.shape[0])
    index_Type=index_Type.reshape(-1,1)
    
    for l in range(0, Data_frame.shape[0]):
        if Data_frame.Name[l]=='m' :
            index_Type[l]=1
        elif Data_frame.Name[l]=='r':
            index_Type[l]=0
        else :
            index_Type[l]=2
        index_Type    
    
    Data_frame['TYPE']=index_Type
    np.concatenate((Data_frame,index_Type), axis=1)
     
    " index Id Image"
    D_Index=np.arange(0,Data_frame.shape[0])
    D_Index=np.ones(D_Index.shape[0])
    D_Index=imageId*D_Index.reshape(-1,1)
    Data_frame['ID_Image']=D_Index
    return(Data_frame)   


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