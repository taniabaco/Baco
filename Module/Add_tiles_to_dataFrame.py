
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd

import Fonctions_used_for_many_DF_pre_processing as fct_pp
reload(fct_pp);

def Add_tiles_to_dataFrame(original_dataFrame, weight, height):
    
    columns_names = list(original_dataFrame.columns.values)
    df_New=np.zeros([2*original_dataFrame.shape[0],len(columns_names)])
    df_New=pd.DataFrame(data=df_New,columns= original_dataFrame.columns)
    df_New=pd.concat([original_dataFrame, original_dataFrame], axis=0)
    df_New=fct_pp.getDF(df_New)
    df_New=fct_pp.Switch_Indices(df_New)



    # left up
    for i in range(1,len(df_New)/2-1):
        df_New.X[i+original_dataFrame.shape[0]]=-weight/2+df_New.X[i-1]+1
        df_New.Y[i+original_dataFrame.shape[0]]=-height/2+df_New.Y[i-1]+1
    #  right up
    df_New_r_u=original_dataFrame.copy()
    for i in range(0,len(df_New)/2-1):
        df_New_r_u.X[i]=weight/2+df_New.X[i]
        df_New_r_u.Y[i]=-height/2+df_New.Y[i]+1

    # left down
    df_New_l_d=original_dataFrame.copy()
    for i in range(0,len(df_New)/2-1):
        df_New_l_d.X[i]=-weight/2+df_New.X[i]+1
        df_New_l_d.Y[i]=height/2+df_New.Y[i]

    # right down
    df_New_r_d=original_dataFrame.copy()
    for i in range(0,len(df_New)/2-1):
        df_New_r_d.X[i]=weight/2+df_New.X[i]
        df_New_r_d.Y[i]=height/2+df_New.Y[i]

    # concat the data frames
    df_NEW=pd.concat([df_New, df_New_r_u], axis=0)
    df_NEW=pd.concat([df_NEW, df_New_l_d], axis=0)
    df_NEW=pd.concat([df_NEW, df_New_r_d], axis=0)
    df_New=fct_pp.getDF(df_NEW)
    df_New=fct_pp.Switch_Indices(df_New)
    df_New_copy=df_New.copy()

    return(df_New_copy)

