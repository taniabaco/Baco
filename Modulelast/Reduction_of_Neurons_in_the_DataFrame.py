
# coding: utf-8
import numpy as np
import pandas as pd



def Get_DataFrame_less_Neurons(dfpoints):
   
    dfpoints=dfpoints.loc[dfpoints.TYPE!=0].copy()
    # Reduire le nombre de neurones de la base de donnees
    data_Astrocytes=dfpoints.loc[dfpoints.TYPE==1.0].copy()
    data_Astrocytes.head()

    data_Neurons=dfpoints.loc[dfpoints.TYPE==2.0].copy()
    idx = np.random.randint(0,len(data_Neurons),size=(len(data_Astrocytes),))
    data_Neurons=data_Neurons.iloc[idx].copy()

    dfpoints= data_Neurons.append(data_Astrocytes).copy()
    
    return(dfpoints)





