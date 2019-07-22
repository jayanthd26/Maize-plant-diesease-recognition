# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 23:29:28 2019

@author: Nanda Krishna K S
"""

from sklearn.externals import joblib
import pandas as pd
import numpy as np

result=0
def predict(year,sea,ar):
    sea='Kharif     '
    year=int(year)
    ar=int(ar)
    print(ar)
    #sample=[1997, 'Kharif     ', 20029 ]
    sample=[year, sea, int(ar) ]
    print(sample)
    sample.append(65080.0)
    test=np.array(pd.DataFrame(sample).values.reshape(1,4))

    labelencoder_X=joblib.load('LabelEncoderYieldPredictor')
    test[:,1]=labelencoder_X.transform(test[:,1])

    onehotencoder=joblib.load('OneHotEncoderPredictor')
    test=onehotencoder.transform(test).toarray()

    sc=joblib.load('SCPredictor')
    test=sc.transform(test)

    test=test[:,:-1]

    regressor=joblib.load('RegressorPredictor')
    res=regressor.predict(test)

    np.append(test,res)
    return (sc.inverse_transform(np.append(test,res))[-1])
