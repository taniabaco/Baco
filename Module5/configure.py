
# coding: utf-8

# In[ ]:

import sys

def config():

    projectpath='/home/tbacoyannis/Desktop/LOB/Pipeline/'

    modulepath=projectpath+'src/Module'

    if modulepath not in sys.path:
        sys.path.append(modulepath)

    OmeroPath='/home/tbacoyannis/Desktop/LOB/OMERO.py-5.2.7-ice36-b40/lib/python/'

    if OmeroPath not in sys.path:
        sys.path.append(OmeroPath)

