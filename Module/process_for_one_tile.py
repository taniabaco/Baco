
# coding: utf-8


import numpy as np
import pandas as pd
from skimage.io import imshow, imsave
from skimage.color import rgb2gray

from sklearn.pipeline import Pipeline
from sklearn import decomposition
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets, linear_model, cross_validation, grid_search
from sklearn.metrics import confusion_matrix
import seaborn as sns
get_ipython().magic(u'matplotlib notebook')
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from wndcharm.PyImageMatrix import PyImageMatrix
from wndcharm.FeatureVector import FeatureVector
import time

import sys

projectpath='/home/tbacoyannis/Desktop/LOB/Pipeline/'

modulepath=projectpath+'src/Module'

if modulepath not in sys.path:
    sys.path.append(modulepath)
    
OmeroPath='/home/tbacoyannis/Desktop/LOB/OMERO.py-5.2.7-ice36-b40/lib/python/'

if OmeroPath not in sys.path:
    sys.path.append(OmeroPath)




def Get_true_y(DF):
    y=np.zeros([DF.shape[0]])
    for j in range(0,DF.shape[0]):
        if (DF.TYPE[j]==1):
            y[j]=1
        elif (DF.TYPE[j]==2):
            y[j]=2
        else :
            y[j]=3
        yr=(y.reshape(-1,1)).ravel() 
            #yr = yr.ravel()   
    return(yr)


def Get_proba(ind,h,w, M_mean,nb_features):
    img=np.empty([h,w,3])
    GRAY_IM=np.empty([h,w])
    img=M_mean[:,:,:][ind]
    
    gray_img = rgb2gray(img)
    gray_img = (gray_img * 255 ).astype( np.uint8 )
    GRAY_IM[:,:]=gray_img-np.mean(gray_img)
    GRAY_IM
    
    FV=np.empty([nb_features])
    matrix = PyImageMatrix()
    matrix.allocate(h, w)
    numpy_matrix = matrix.as_ndarray()
    numpy_matrix[:] = GRAY_IM[:,:]
    fv = FeatureVector( name='stufff', long=True, original_px_plane=matrix )
    t1 = time.time()
    fv.GenerateFeatures(quiet=True, write_to_disk=False)
    t2 = time.time()
    
    FV[:]=fv.values
    Names=fv.feature_names
    FV
    FV=FV.astype(float)
    
    pca = decomposition.PCA()
    RFC= RandomForestClassifier()

    estimators = [('reduce_dim', pca), ('Random_Forest', RFC)]
    pipe = Pipeline(estimators)
    
    params = dict(reduce_dim__n_components=90,Random_Forest__n_estimators=200,Random_Forest__random_state=0)
    
    
   
    filename_Features_two_blocs=projectpath+'io/Output/Features_two_blocs.npy'
    FV_N=np.load(filename_Features_two_blocs)
    X=FV_N  
    
    Data_FRAMES=pd.read_pickle(projectpath+'io/Output/Dataframe_.pkl')
    yr=Get_true_y(Data_FRAMES)
    
    filename_yr =projectpath+'io/Output/yr.npy'
    np.save(filename_yr, yr)
    yr=np.load(filename_yr)
  
    RFC=RandomForestClassifier(n_estimators=200, random_state=0)
    
    
    predictedVAL = cross_val_predict(RFC, X, yr , n_jobs =-1)
    metrics.accuracy_score(yr, predictedVAL) 
    Conf_Mat=confusion_matrix(yr, predictedVAL)

    
    RFC.fit(X, yr)
    
    predict_probab=np.ones([M_mean.shape[0],3])
    
    predict_proba=RFC.predict_proba(FV)
    
    predict_probab[ind,0]=predict_proba[:,0]
    predict_probab[ind,1]=predict_proba[:,1]
    predict_probab[ind,2]=predict_proba[:,2]
    
    return(predict_probab)



