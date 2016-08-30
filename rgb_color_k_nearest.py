#!/usr/bin/env python
# rgb2_color_k_nearest.py
# by wilsonmar@gmail.com, ayush.original@gmail.com, paarth.n@gmail.com
# This is not the complete/correct approach. This is just the framework possibly of using ML
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

df = pd.read_csv('rgb_combined_v01.csv') # load into dataframe
df.drop(['_Hex','_Name','_grey','_X11','_SVG'], 1, inplace=True)  #axis=1 denotes that we are referring to a column, not a row
#Here I've dropped all columns except those which give RGB values

#TEST: Data Loaded
print (df)


X= np.array(df.drop(['_Title'],1))# represents features
Y= np.array(df['_Title'])# represents labels

#partition in training and testing sets
X_train, X_test , Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size=0.01)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_test, Y_test)

accuracy = clf.score(X_test, Y_test)
print(accuracy)

example_rgb = np.array([222,184,135]) 
prediction = clf.predict(example_rgb)
print(prediction)