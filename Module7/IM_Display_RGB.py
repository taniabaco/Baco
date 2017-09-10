
# coding: utf-8

import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
import numpy as np


def imshowRGB(IM,original_Im,s):
    
    def imshowsim(IM,original_Im,s,color):
        fig = plt.subplots(figsize=(s, s))

        if color=='RGB':
            plt.title('Original image')
            plt.imshow(original_Im[:,:],cmap='spectral')
            plt.colorbar()
        elif color=='RGB2':
            plt.title('Proba image')
            plt.imshow(IM[:,:,:],cmap='spectral')
            plt.colorbar()
        elif color=='Red':
            plt.title('Image of Proba Astrocytes ')
            plt.imshow(IM[:,:,0],cmap='Reds')
            plt.colorbar()
        elif color=='Green':
            plt.title('Image of Proba Neurons ')
            plt.imshow(IM[:,:,1],cmap='Greens')
            plt.colorbar()
        else:
            plt.title('Image of Proba Background ')
            plt.imshow(IM[:,:,2],cmap='Blues')
            plt.colorbar()

    interact(imshowsim, IM=fixed(IM),original_Im=fixed(original_Im),s=fixed(s), color=['RGB','RGB2','Red','Green','Blue'])




