
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
     
    " index the Type : 1 Astrocyte, 2 Neuron, 0 rectangle"
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