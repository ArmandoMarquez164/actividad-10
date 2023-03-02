#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Atributos, metodos y funciones
#AMO 1 de marzo de 2023
import pandas as pd

#reading the cvs file
df_exams = pd.read_csv ('C:/analitica/StudentsPerformance.csv')

#mostrando el dataframe
df_exams


# In[2]:


#obteniendo acceso al atributo shape
df_exams.shape


# In[3]:


#obteniendo acceso al atributo index
df_exams.index


# In[5]:


#obteniendo acceso al atributo colums
df_exams.columns


# In[6]:


#tipo de dato de cada columna
df_exams.dtypes


# In[7]:


#mostrando las 5 primeras filas
df_exams.head()


# In[8]:


#mostrando informacion del dataframe
df_exams.info()


# In[9]:


#obteniendo valores estadisticos del dataframe
df_exams.describe()


# In[10]:


#obtener el tamaño del dataframe (filas)
len(df_exams)


# In[11]:


#obtener el maximo index
max(df_exams.index)


# In[12]:


#obtener el tipo de dato
type(df_exams)


# In[13]:


#redondear valores del dataframe
round(df_exams,2)


# In[ ]:




