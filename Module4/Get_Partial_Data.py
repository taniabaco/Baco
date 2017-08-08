
# coding: utf-8



import numpy as np
import pandas as pd
import configure as cc
import omero
from omero.gateway import BlitzGateway


def get_mean_zstacks_data( index,imageId,zsize,h,w,Data_F):

        
    conn = BlitzGateway('tbacoyannis','d33pl34rn1ng',port=4064,host='chinensis.polytechnique.fr')
    connected = conn.connect()
    
    #imageId = 451
    image = conn.getObject("Image", imageId)
    pixels = image.getPrimaryPixels() # get raw pixels information
    
    Matrix=np.zeros((zsize,h,w,3))
   
    x=Data_F.iloc[index].X - w/2
    y=(Data_F.iloc[index].Y) - h/2
    z=(Data_F.iloc[index].Pos)
    
    xtiles = np.ones(zsize,dtype=int)*x
    ytiles = np.ones(zsize,dtype=int)*y
    tilewidths = np.ones(zsize,dtype=int)*w
    tileheights = np.ones(zsize,dtype=int)*h
    tilestacks = zip(xtiles,ytiles,tilewidths,tileheights)
    
    zstacks=np.tile(np.arange(z-zsize/2,z+zsize/2+1),3)
    
    tstacks=np.zeros(zsize, dtype=int)
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste=zip(zstacks,cstacks,tstacks, tilestacks)
        pxobj = pixels.getTiles(liste)
        for i, p in enumerate(pxobj):
            Matrix[i,:,:,c]=p
            Norm_Matrix=(Matrix-np.min(Matrix))*1.0/(np.max(Matrix)-np.min(Matrix))
    M_mean=np.mean(Norm_Matrix, axis=0)
    
    conn._closeSession()
    
    return(M_mean)





