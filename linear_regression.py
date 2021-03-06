# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7eR2hKawnLgW0rVe5jUzncZSI8H2e35
"""
#this model can predict sales based on Advertisements on TV,Newspaper and radio

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Advertising.csv')

X=df.drop('Sales',axis=1)
y=df['Sales']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
predic=model.predict(X_test)
from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(predic,y_test))
