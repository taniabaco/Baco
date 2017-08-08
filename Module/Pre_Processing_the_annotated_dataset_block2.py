
# coding: utf-8


import numpy as np
import pandas as pd


def Get_Real_coordinates_Dataframe(Data_frame):
    " the function is rectifying the real coordinates values corresponding to Omero pixels coordinates"
    Data_frame_N=Data_frame.copy()
    for i in range(0,Data_frame.shape[0]):
        Data_frame_N.X[i]=Data_frame.X[i]+60
        Data_frame_N.Y[i]=Data_frame.Y[i]+54
    return(Data_frame_N)
    