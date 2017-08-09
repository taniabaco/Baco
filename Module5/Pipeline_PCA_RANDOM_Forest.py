
# coding: utf-8


from sklearn.pipeline import Pipeline
from sklearn import decomposition
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets, linear_model, cross_validation, grid_search
from sklearn.metrics import confusion_matrix
import seaborn as sns

from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import pandas as pd

def Get_true_y(DF):
    " Get the real class "
    y=np.zeros([DF.shape[0]])
    for j in range(0,DF.shape[0]):
        if (DF.TYPE[j]==1):
            y[j]=1
        elif (DF.TYPE[j]==2):
            y[j]=2
        else :
            y[j]=3
        yr=(y.reshape(-1,1)).ravel() 
            #yr = yr.ravel()   
    return(yr)

def classification(FV_N):
    " PCA reduction dimension & Random Forest Classification"

    pca = decomposition.PCA()
    RFC= RandomForestClassifier()

    estimators = [('reduce_dim', pca), ('Random_Forest', RFC)]
    pipe = Pipeline(estimators)


# Search the best parameters for the classification
    #for i in range(100,700,100):
    #    cc=[i]+cc
    #nb_tree=[]
    #random_st=[]
    #for i in range(50,350,50):
    #    nb_tree=[i]+nb_tree
    #    random_st=[0]+random_st

    cc=[70, 80, 90]
    nb_tree=[200, 200, 200]
    random_st=[0, 0, 0]

    aa=[100, 200, 300]
    cc=[]

    params = dict(reduce_dim__n_components=cc,
              Random_Forest__n_estimators=nb_tree,Random_Forest__random_state=random_st)



    grid_search = GridSearchCV(pipe, param_grid=params)


    X=FV_N


    yr=Get_true_y(Data_FRAMES)



    filename_yr =projectpath+'io/Output/yr.npy'

    np.save(filename_yr, yr)

    yr=np.load(filename_yr)


    Data_FRAMES.loc[Data_FRAMES.indice==1595]


    X=X[:yr.shape[0]]
    X.shape
    yr=yr[:X.shape[0]]
    np.save(filename_yr, yr)

    yr=np.load(filename_yr)

    grid_search.fit(X, yr)

    print(grid_search.best_estimator_)

    plt.figure()
    plt.axvline(grid_search.best_estimator_.named_steps['reduce_dim'].n_components,
                linestyle=':', label='n_components chosen')
    plt.legend(prop=dict(size=12))
    plt.show()


    plt.figure()
    plt.axvline(grid_search.best_estimator_.named_steps['Random_Forest'].n_estimators,
                linestyle=':', label='n_estimators chosen')
    plt.legend(prop=dict(size=12))
    plt.show()


    n_est_rdf=grid_search.best_estimator_.named_steps['Random_Forest'].n_estimators

    n_compo_pca=grid_search.best_estimator_.named_steps['reduce_dim'].n_components


    pca=decomposition.PCA(n_components=n_compo_pca, svd_solver='auto')
    pca.fit(X)

    variance_Ratio=pca.explained_variance_ratio_

    plt.figure(1, figsize=(4, 3))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    plt.plot(pca.explained_variance_ratio_.cumsum(), linewidth=1)
    plt.axis('tight')
    plt.xlabel('n_components')
    plt.ylabel('Cumulative Explained variance')

    M = pca.transform(X)

    plt.figure()
    plt.plot(M[yr==1,0],M[yr==1,1],'or')
    plt.title('Astrocytes')
    plt.figure()
    plt.plot(M[yr==2,0],M[yr==2,1],'ob')
    plt.title('Neurons')


    grid_search.predict(X)


    metrics.accuracy_score(yr, grid_search.predict(X))


    RFC=RandomForestClassifier(n_estimators=n_est_rdf, random_state=0)


    predictedVAL = cross_val_predict(RFC, X, yr , n_jobs =-1)


    metrics.accuracy_score(yr, predictedVAL) 


    Conf_Mat=confusion_matrix(yr, predictedVAL)

    import seaborn as sns
    sns.heatmap(Conf_Mat.T, square=True, annot=True, cbar=False)
    plt.xlabel('True label')
    plt.ylabel('predicted label');
    
    return()


