
# coding: utf-8

import numpy as np
import pandas as pd
from skimage.io import imshow, imsave
from skimage.color import rgb2gray



def Convert_Im_in_Gray_levels(ind,h,w, M_mean):
    img=np.empty([h,w,3])
    GRAY_IM=np.empty([h,w])
    img=M_mean[:,:,:][ind]
    for d, label in enumerate( ('r', 'g', 'b')):
        plane = img[:,:,d]
    gray_img = rgb2gray(img)
    gray_img = (gray_img * 255 ).astype( np.uint8 )
    GRAY_IM[:,:]=gray_img-np.mean(gray_img)
    GRAY_IM
    return(GRAY_IM)




