
# coding: utf-8


import numpy as np
import pandas as pd


def Get_Clones(Data_frame):
    ROI_Index=np.arange(0,Data_frame.shape[0])
    ROI_Index=np.zeros(ROI_Index.shape[0])
    ROI_Index=ROI_Index.reshape(-1,1)
    
    for k in range(1,Data_frame.shape[0]) :
        if Data_frame.Name[k]=='r' :
            ROI_Index[k]=ROI_Index[k-1]+1
        else :
            ROI_Index[k]=ROI_Index[k-1]
        ROI_Index
    
    Data_frame['Clone']=ROI_Index
    np.concatenate((Data_frame,ROI_Index), axis=1)
    return(Data_frame)   



def Get_Type(Data_frame):
    index_Type=np.arange(0,Data_frame.shape[0])
    index_Type=np.zeros(index_Type.shape[0])
    index_Type=index_Type.reshape(-1,1)
    
    for l in range(0, dfpoints.shape[0]):
        if Data_frame.Name[l]=='m' :
            index_Type[l]=1
        elif Data_frame.Name[l]=='r':
            index_Type[l]=0
        else :
            index_Type[l]=2
        index_Type    
    
    Data_frame['TYPE']=index_Type
    np.concatenate((Data_frame,index_Type), axis=1)
    
    return(Data_frame)   


# In[5]:

#dfpoints=Get_Type(dfpoints)


# In[8]:

#dfpoints=dfpoints.loc[dfpoints.TYPE!=0].copy()


# In[18]:

# Reduire le nombre de neurones de la base de donnees
#data_Astrocytes=dfpoints.loc[dfpoints.TYPE==1.0].copy()
#data_Astrocytes.head()

#data_Neurons=dfpoints.loc[dfpoints.TYPE==2.0].copy()
#idx = np.random.randint(0,len(data_Neurons),size=(len(data_Astrocytes),))
#data_Neurons=data_Neurons.iloc[idx].copy()

#dfpoints= data_Neurons.append(data_Astrocytes).copy()


# In[59]:

## QUAND ON CONSIDERE AUSSI LES RECTANGLES

# # Reduire le nombre de neurones de la base de donnees
# data_Astrocytes=dfpoints.loc[dfpoints.TYPE==1.0].copy()
# data_Astrocytes.head()

# data_Neurons=dfpoints.loc[dfpoints.TYPE==2.0].copy()
# idx = np.random.randint(0,len(data_Neurons),size=(len(data_Astrocytes),))
# data_Neurons=data_Neurons.iloc[idx].copy()

# data_Rect=dfpoints.loc[dfpoints.TYPE==0.0].copy()

# dfpoints= data_Neurons.append(data_Astrocytes).copy()
# dfpoints= dfpoints.append(data_Rect).copy()


# In[ ]:




# # Get image Informations

# In[19]:

#get_ipython().magic(u'run ../Connection_to_server.ipynb')
#imageId = 451
#image = conn.getObject("Image", imageId)
#pixels = image.getPrimaryPixels() # get raw pixels information


# ## DATA FRAMES

# In[20]:

# Index Image's ID
def Get_Data_frame(imageId, Data_frame):
    D_Index=np.arange(0,Data_frame.shape[0])
    D_Index=np.ones(D_Index.shape[0])
    D_Index=imageId*D_Index.reshape(-1,1)
    Data_frame['ID_Image']=D_Index
    return(Data_frame)   


# In[24]:

def getDF(DF):
    D_Indexc=np.arange(0,DF.shape[0])
    D_Indexc=np.ones(D_Indexc.shape[0])
    D_Indexc=D_Indexc.reshape(-1,1)
    for i in range(0, DF.shape[0]):
        D_Indexc[i]=i*D_Indexc[i]
    D_Indexc
    DFS=DF
    DFS['indice']=D_Indexc
    return(DFS)


# ### Get Astrocytes' and Neurons' DF

# In[25]:

def Switch_Indices(DF):
    (DF.index)=(DF.indice)[:]
    return(DF)


# In[26]:

#DF_=Get_Data_frame(imageId, dfpoints)


# In[27]:

#Data_FRAMES=getDF(DF_)


# In[28]:

#Data_FRAMES=Switch_Indices(Data_FRAMES)


# ## Borders conditions to exclude data

# In[29]:

# Exclure les x et y negatifs sinon ca ne fonctionne pas!
def exclure(dfin,weight,height):
    a=dfin.loc[dfin.X>=(weight/2)]
    b=a.loc[a.Y!=2446] # POUR NOTRE CAS
    c=b.loc[b.Y>=(height/2)]
    d=c.loc[c.Y<=(max(c.Y)-height/2)]
    dfout=d.loc[d.X<=(max(d.X)-weight/2)]
    return(dfout)


# In[30]:

# Data_FRAMES=exclure(Data_FRAMES,50,50)


# In[ ]:

# TEST AVEC W=H=25
#Data_FRAMES=exclure(Data_FRAMES,25, 25)


# In[31]:

#D_F=getDF(Data_FRAMES)


# In[32]:

#Data_FRAMES=Switch_Indices(D_F)


# # Save the Data Frames 

# In[72]:

#import pickle
#import pandas as pd


# In[73]:

#Data_FRAMES.to_pickle(projectpath+'io/Output/Data_FRAMES.pkl')


# In[ ]:



