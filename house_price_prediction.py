# -*- coding: utf-8 -*-
"""House Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DGx9BpQxqP7tdwCMbzdZkYtIhrO4WZKA
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

path = "/content/drive/MyDrive/House Price Prediction Project/"

df = pd.read_csv(f"{path}House Price India.csv")
df.head()

df.info()

sns.heatmap(df.corr())

plt.scatter(df['number of bedrooms'],df['Price'])

plt.scatter(df['number of bathrooms'],df['Price'])

plt.scatter(df['living area'],df['Price'])

plt.scatter(df['lot area'],df['Price'])

plt.scatter(df['number of floors'],df['Price'])

plt.scatter(df['waterfront present'],df['Price'])

plt.scatter(df['number of bathrooms'],df['Price'])

plt.scatter(df['number of bathrooms'],df['Price'])

plt.scatter(df['number of views'],df['Price'])

plt.scatter(df['condition of the house'],df['Price'])

plt.scatter(df['grade of the house'],df['Price'])

plt.scatter(df['Area of the house(excluding basement)'],df['Price'])

plt.scatter(df['Area of the basement'],df['Price'])

plt.scatter(df['Built Year'],df['Price'])

plt.scatter(df['Renovation Year'],df['Price'])

plt.scatter(df['Postal Code'],df['Price'])

plt.scatter(df['Lattitude'],df['Price'])

plt.scatter(df['Longitude'],df['Price'])

plt.scatter(df['living_area_renov'],df['Price'])

plt.scatter(df['lot_area_renov'],df['Price'])

plt.scatter(df['Number of schools nearby'],df['Price'])

plt.scatter(df['Distance from the airport'],df['Price'])

X = ['id', 'number of bedrooms', 'number of bathrooms', 'living area', 'lot area', 'number of floors', 'waterfront present', 'number of views', 'condition of the house', 'grade of the house', 'Area of the house(excluding basement)', 'Area of the basement', 'Built Year', 'Renovation Year', 'Postal Code', 'Lattitude', 'Longitude', 'living_area_renov', 'lot_area_renov', 'Number of schools nearby', 'Distance from the airport']
X = df[X]
y = df['Price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train,y_train)

predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))