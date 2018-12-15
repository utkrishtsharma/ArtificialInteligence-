import numpy as np
from sklearn import preprocessing, cross_validation
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#Loading Data
df = pd.read_csv('/home/cloudera/Desktop/McKinsey/train.csv')

#Feature Engineering
df.drop(['id'],1,inplace=True)  #dropping this column because it creates noise and reduce accuracy to 57%
df.drop(['work_type'],1,inplace=True)
df['gender'] = df['gender'].map({'Female':1,'Male':0,'Other':-99999})
df['ever_married'] = df['ever_married'].map({'No':0,'Yes':1}).astype(float)
df['Residence_type'] = df['Residence_type'].map({'Rural':1,'Urban':0}).astype(float)
df['smoking_status'] = df['smoking_status'].map({'formerly smoked':2,'never smoked':0,'smokes':1})
df['smoking_status'].fillna(-99999,inplace=True)
df['bmi'].fillna(-99999,inplace=True)   #filling null values with -99999 (as outlier)
df.astype(float).values.tolist()    #creating a list (array in other languages)

#Spliting Data to train machine
X = np.array(df.drop(['stroke'],1))
y = np.array(df['stroke'])

#Test size is 20% and Train is 80%
#Using Crossvalidation to validate train_test_split
X_train,X_test, y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2)

#Using Random forest because it's giving more auc_roc score
clf = RandomForestClassifier(max_depth=8, random_state=2) #these parameters are optional

#Similar Operations for test.csv
td = pd.read_csv('/home/cloudera/Desktop/McKinsey/test.csv')
td.drop(['id'],1,inplace=True)
td.drop(['work_type'],1,inplace=True)
td['gender'] = td['gender'].map({'Female':1,'Male':0,'Other':-99999})
td['ever_married'] = td['ever_married'].map({'No':0,'Yes':1}).astype(float)
td['Residence_type'] = td['Residence_type'].map({'Rural':1,'Urban':0}).astype(float)
td['smoking_status'] = td['smoking_status'].map({'formerly smoked':2,'never smoked':0,'smokes':1})
td['smoking_status'].fillna(-99999,inplace=True)
td['bmi'].fillna(-99999,inplace=True)
test_data = td.astype(float).values.tolist()

#Fitting Model
z = clf.fit(X_train,y_train)

#Calculating confidence
confidence = clf.score(X_test,y_test)

print(confidence)

#Predicting Values for Strokes (0/1)
p = clf.predict(test_data)

#Predicting Probabilities (from 0 to 1)
pro = clf.predict_proba(test_data)

#Saving output into csv
np.savetxt("/home/cloudera/Desktop/McKinsey/result_pro.csv", pro, delimiter=",")
