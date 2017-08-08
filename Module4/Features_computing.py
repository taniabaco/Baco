
# coding: utf-8

import pandas as pd
import numpy as np


from wndcharm.PyImageMatrix import PyImageMatrix
from wndcharm.FeatureVector import FeatureVector
import time



def Features_calcul_np_GrayscaleIm_WND(ind,nb_features,w, h, GRAY):
    " calculate WND Charm Features from grayscale images (2919 features)"
    FV=np.empty([nb_features])
    matrix = PyImageMatrix()
    matrix.allocate(h, w)
    numpy_matrix = matrix.as_ndarray()
    numpy_matrix[:] = GRAY[:,:][ind]
    fv = FeatureVector( name='stufff', long=True, original_px_plane=matrix )
    t1 = time.time()
    fv.GenerateFeatures(quiet=True, write_to_disk=False)
    t2 = time.time()
    
    FV[:]=fv.values
    Names=fv.feature_names
    FV
    return(FV,Names)


def Get_Normalized_FEATURES(ind, FV):
    " normalization of the extracted features"
    FEAT=FV[ind]
    mean=FEAT.mean(axis=0)
    stdv=FEAT.std(axis=0)
    FV_Normalized=(FEAT-mean)/stdv
    return(FV_Normalized)  

