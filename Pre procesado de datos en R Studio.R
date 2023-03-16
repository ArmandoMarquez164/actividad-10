#Plantilla para el pre procesado de datos
#importar el dataset
dataset = read.csv('C:/cargar/examen/Data.csv')
dataset = dataset [2:3]

#Dividir los datos en conjunto de entrenamiento y conjunto de test 
install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split (dataset$Salary, SplitRatio = 0.8)
training_set = subset(dataset, split== TRUE)
testing_set = subset(dataset, split== FALSE)
