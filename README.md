# Coronary-Heart-Disease-Risk-Prediction


# Introduction
The contribution of ML in the healthcare industry is becoming more and more significant day by day. Looking into the health data of patients, along with demographic and lifestyle data can give us helpful insights into the medical condition of a patient. 
In this project, I'll be developing an ML Classification model to help predict if a patient is at the risk of developing Coronary Heart Disease, in the next 10 years, given their medical, behavioral and demographic data.

# Objective:

The objective of the project would be to predict whether a patient is under risk of contracting coronory heart disease (CHD) in the next 10 years, given the data about following 14 attributes:

• Sex: male or female("M" or "F")

• Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)

Behavioral

• is_smoking: whether or not the patient is a current smoker ("YES" or "NO")

• Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)

Medical( history)

• BP Meds: whether or not the patient was on blood pressure medication (Nominal)

• Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)

• Prevalent Hyp: whether or not the patient was hypertensive (Nominal)

• Diabetes: whether or not the patient had diabetes (Nominal) Medical(current)

• Tot Chol: total cholesterol level (Continuous)

• Sys BP: systolic blood pressure (Continuous)

• Dia BP: diastolic blood pressure (Continuous)

• BMI: Body Mass Index (Continuous)

• Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)

• Glucose: glucose level (Continuous)

# Approach
Following steps were followed to build the model: 
1. Dataset was cleaned off the null values. 
2. Outliers were replaced with upper limit and lower limit values as applicable. 3. Imbalances in the classes were fixed using SMOTE. 
4. Categorical features were encoded 
5. Feature selection was done by inspecting correlation between features and aforementioned features were finalised. 
6. The data was split to train and test and scaled using MinMaxScaler. 7. Following 4 models were implemented on the training set: 
1. Logistic Regression 
2. Random Forest Classifier 
3. K Nearest Neighbours 
4. Naive Bayes Classifier.

# Result
The task was to determine if a given patient is under the risk of CHD in the coming 10 years. To do this, following features were at our disposal: 
'id','age','education','sex','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabe tes','totChol','sysBP','BMI','glucose'. 'is_smoking','heartRate','diaBP','TenYearCHD'. Logistic Regression, Random Forest Classifier, K Nearest Neighbours, Naive Bayes Classifier were used Of which, the Random Forest classifier yielded best results. 
Using Shapley analysis it was found that education, age, cigsPerDay, sysBP, and totChol were top 5 most influential factors in determination of whether the patient is facing the risk of CHD or not.
