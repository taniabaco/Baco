
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



################ Nouvelle fonction incluant les images autour du point anote manuellement

def NEW_get_mean_zstacks_data( index,imageId,zsize,h,w,Data_F):

        
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
    
    # left up
    x_l_u=x-w/2
    y_l_u=y-h/2
    
    xtiles_l_u = np.ones(zsize,dtype=int)*x_l_u
    ytiles_l_u = np.ones(zsize,dtype=int)*y_l_u
    tilewidths_l_u = np.ones(zsize,dtype=int)*w
    tileheights_l_u = np.ones(zsize,dtype=int)*h
    tilestacks_l_u = zip(xtiles_l_u,ytiles_l_u,tilewidths_l_u,tileheights_l_u)
    zstacks_l_u=np.tile(np.arange(z-zsize/2,z+zsize/2+1),3)
    tstacks_l_u=np.zeros(zsize, dtype=int)
    # right up
    x_r_u=x+w/2
    y_r_u=y-h/2
    
    xtiles_r_u = np.ones(zsize,dtype=int)*x_r_u
    ytiles_r_u = np.ones(zsize,dtype=int)*y_r_u
    tilewidths_r_u = np.ones(zsize,dtype=int)*w
    tileheights_r_u = np.ones(zsize,dtype=int)*h
    tilestacks_r_u = zip(xtiles_r_u,ytiles_r_u,tilewidths_r_u,tileheights_r_u)
    zstacks_r_u=np.tile(np.arange(z-zsize/2,z+zsize/2+1),3)
    tstacks_r_u=np.zeros(zsize, dtype=int)
    # left down
    x_l_d=x-w/2
    y_l_d=y+h/2
    
    xtiles_l_d = np.ones(zsize,dtype=int)*x_l_d
    ytiles_l_d = np.ones(zsize,dtype=int)*y_l_d
    tilewidths_l_d = np.ones(zsize,dtype=int)*w
    tileheights_l_d = np.ones(zsize,dtype=int)*h
    tilestacks_l_d = zip(xtiles_l_d,ytiles_l_d,tilewidths_l_d,tileheights_l_d)
    zstacks_l_d=np.tile(np.arange(z-zsize/2,z+zsize/2+1),3)
    tstacks_l_d=np.zeros(zsize, dtype=int)
    # right down
    x_r_d=x+w/2
    y_r_d=y+h/2
    
    xtiles_r_d = np.ones(zsize,dtype=int)*x_r_d
    ytiles_r_d = np.ones(zsize,dtype=int)*y_r_d
    tilewidths_r_d = np.ones(zsize,dtype=int)*w
    tileheights_r_d = np.ones(zsize,dtype=int)*h
    tilestacks_r_d = zip(xtiles_r_d,ytiles_r_d,tilewidths_r_d,tileheights_r_d)
    zstacks_r_d=np.tile(np.arange(z-zsize/2,z+zsize/2+1),3)
    tstacks_r_d=np.zeros(zsize, dtype=int)
    
    
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste=zip(zstacks,cstacks,tstacks, tilestacks)
        pxobj = pixels.getTiles(liste)
        for i, p in enumerate(pxobj):
            Matrix[i,:,:,c]=p
            Norm_Matrix=(Matrix-np.min(Matrix))*1.0/(np.max(Matrix)-np.min(Matrix))
    M_mean=np.mean(Norm_Matrix, axis=0)
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste_l_u=zip(zstacks_l_u,cstacks,tstacks_l_u, tilestacks_l_u)
        pxobj_l_u = pixels.getTiles(liste_l_u)
        for i, p in enumerate(pxobj_l_u):
            Matrix_l_u[i,:,:,c]=p
            Norm_Matrix_l_u=(Matrix_l_u-np.min(Matrix_l_u))*1.0/(np.max(Matrix_l_u)-np.min(Matrix_l_u))
    M_mean_l_u=np.mean(Norm_Matrix_l_u, axis=0)
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste_r_u=zip(zstacks_r_u,cstacks,tstacks_r_u, tilestacks_r_u)
        pxobj_r_u = pixels.getTiles(liste_r_u)
        for i, p in enumerate(pxobj_r_u):
            Matrix_r_u[i,:,:,c]=p
            Norm_Matrix_r_u=(Matrix_r_u-np.min(Matrix_r_u))*1.0/(np.max(Matrix_r_u)-np.min(Matrix_r_u))
    M_mean_r_u=np.mean(Norm_Matrix_r_u, axis=0)
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste_l_d=zip(zstacks_l_d,cstacks,tstacks_l_d, tilestacks_l_d)
        pxobj_l_d = pixels.getTiles(liste_l_d)
        for i, p in enumerate(pxobj_l_d):
            Matrix_l_d[i,:,:,c]=p
            Norm_Matrix_l_d=(Matrix_l_d-np.min(Matrix_l_d))*1.0/(np.max(Matrix_l_d)-np.min(Matrix_l_d))
    M_mean_l_d=np.mean(Norm_Matrix_l_d, axis=0)
    
    for c in range(0,3):
        cstacks=np.ones(zsize, dtype=int)*c
        liste_r_d=zip(zstacks_r_d,cstacks,tstacks_r_d, tilestacks_r_d)
        pxobj_r_d = pixels.getTiles(liste_r_d)
        for i, p in enumerate(pxobj_r_d):
            Matrix_r_d[i,:,:,c]=p
            Norm_Matrix_r_d=(Matrix_r_d-np.min(Matrix_r_d))*1.0/(np.max(Matrix_r_d)-np.min(Matrix_r_d))
    M_mean_r_d=np.mean(Norm_Matrix_r_d, axis=0)
    
    conn._closeSession()
    
    return(M_mean, M_mean_l_u,M_mean_r_u, M_mean_l_d, M_mean_r_d)

