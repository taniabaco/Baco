
# coding: utf-8



import numpy as np
import pandas as pd
import pickle



def Get_Df_with_backgroung_class(Data_FRAMES,imageId):
    

#Data_FRAMES=pd.read_pickle(projectpath+'io/Output/Data_FRAMES.pkl')


# create a dataframe (size= number of ROI manually annotated from Fiji)

    datafr=np.zeros([18])
    datafr=pd.DataFrame(data=datafr)


    # In[7]:

    ROI_nb=np.zeros(datafr.shape[0])
    ROI_nb=ROI_nb.reshape(-1,1)
    x=ROI_nb
    id_IMG=ROI_nb
    y=ROI_nb
    h=ROI_nb
    w=ROI_nb
    theZ=ROI_nb
    theT=ROI_nb


    # In[8]:

    datafr['id']=id_IMG 
    datafr['ROI_nb']=ROI_nb
    datafr['x']=x
    datafr['y']=y
    datafr['h']=h
    datafr['w']=w
    datafr['theZ']=theZ
    datafr['theT']=theT
    Background_DF=datafr.copy()




# Manually anotated ROIs (rectangles shapes) of background
    Background_DF.id[0]=451
    Background_DF.ROI_nb[0]=1
    Background_DF.x[0]=664
    Background_DF.y[0]=912
    Background_DF.theZ[0]=155
    Background_DF.w[0]=672
    Background_DF.h[0]=352

    Background_DF.id[1]=451
    Background_DF.ROI_nb[1]=2
    Background_DF.x[1]=1136
    Background_DF.y[1]=296
    Background_DF.theZ[1]=155
    Background_DF.w[1]=640
    Background_DF.h[1]=448

    Background_DF.id[ 2]=451
    Background_DF.ROI_nb[ 2]=3
    Background_DF.x[ 2]=1960
    Background_DF.y[ 2]=2756
    Background_DF.theZ[2 ]=158
    Background_DF.w[ 2]=344
    Background_DF.h[ 2]=128

    Background_DF.id[ 3]=451
    Background_DF.ROI_nb[ 3]=4
    Background_DF.x[3 ]=624
    Background_DF.y[ 3]=2020
    Background_DF.theZ[ 3]=158
    Background_DF.w[3]=268
    Background_DF.h[ 3]=216

    Background_DF.id[ 4]=451
    Background_DF.ROI_nb[ 4]=5
    Background_DF.x[4 ]=2044
    Background_DF.y[ 4]=2352
    Background_DF.theZ[4 ]=41
    Background_DF.w[4 ]=352
    Background_DF.h[ 4]=376

    Background_DF.id[ 5]=451
    Background_DF.ROI_nb[5 ]=6
    Background_DF.x[5 ]=1692
    Background_DF.y[ 5]=2088
    Background_DF.theZ[5 ]=45
    Background_DF.w[5 ]=609
    Background_DF.h[5 ]=336

    Background_DF.id[6 ]=451
    Background_DF.ROI_nb[6 ]=7
    Background_DF.x[6 ]=261
    Background_DF.y[ 6]=414
    Background_DF.theZ[6 ]=45
    Background_DF.w[6 ]=534
    Background_DF.h[6 ]=486

    Background_DF.id[7 ]=451
    Background_DF.ROI_nb[ 7]=8
    Background_DF.x[7 ]=654
    Background_DF.y[ 7]=3294
    Background_DF.theZ[ 7]=201
    Background_DF.w[7 ]=402
    Background_DF.h[ 7]=357

    Background_DF.id[8 ]=451
    Background_DF.ROI_nb[8 ]=9
    Background_DF.x[ 8]=732
    Background_DF.y[ 8]=1185
    Background_DF.theZ[8 ]=201
    Background_DF.w[8 ]=378
    Background_DF.h[ 8]=207

    Background_DF.id[ 9]=451
    Background_DF.ROI_nb[ 9]=10
    Background_DF.x[ 9]=36
    Background_DF.y[9 ]=2124
    Background_DF.theZ[9 ]=201
    Background_DF.w[ 9]=303
    Background_DF.h[9 ]=564

    Background_DF.id[ 10]=451
    Background_DF.ROI_nb[ 10]=11
    Background_DF.x[10 ]=835
    Background_DF.y[10 ]=2421
    Background_DF.theZ[ 10]=279
    Background_DF.w[10 ]=333
    Background_DF.h[10]=366

    Background_DF.id[11]=451
    Background_DF.ROI_nb[11 ]=12
    Background_DF.x[11 ]=334
    Background_DF.y[11]=3306
    Background_DF.theZ[11 ]=279
    Background_DF.w[11 ]=642
    Background_DF.h[11 ]=315

    Background_DF.id[12]=451
    Background_DF.ROI_nb[ 12]=13
    Background_DF.x[ 12]=595
    Background_DF.y[ 12]=3396
    Background_DF.theZ[12 ]=276
    Background_DF.w[12]=459
    Background_DF.h[12]=225

    Background_DF.id[13]=451
    Background_DF.ROI_nb[13]=14
    Background_DF.x[13]=853
    Background_DF.y[13]=2457
    Background_DF.theZ[13]=276
    Background_DF.w[13]=321
    Background_DF.h[13]=255

    Background_DF.id[14]=451
    Background_DF.ROI_nb[14]=15
    Background_DF.x[14]=367
    Background_DF.y[14]=2727
    Background_DF.theZ[14]=276
    Background_DF.w[14]=255
    Background_DF.h[14]=288

    Background_DF.id[15]=451
    Background_DF.ROI_nb[15]=16
    Background_DF.x[15]=1708
    Background_DF.y[15]=3135
    Background_DF.theZ[15]=276
    Background_DF.w[15]=189
    Background_DF.h[15]=156

    Background_DF.id[16]=451
    Background_DF.ROI_nb[16]=17
    Background_DF.x[16]=2506
    Background_DF.y[16]=2964
    Background_DF.theZ[16]=276
    Background_DF.w[16]=381
    Background_DF.h[16]=279




# choose randomly 31 points in each ROI 
    xx=np.ones([Background_DF.shape[0]-1,31],dtype=int)
    yy=np.ones([Background_DF.shape[0]-1,31],dtype=int)
    zz=np.ones([Background_DF.shape[0]-1,31],dtype=int)

    for i in range(0,Background_DF.shape[0]-1):
        xx[i,:]=np.random.randint(int(Background_DF.x[i]), int(Background_DF.w[i])+int(Background_DF.x[i]), size=31)
        yy[i,:]=np.random.randint(int(Background_DF.y[i]), int(Background_DF.h[i])+int(Background_DF.y[i]), size=31)  
        zz[i,:]=np.ones([31])*(int(Background_DF.theZ[i]))

    xx=np.reshape(xx, xx.shape[0]*xx.shape[1])
    yy=np.reshape(yy, yy.shape[0]*yy.shape[1])
    zz=np.reshape(zz, zz.shape[0]*zz.shape[1])


#

    new_Background_DF_Shape0=(Background_DF.shape[0]+xx.shape[0])
    Background_DF_new=np.zeros([new_Background_DF_Shape0,Background_DF.shape[1]])


# 


    for i in range(0,Background_DF.shape[0]):
        Background_DF_new[i,:]=Background_DF.iloc[i,:].copy()

    for k in range(0,xx.shape[0]):
        Background_DF_new[k+Background_DF.shape[0],3]=xx[k]
        Background_DF_new[k+Background_DF.shape[0],4]=yy[k]
        Background_DF_new[k+Background_DF.shape[0],7]=zz[k]
        Background_DF_new[k+Background_DF.shape[0],1]=imageId


# The dataframe with only background has been created

    df_Background_DF_new=pd.DataFrame(data=Background_DF_new)


# Let's transform it in order to have the sames column name as the Data Frame containing Neurons and Astrocytes

    columns_names = list(Data_FRAMES.columns.values)
    New_DF=np.zeros([df_Background_DF_new.shape[0],len(columns_names)])
    New_DF=pd.DataFrame(data=New_DF,columns= Data_FRAMES.columns)

    New_DF['X']=df_Background_DF_new.loc[:,3].copy()
    New_DF['Y']=df_Background_DF_new.loc[:,4].copy()
    New_DF['Pos']=df_Background_DF_new.loc[:,7].copy()
    New_DF['Height']=df_Background_DF_new.loc[:,5].copy()
    New_DF['Width']=df_Background_DF_new.loc[:,6].copy()
    New_DF['TYPE']=3.0
    New_DF['ID_Image']=imageId
    
    New_DF=New_DF.loc[New_DF.indice!=17].copy() #exclusion because all the line has values 0


    return(New_DF)



def Get_Df_with_backgroung_class_Im2(Data_FRAMES,imageId):
    

#Data_FRAMES=pd.read_pickle(projectpath+'io/Output/Data_FRAMES.pkl')


# create a dataframe (size= number of ROI manually annotated from Fiji)

    datafr=np.zeros([18])
    datafr=pd.DataFrame(data=datafr)


    # In[7]:

    ROI_nb=np.zeros(datafr.shape[0])
    ROI_nb=ROI_nb.reshape(-1,1)
    x=ROI_nb
    id_IMG=ROI_nb
    y=ROI_nb
    h=ROI_nb
    w=ROI_nb
    theZ=ROI_nb
    theT=ROI_nb


    # In[8]:

    datafr['id']=id_IMG 
    datafr['ROI_nb']=ROI_nb
    datafr['x']=x
    datafr['y']=y
    datafr['h']=h
    datafr['w']=w
    datafr['theZ']=theZ
    datafr['theT']=theT
    Background_DF=datafr.copy()




# Manually anotated ROIs (rectangles shapes) of background
    Background_DF.id[0]=imageId #462
    Background_DF.ROI_nb[0]=1
    Background_DF.x[0]=1296
    Background_DF.y[0]=3338
    Background_DF.theZ[0]=35
    Background_DF.w[0]=188
    Background_DF.h[0]=336

    Background_DF.id[1]=imageId
    Background_DF.ROI_nb[1]=2
    Background_DF.x[1]=620
    Background_DF.y[1]=3182
    Background_DF.theZ[1]=35
    Background_DF.w[1]=400
    Background_DF.h[1]=228

    Background_DF.id[ 2]=imageId
    Background_DF.ROI_nb[ 2]=3
    Background_DF.x[ 2]=1252
    Background_DF.y[ 2]=2014
    Background_DF.theZ[2 ]=35
    Background_DF.w[ 2]=392
    Background_DF.h[ 2]=188

    Background_DF.id[ 3]=imageId
    Background_DF.ROI_nb[ 3]=4
    Background_DF.x[3 ]=908
    Background_DF.y[ 3]=3638
    Background_DF.theZ[ 3]=35
    Background_DF.w[3]=192
    Background_DF.h[ 3]=132

    Background_DF.id[ 4]=imageId
    Background_DF.ROI_nb[ 4]=5
    Background_DF.x[4 ]=1876
    Background_DF.y[ 4]=1646
    Background_DF.theZ[4 ]=35
    Background_DF.w[4 ]=156
    Background_DF.h[ 4]=108

    Background_DF.id[ 5]=imageId
    Background_DF.ROI_nb[5 ]=6
    Background_DF.x[5 ]=632
    Background_DF.y[ 5]=3754
    Background_DF.theZ[5 ]=35
    Background_DF.w[5 ]=96
    Background_DF.h[5 ]=128

    Background_DF.id[6 ]=imageId
    Background_DF.ROI_nb[6 ]=7
    Background_DF.x[6 ]=1068
    Background_DF.y[ 6]=1766
    Background_DF.theZ[6 ]=85
    Background_DF.w[6 ]=236
    Background_DF.h[6 ]=232

    Background_DF.id[7 ]=imageId
    Background_DF.ROI_nb[ 7]=8
    Background_DF.x[7 ]=352
    Background_DF.y[ 7]=3246
    Background_DF.theZ[ 7]=85
    Background_DF.w[7 ]=448
    Background_DF.h[ 7]=224

    Background_DF.id[8 ]=imageId
    Background_DF.ROI_nb[8 ]=9
    Background_DF.x[ 8]=852
    Background_DF.y[ 8]=1530
    Background_DF.theZ[8 ]=85
    Background_DF.w[8 ]=228
    Background_DF.h[ 8]=228

    Background_DF.id[ 9]=imageId
    Background_DF.ROI_nb[ 9]=10
    Background_DF.x[ 9]=2508
    Background_DF.y[9 ]=3134
    Background_DF.theZ[9 ]=158
    Background_DF.w[ 9]=156
    Background_DF.h[9 ]=224

    Background_DF.id[ 10]=imageId
    Background_DF.ROI_nb[ 10]=11
    Background_DF.x[10 ]=2348
    Background_DF.y[10 ]=2690
    Background_DF.theZ[ 10]=158
    Background_DF.w[10 ]=152
    Background_DF.h[10]=280

    Background_DF.id[11]=imageId
    Background_DF.ROI_nb[11 ]=12
    Background_DF.x[11 ]=104
    Background_DF.y[11]=3310
    Background_DF.theZ[11 ]=231
    Background_DF.w[11 ]=192
    Background_DF.h[11 ]=360

    Background_DF.id[12]=imageId
    Background_DF.ROI_nb[ 12]=13
    Background_DF.x[ 12]=948
    Background_DF.y[ 12]=1880
    Background_DF.theZ[12 ]=231
    Background_DF.w[12]=544
    Background_DF.h[12]=380

    Background_DF.id[13]=imageId
    Background_DF.ROI_nb[13]=14
    Background_DF.x[13]=752
    Background_DF.y[13]=3740
    Background_DF.theZ[13]=231
    Background_DF.w[13]=168
    Background_DF.h[13]=264

    Background_DF.id[14]=imageId
    Background_DF.ROI_nb[14]=15
    Background_DF.x[14]=1120
    Background_DF.y[14]=3048
    Background_DF.theZ[14]=282
    Background_DF.w[14]=212
    Background_DF.h[14]=260

    Background_DF.id[15]=imageId
    Background_DF.ROI_nb[15]=16
    Background_DF.x[15]=240
    Background_DF.y[15]=3772
    Background_DF.theZ[15]=282
    Background_DF.w[15]=164
    Background_DF.h[15]=192

    Background_DF.id[16]=imageId
    Background_DF.ROI_nb[16]=17
    Background_DF.x[16]=2636
    Background_DF.y[16]=2744
    Background_DF.theZ[16]=308
    Background_DF.w[16]=172
    Background_DF.h[16]=268
    
    Background_DF.id[17]=imageId
    Background_DF.ROI_nb[17]=18
    Background_DF.x[17]=620
    Background_DF.y[17]=788
    Background_DF.theZ[17]=308
    Background_DF.w[17]=848
    Background_DF.h[17]=520

    Background_DF.id[18]=imageId
    Background_DF.ROI_nb[18]=19
    Background_DF.x[18]=2456
    Background_DF.y[18]=2100
    Background_DF.theZ[18]=308
    Background_DF.w[18]=144
    Background_DF.h[18]=180




# choose randomly 31 points in each ROI 
    xx=np.ones([Background_DF.shape[0]-1,35],dtype=int)
    yy=np.ones([Background_DF.shape[0]-1,35],dtype=int)
    zz=np.ones([Background_DF.shape[0]-1,35],dtype=int)

    for i in range(0,Background_DF.shape[0]-1):
        xx[i,:]=np.random.randint(int(Background_DF.x[i]), int(Background_DF.w[i])+int(Background_DF.x[i]), size=35)
        yy[i,:]=np.random.randint(int(Background_DF.y[i]), int(Background_DF.h[i])+int(Background_DF.y[i]), size=35)  
        zz[i,:]=np.ones([35])*(int(Background_DF.theZ[i]))

    xx=np.reshape(xx, xx.shape[0]*xx.shape[1])
    yy=np.reshape(yy, yy.shape[0]*yy.shape[1])
    zz=np.reshape(zz, zz.shape[0]*zz.shape[1])


#

    new_Background_DF_Shape0=(Background_DF.shape[0]+xx.shape[0])
    Background_DF_new=np.zeros([new_Background_DF_Shape0,Background_DF.shape[1]])


# 


    for i in range(0,Background_DF.shape[0]):
        Background_DF_new[i,:]=Background_DF.iloc[i,:].copy()

    for k in range(0,xx.shape[0]):
        Background_DF_new[k+Background_DF.shape[0],3]=xx[k]
        Background_DF_new[k+Background_DF.shape[0],4]=yy[k]
        Background_DF_new[k+Background_DF.shape[0],7]=zz[k]
        Background_DF_new[k+Background_DF.shape[0],1]=imageId


# The dataframe with only background has been created

    df_Background_DF_new=pd.DataFrame(data=Background_DF_new)


# Let's transform it in order to have the sames column name as the Data Frame containing Neurons and Astrocytes

    columns_names = list(Data_FRAMES.columns.values)
    New_DF=np.zeros([df_Background_DF_new.shape[0],len(columns_names)])
    New_DF=pd.DataFrame(data=New_DF,columns= Data_FRAMES.columns)

    New_DF['X']=df_Background_DF_new.loc[:,3].copy()
    New_DF['Y']=df_Background_DF_new.loc[:,4].copy()
    New_DF['Pos']=df_Background_DF_new.loc[:,7].copy()
    New_DF['Height']=df_Background_DF_new.loc[:,5].copy()
    New_DF['Width']=df_Background_DF_new.loc[:,6].copy()
    New_DF['TYPE']=3.0
    New_DF['ID_Image']=imageId
    
    New_DF=New_DF.loc[New_DF.indice!=19].copy() #exclusion because all the line has values 0


    return(New_DF)
