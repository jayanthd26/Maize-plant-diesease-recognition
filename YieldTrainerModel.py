# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import numpy as np
from sklearn.externals import joblib

dataset=pd.read_csv("Mysuru_data.csv")
X=dataset.iloc[:,1:-1]
Y=dataset.iloc[:,-1]

data=[]
for i in range(831):
    if(X.iloc[i,-2]=="Maize"):
        data.append(dataset.iloc[i,:])
data=pd.DataFrame(data)
data = data.drop('Crop',axis=1)
data = data.drop('PLACE',axis=1)

data=np.array(data)

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
data[:,1]=labelencoder_X.fit_transform(data[:,1])
joblib.dump(labelencoder_X,'LabelEncoderYieldPredictor')
onehotencoder=OneHotEncoder(categorical_features=[1])
data=onehotencoder.fit_transform(data).toarray()
joblib.dump(onehotencoder,'OneHotEncoderPredictor')

from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
data=sc.fit_transform(data)
joblib.dump(sc,'SCPredictor')

X=data[:,:-1]
Y=data[:,-1]

X_train=X[:41,:]
Y_train=Y[:41,]
X_test=X[42:,:]
Y_test=Y[42:,]

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X_train,Y_train)
joblib.dump(regressor,'RegressorPredictor')


