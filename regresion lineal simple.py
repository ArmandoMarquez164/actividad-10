# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:41:34 2023

@author: El Nando0 16 4
"""
#ARMANDO MARQUEZ OCHOA
#212664761
#08/03/2023
#ACTIVIDAD 17

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar el data set
dataset = pd.read_csv('C:/cargar/Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0 )

#Crear modelo de regresion lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#Predecir el conjunto de test
y_pred = regression.predict(X_test)

#Visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "red")
plt.plot(X_train, regression.predict(X_train), color = "blue")
plt.title("Sueldo vs Años de experiencia (conjunto de testing)")
plt.xlabel("Años de experiencia ARMANDO MARQUEZ OCHOA, 212664761")
plt.ylabel("Sueldo (en $)")
plt.show()

#visualizar los resultados de test
plt.scatter(X_test, y_test,color = "red")
plt.title("Sueldo vs Años de experiencia ARMANDO MARQUEZ OCHOA, 212664761")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo (en $)")
plt.show()
