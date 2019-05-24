# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.5
# ---

# +
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
# -

df = pd.read_csv('ChanDarren_RaiTaran_Lab2a.csv')

df.head()

male = pd.get_dummies(df['Sex'],drop_first=True)
merged = pd.concat([df,male],axis='columns')
merged = merged.drop('Sex',axis='columns')

classes = pd.get_dummies(df['Pclass'],drop_first=True)
classes.columns = ['Class 2', 'Class 3']
merged2 = pd.concat([merged,classes],axis='columns')
merged2 = merged2.drop('Pclass',axis='columns')

merged2.Age = merged2.Age.fillna(merged2.Age.median())

features = merged2[['Age','SibSp','Parch','Fare','male','Class 2','Class 3']]
target = merged2['Survived']

clf = DecisionTreeClassifier(max_depth=10)

# # Train the model

clf.fit(features,target)

# # Use the model

clf.predict([[30,0,0,32,1,0,1]])

clf.predict_proba([[30,0,0,32,1,0,1]])

# # Save the model

joblib.dump(clf, 'my_model.pkl') 
