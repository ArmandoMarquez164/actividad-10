#Plantilla para el pre procesado de datos - datos faltantes
dataset = read.csv('C:/cargar/examen/Data.csv')



#Tratamiento de los valores N/A
dataset$Age = ifelse (is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean (x, na.rm = TRUE)),
                          dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean (x, na.rm = TRUE)),
                        dataset$Salary)
