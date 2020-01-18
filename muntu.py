import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('fever2.csv')
X = dataset.iloc[:, :-1] 
y = dataset.iloc[:, -1]
# =================================================================================== #
print(y)
modelRegressor = LinearRegression()
modelRegressor.fit(X, y)
pickle.dump(modelRegressor, open('muntu.pkl','wb'))
muntu = pickle.load(open('muntu.pkl','rb'))
print('|=========================== START OF PREDICTION  ===========================|')
print(muntu.predict([[3, 20, 40, 50, 67,88,77,44]]))
print(muntu.predict([[8, 60, 60, 70, 98,90,77,88]]))
print(muntu.predict([[4, 63, 45, 59, 84,59,67,79]]))
print('|=========================== END OF PREDICTION  =============================|')
# ==================================================================================== #