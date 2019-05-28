# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:53:54 2019

@author: YellapuP
"""

# Everything about Pandas
#https://medium.com/data-science-everywhere/ml-series-day-6-pandas-for-beginners-part-1-4aacad767d1c


import pandas as pd
import os

print (pd.__version__)

# Series is a one-dimensional array to hold data of any type such as 
# integer, string, float, python objects, etc.
# Unlike in arrays, in Series, we can customize the index values.


# a Serier will have data,index which can be customized, datatype
# pd.Series(data, index, dtype, copy)


# Empty Series
s = pd.Series()
print (s)
print (type(s))

# Creating a Series from a python List

list_py = [10,250,180,260]
s1 = pd.Series(list_py) # This will be created with a default index
print (s1,type(s1))


# with custom index
ind_py = ['jon','varys','tyrion','sansa']
s2 = pd.Series(list_py, index = ind_py) #can also give the list directly instead of ind_py
s3 = pd.Series(list_py, index = ['j','v','t','s'])
print (s2,type(s2))
print (s3,type(s3))

# Series can also be created from Dictionary. 
# Dict Indices are used as Series Indices

dictA = {'Name':['Tyrion','Sansa','Jon','Dany'],
         'Height':["3.4'","5.6'","5.11'","5.7'"]}
sA = pd.Series(dictA)
print (sA,type(sA))
print (sA.keys)

# Retrieving Data from a Series

print (s2[0])
print (s3['j'])
print (s2[['jon','sansa']])
print (s3[:3])
print (s3[-3:])
print (s2[:-2])
print (s2[1:-2])

# Normal Dictionary

dict1 = {'Name':['Tyrion','Sansa','Jon','Dany'],
         'Interests':['Reading Books','Say No to Dany','She is my Queen','Iron Throne']}

print (dict1,type(dict1))



####### Data Frames #########

# Data frame aslo has data, index, columns, dtype, copy
# pandas.DataFrame( data, index, columns, dtype, copy)

# Empty Data Frame
df1 = pd.DataFrame()
print (df1,type(df1))

s4 = pd.Series(dict1)
print (s4,type(s4))

df2 = pd.DataFrame(dict1)
print (df2,type(df2))

# Col and Row Operations on Series and DataFrame

print ('before adding column \n \n', df2)
df2['Famous for'] = pd.Series(['Wisdom','Nothing','She is my Queen','Dragon'])
print ('after adding column \n \n',df2)

# Deletion of columns

del df2['Famous for']

print (df2)

# Row Addition --> use append

new_row_data = pd.DataFrame([['Arya','No One']],columns=['Name','Interests'])
df2.append(new_row_data)

# deleting rows 
df2.drop(0) # Deletes the rows with the index as '0'

### Basic Functionalities in Series
# https://medium.com/data-science-everywhere/ml-series-day-6-pandas-for-beginners-part-1-4aacad767d1c

# Series --> axes, ndim, size, empty, values, head, tail,
# DataFrames --> transpose, axes, dtypes, empty, ndim, shape, size, head, tail
#               describe, Sum, Mean, Min, std, count, etc..,
#               Indexing and Slicing

df2.ndim # Gives number of Dimenstions of the dataframe/series
os.chdir('C:\\Pavan Kumar Yellapu\\Pavan Workspace\\Learning\\prisonbreak263\\titanic\\')
t_csv = pd.read_csv('test.csv')
t_csv.ndim # Gives number of Dimentions of the dataframe
t_csv.axes # Gives the lables of the dataframe in List format
print (type(t_csv.axes))
t_csv.columns.tolist() # alternate to .axes

t_csv.empty #Checks whether the df/series is empty or not. true if empty
t_csv.size
df2.size # total number of values 
df2.values # returns number of values of df in array format
df2.head(3) # returns first 3
df2.tail(2) # returns last 2
df2.T # Transpose a dataframe
df2.dtypes # returns datatype of each col

t_csv.shape # Gives the rows X cols number

t_csv.info() # Gives insight about the dataframe. 
# each col of this info is accessed as below

t_csv.dtypes # Gives the datatype of each col
t_csv.count() # Gives the count of each col

t_csv.describe() # More insight about the data

t_csv.sum() # Sum of all cols
t_csv.mean() # Avg of the numeric cols
t_csv.std() # Gives the Standard Deviation of the numeric cols
t_csv.min() # Min value of all cols
t_csv.max() # Max value of all cols
t_csv.max().tolist()
print (type(t_csv.max().tolist()))
print (type(t_csv.max()))

t_csv.groupby(['Sex']).groups # Group By col name
t_csv.groupby(['Pclass']).size() # Group By columns and give the count
t_csv.groupby(['Pclass']).mean() # Mean of all the numberical cols after grouping by a col
t_csv.groupby(['Pclass','SibSp']).groups
t_csv.groupby(['Pclass','SibSp']).size()
t_csv.groupby(['Pclass','SibSp']).mean()
t_csv.groupby(['Pclass','SibSp']).mean()['Fare'] # after mean extract specific col


# Fetching data by a specific data of a col

# .loc and .iloc are used
# .loc uses indexes and .iloc uses rows/row numbers

t_csv.loc[t_csv.Sex == 'female','Age'] # gives ages of all the females
t_csv.iloc[10:25] # 10 to 25 rows
# .loc takes index with respect to the original data
# after the fetch is done, 10 to 25 index of the original data is displayed
t_csv.loc[t_csv.Sex == 'female','Age'].loc[10:25] 

# whereas .iloc takes index with respect to the current data (data after some fetch)
# after the fetch is done, rows 10 to 25 fetched data is given
t_csv.loc[t_csv.Sex == 'female','Age'].iloc[10:25]

t_csv.iloc[2:20,1:3] # 2 to 20 rows of first 3 cols
t_csv.loc[1:4]

# filling the missing values
# fillna(), fillna(0), fillna(metod='backfill'), fillna(method='pad')

t_csv.fillna()



