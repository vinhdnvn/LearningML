import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd


data_set= pd.read_csv('data/salary/salary_Data.csv')

x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 1].values

# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 1/3, random_state=0)  