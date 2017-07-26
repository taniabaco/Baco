
# coding: utf-8

# # Display the images corresponding to normalized volums

import matplotlib 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as cm


def PLOT_Im(normalized_vol):
    plt.subplot(221)
    CH1=normalized_vol[:,:,0]
    plt.title('CH1: Background')
    plt.imshow(CH1,cmap='gray')

    plt.subplot(222)
    CH2=normalized_vol[:,:,1]
    plt.title('CH2: Background')
    plt.imshow(CH2,cmap='gray')

    plt.subplot(223)
    CH3=normalized_vol[:,:,2]
    plt.title('CH3: Background')
    plt.imshow(CH3,cmap='gray')

    VolCH1=normalized_vol[:,:,:]
    plt.figure(figsize=(3,3))
    plt.title('RGB: Background')
    plt.imshow(VolCH1)


