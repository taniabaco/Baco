
# coding: utf-8

import numpy as np
import pandas as pd

def join_blocs(dataframe1,dataframe2, feature_vectors1, feature_vectors2):
    # Join the 2 DataFrames
    dataframe=pd.concat([dataframe1, dataframe2], axis=0)
    # Join the 2 Features values vectors
    feat_vect=np.concatenate((feature_vectors1,feature_vectors2), axis=0)
    return(dataframe, feat_vect)
    



