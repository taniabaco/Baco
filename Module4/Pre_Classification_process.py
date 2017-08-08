
# coding: utf-8

# # Compute for each bloc ( different image ID)
# ### data processing of the manually annoted dataset
# ### image processing : extraction of RGB volumes
# ### Features extraction based on WND-charm Model




import numpy as np
import pandas as pd
from functools import partial
import multiprocessing
get_ipython().magic(u'matplotlib notebook')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as cm
import pickle
from pandas import DataFrame, read_csv,concat,merge

import Pre_Processing_the_annotated_dataset as pp
reload(pp);
import Pre_Processing_the_annotated_dataset_block2 as pp2
reload(pp2);
import Reduction_of_Neurons_in_the_DataFrame as nr
reload(nr);
import Fonctions_used_for_many_DF_pre_processing as fct_pp
reload(fct_pp);
import Add_Background_class_to_Dataframe as Bc
reload(Bc);
import Get_Partial_Data as gpd
reload(gpd);
import RGB2GRAY
reload(RGB2GRAY);
import Features_computing as FC
reload(FC);




weight=25
height=25

dfpoints1=read_csv(projectpath+'io/Input/Bloc01_pointes_first_mod.csv')

def Get_informations_for_classifier(imageId, weight, height, dfpoints1):
    


    dfpoints=pp.Get_Dataframe(imageId, dfpoints1)

# ## Reduce the number of Neurons in order to have as many as Astrocytes
    dfpoints=nr.Get_DataFrame_less_Neurons(dfpoints)
    DF_=nr.Get_Data_frame(imageId, dfpoints)
    Data_FRAMES=fct_pp.getDF(DF_)
    Data_FRAMES=fct_pp.Switch_Indices(Data_FRAMES)
    Data_FRAMES=fct_pp.exclure(Data_FRAMES,weight, height)
    D_F=fct_pp.getDF(Data_FRAMES)
    Data_FRAMES=fct_pp.Switch_Indices(D_F)
    Data_FRAMES.to_pickle(projectpath+'io/Output/Data_FRAMES.pkl')

 # Add a fourth class to the data Frame (Background Type :4)
    Data_FRAMES=pd.read_pickle(projectpath+'io/Output/Data_FRAMES.pkl')
    New_DF=Bc.Get_Df_with_backgroung_class(Data_FRAMES,imageId)
    New_DF=fct_pp.exclure_Bc(New_DF,weight,height)
    New_DF=fct_pp.getDF(New_DF)
    New_DF=fct_pp.Switch_Indices(New_DF)

# # Create the full data Frame ( 1135 Adtrocytes, 1135 Neurons, 1151 background) 
# Join the 2 DataFrames
    Dataframe_=pd.concat([Data_FRAMES, New_DF], axis=0)
    Dataframe_=fct_pp.getDF(Dataframe_)
    Dataframe_=fct_pp.Switch_Indices(Dataframe_)
    Dataframe_.to_pickle(projectpath+'io/Output/Dataframe_.pkl')
    Data_FRAMES=pd.read_pickle(projectpath+'io/Output/Dataframe_.pkl')


# # Get volumes with Multiprocessing

    #Metrics
    zsize=3
    nidx=Data_FRAMES.shape[0] 

    partial_getDATA_MEAN = partial(gpd.get_mean_zstacks_data, imageId=imageId, zsize=zsize, h=height, w=weight, Data_F=Data_FRAMES)

    # get raw data using multiprocesses

    pool = multiprocessing.Pool(27)
    M_Means = pool.map(partial_getDATA_MEAN,xrange(nidx))
    pool.close()


    filename_M_DF =projectpath+'io/Output/M_DF.npy'

    np.save(filename_M_DF,M_Means)
# ## Load Normalized volums as numpy array
    M_DF_parallel=np.load(filename_M_DF)



    partial_get_Gray_Img = partial(RGB2GRAY.Convert_Im_in_Gray_levels, h=height, w=weight, M_mean=M_DF_parallel)

    pool = multiprocessing.Pool(27)
    GRAY_IM = pool.map(partial_get_Gray_Img,xrange(nidx))
    pool.close()

    filename_Gray_IM =projectpath+'io/Output/GRAY_IM.npy'

    np.save(filename_Gray_IM,GRAY_IM)
# ## Load the gray images as numpy array
    filename_Gray_IM =projectpath+'io/Output/GRAY_IM.npy'
    GRAY_IM_parallel=np.load(filename_Gray_IM)


    nb_features=2919

    partial_get_FEATURES = partial(FC.Features_calcul_np_GrayscaleIm_WND, nb_features=nb_features, w=weight, h=height, GRAY=GRAY_IM_parallel)

    pool = multiprocessing.Pool(27)
    Featur = pool.map(partial_get_FEATURES,xrange(nidx))
    pool.close()
 

    filename_FEATURES =projectpath+'io/Output/FEATURES.npy'
    np.save(filename_FEATURES,Featur)
# 

# ## Load the extracted Features
    FEATURES=np.load(filename_FEATURES)


# ## Etablish one np.array for the Features' Names & another one for Features' Values

    FEAT_NAMES=FEATURES[:,1,:]
    FEAT_VALUES=FEATURES[:,0,:]
    FEAT_VALUES=FEAT_VALUES.astype(float)
    filename_FEATURES_Val =projectpath+'io/Output/FEATURES_Val.npy'
    np.save(filename_FEATURES_Val,FEAT_VALUES)
    FEAT_VALUES=np.load(filename_FEATURES_Val)


    # # 4.3- Features Post- processing

    # ## A- Get the normalized Features

    partial_get_NORMALIZED_FEAT = partial(FC.Get_Normalized_FEATURES, FV=FEAT_VALUES)

    # get raw data using multiprocesses
    pool = multiprocessing.Pool(27)
    FV_N = pool.map(partial_get_NORMALIZED_FEAT,xrange(nidx))
    pool.close()
    
    filename_FVN =projectpath+'io/Output/FV_N.npy'
    np.save(filename_FVN,FV_N)
    FV_N=np.load(filename_FVN)
    
    return(FV_N, Data_FRAMES)