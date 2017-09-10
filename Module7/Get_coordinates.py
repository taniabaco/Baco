
# coding: utf-8

import numpy as np
import pandas as pd
import omero
from omero.gateway import BlitzGateway


def get_coordinates(index_ligne,imageId, large, delta_x,z):
    conn = BlitzGateway('tbacoyannis','d33pl34rn1ng',port=4064,host='chinensis.polytechnique.fr')
    connected = conn.connect()

    image = conn.getObject("Image", imageId)
    pixels = image.getPrimaryPixels() # get raw pixels information
    
    size_x= image.getSizeX()
    size_y= image.getSizeY()
    size_z = image.getSizeZ()
    size_c = image.getSizeC()
    size_t = image.getSizeT()
   
   
    
    nb_fenetres=np.arange(size_x/delta_x)
    index=nb_fenetres
    
    x=(index*delta_x)+delta_x
    #x=x[22:-22]
    
    y=((index_ligne*delta_x)+delta_x)*np.ones(len(x)) #(index))
    
    index_colonne=index+2
    index_lignee=(2+index_ligne)*np.ones(len(x)) 
    
    Tuple_Coord=(x,y,index_lignee, index_colonne) 
    
    Matrix=np.zeros((len(x),large,large,3))
       
    tilewidths = np.ones(len(x),dtype=int)*large
    tileheights = tilewidths
    tilestacks = zip(x,y,tilewidths,tileheights)
    
    zstacks= np.ones(len(x),dtype=int)*z
    
    tstacks=np.zeros(len(x), dtype=int)
    
    for c in range(0,3):
        cstacks=np.ones(len(x), dtype=int)*c
        liste=zip(zstacks,cstacks,tstacks, tilestacks)
        pxobj = pixels.getTiles(liste)
        for i, p in enumerate(pxobj):
            Matrix[i,:,:,c]=p
    
    conn._closeSession()
    return(Matrix,Tuple_Coord)


def get_coordinates_list(index_ligne,imageId, large, delta_x,z):
    conn = BlitzGateway('tbacoyannis','d33pl34rn1ng',port=4064,host='chinensis.polytechnique.fr')
    connected = conn.connect()

    image = conn.getObject("Image", imageId)
    pixels = image.getPrimaryPixels() # get raw pixels information
    
    size_x= image.getSizeX()
    size_y= image.getSizeY()
    size_z = image.getSizeZ()
    size_c = image.getSizeC()
    size_t = image.getSizeT()
   
   
    
    nb_fenetres=np.arange(size_x/delta_x)
    index=nb_fenetres
    
    x=(index*delta_x)+delta_x
    #x=x[22:-22]
    
    y=((index_ligne*delta_x)+delta_x)*np.ones(len(x)) #(index))
    
    index_colonne=index+2
    index_lignee=(2+index_ligne)*np.ones(len(x)) 
    
    Tuple_Coord=(x,y,index_lignee, index_colonne) 
    
    conn._closeSession()
    return(Tuple_Coord)



def get_coordinates_test(index_ligne,imageId, large, delta_x,z,x_min,y_min,x_max, y_max):
   
    
    
    conn = BlitzGateway('tbacoyannis','d33pl34rn1ng',port=4064,host='chinensis.polytechnique.fr')
    connected = conn.connect()
   
    image = conn.getObject("Image", imageId)
    pixels = image.getPrimaryPixels() # get raw pixels information

    
    
    size_x= x_max-x_min
    size_y= y_max-y_min
    size_z = 3
    size_c = 3
    size_t = image.getSizeT()
   
   
    
    nb_fenetres=np.arange(size_x/delta_x)
    index=nb_fenetres
    
    x=(index*delta_x)+delta_x+x_min
    #x=x[22:-22]
    
    y=((index_ligne*delta_x)+delta_x+y_min)*np.ones(len(x)) #(index))
    
    index_colonne=index+2
    index_lignee=(2+index_ligne)*np.ones(len(x)) 
    
    Tuple_Coord=(x,y,index_lignee, index_colonne) 
    
    Matrix=np.zeros((len(x),large,large,3))
       
    tilewidths = np.ones(len(x),dtype=int)*large
    tileheights = tilewidths
    tilestacks = zip(x,y,tilewidths,tileheights)
    
    zstacks= np.ones(len(x),dtype=int)*z
    
    tstacks=np.zeros(len(x), dtype=int)
    
    for c in range(0,3):
        cstacks=np.ones(len(x), dtype=int)*c
        liste=zip(zstacks,cstacks,tstacks, tilestacks)
        pxobj = pixels.getTiles(liste)
        for i, p in enumerate(pxobj):
            Matrix[i,:,:,c]=p
    
    conn._closeSession()
    return(Matrix,Tuple_Coord)