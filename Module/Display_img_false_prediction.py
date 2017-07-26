
# coding: utf-8

import numpy as np
import pandas as pd
from skimage.io import imshow, imsave
from skimage.color import rgb2gray
import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as cm

     
def Get_IMG_failed_prediction(Validation_label_,predictions_RFC):
    " to compute after prediction in order to visualize the failed predicted images by class"

    fail_img_pred_N=np.zeros(Validation_label_.shape[0])
    fail_img_pred_A=np.zeros(Validation_label_.shape[0])
    fail_img_pred_B=np.zeros(Validation_label_.shape[0])

    for t in range(0,Validation_label_.shape[0] ):
        if ((predictions_RFC[t]==1) & (Validation_label_[t]!=1)):
            fail_img_pred_A[t]=t

        if ((predictions_RFC[t]==2) & (Validation_label_[t]!=2)):
            fail_img_pred_N[t]=t
            
        if ((predictions_RFC[t]==3) & (Validation_label_[t]!=3)):
            fail_img_pred_B[t]=t      
        

    fail_img_pred_N=fail_img_pred_N[fail_img_pred_N!=0]
    fail_img_pred_A=fail_img_pred_A[fail_img_pred_A!=0]
    fail_img_pred_B=fail_img_pred_B[fail_img_pred_B!=0]

    return(fail_img_pred_N,fail_img_pred_A,fail_img_pred_B)


def separate_in_3_classes(Data_FRAMES):
    Astro=Data_FRAMES.loc[Data_FRAMES.TYPE==1].copy()
    Astro=Astro.indice
    Astro = np.asarray(Astro)

    Neuron=Data_FRAMES.loc[Data_FRAMES.TYPE==2].copy()
    Neuron=Neuron.indice
    Neuron = np.asarray(Neuron)

    Background=Data_FRAMES.loc[Data_FRAMES.TYPE==3].copy()
    Background=Background.indice
    Background = np.asarray(Background)
    return(Astro,Neuron, Background)


def Plot_IMG_By_Class(GRAY_IM, fail_IMG):
    fig = plt.figure(figsize=(12, 12))
    fig.subplots_adjust(hspace=0.3, wspace=0.2)
    for i in range(1,100 ): 
        plt.subplot(10, 10, i)
        plt.title(int(fail_IMG[i-1]))
        plt.imshow(GRAY_IM[int(fail_IMG[i-1])])
        
def Plot_Failed_IMG(GRAY_IM, fail_IMG):
    fig = plt.figure(figsize=(12, 12))
    fig.subplots_adjust(hspace=0.2, wspace=0.2)
    for i in range(1,20): 
        plt.subplot(5,4, i)
        plt.title(int(fail_IMG[i-1]))
        plt.imshow(GRAY_IM[int(fail_IMG[i-1])])
        
