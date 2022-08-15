#libraries used in this project
from turtle import filling
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt#For visualizations
from sklearn.preprocessing import StandardScaler, MinMaxScaler#for Scalling feature datas
from sklearn.impute import KNNImputer, SimpleImputer#for outlier handling
# Importing libraries for modelling and evaluation
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
#Mounting drive to google account

#Reading the dataset to dataframe named 'data_df'
data_df=pd.read_csv('data_cardiovascular_risk.csv',encoding = 'unicode_escape')
data_df=data_df.drop(columns=['id'])
st.write(data_df)
#Creating two variables for categorical and numerical feature for further analysis
cat_features = ['education', 'sex', 'is_smoking', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes']
num_features = ['age', 'totChol', 'cigsPerDay', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']
#label Encoding categorical features for further better analysis
data_df['sex']=np.where(data_df['sex']=='M',1,0)
data_df['is_smoking']=np.where(data_df['is_smoking']=='YES',1,0)
#Implementing Knn imputer on numerical features
knn_imputer= KNNImputer(n_neighbors=5)
knn_imputer.fit(data_df[num_features])
data_df[num_features]= knn_imputer.transform(data_df[num_features])
#Disrtribution and outlier analysis
fig=sns.displot(data=data_df, x='age', kind="kde")#displot for distribution analysis
st.pyplot(fig)



model = pickle.load(open('model.sav', 'rb'))
scalar = pickle.load(open('scalar.sav', 'rb'))
st.title('Heart diseases Prediction')
st.sidebar.header('Data')

# FUNCTION
def user_report():
  age = st.sidebar.slider('age', 33,100)
  education = st.sidebar.slider('education', 1,4)
  sex = st.sidebar.slider('sex', 0,1,1)
  cigsPerDay = st.sidebar.slider('cigsPerDay', 0,100)
  totChol = st.sidebar.slider('totChol',120,350)
  heartRate = st.sidebar.slider('heartRate	', 48,150)
  glucose = st.sidebar.slider('glucose',51,300)
  PP = st.sidebar.slider('PP',15,200)


  user_report_data = {
      'age':age,
      'education':education,
      'sex':sex,
      'cigsPerDay':cigsPerDay,
      'totChol':totChol,
      'heartRate':heartRate,
      'glucose':glucose,
      'PP':PP
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Data')
st.write(user_data)
user_data1=scalar.transform(user_data)
salary = model.predict(user_data1)
if salary==0:
     st.subheader('No chance for heart diseases')
else:
    st.subheader('High chance for heart diseases')
   
