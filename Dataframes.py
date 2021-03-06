# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:34:40 2019

@author: YellapuP
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 5 08:18:48 2019

@author: Pavan Yellapu

"""
# Working on Pandas and Dataframes

# Dataframes

import pandas as pd
# To know ther version of pandas use __version__
print (pd.__version__)
# Below statement reads a CSV file (you could also read the excel file, text file etc..,
# Give the file name in quotes. 
# This statement returns a Dataframe 
# ***I have considered the titanic disaster data file and wrote all the lines of code
titanic_train = pd.read_csv(<File name here in quotes>)
# prints the above variable data
print (titanic_train)
# prints the variable type
print (type(titanic_train))

# <dataframe>.shape gives the number of rows and columns of the dataframe
# <dataframe>.info() gives the column name and the total number of non null values under that column
# <dataframe>.describe() gives the count, average, mean, max etc.., of the numeric columns

titanic_train.shape
titanic_train.info()
titanic_train.describe()

titanic_train['Sex'] #Gives all the values of column 'Sex'
titanic_train.Sex[0] #gives first row of the column 'Sex'
titanic_train.Fare   #Gives all the values of column 'Fare'
titanic_train['Fare'][0] #Gives first row of the column 'Fare'

# Extract the only the selected columns from a dataframe
# Note that the result would also be a dataframe
list1 = titanic_train[['Survived','Sex','Age']] 
print (list1)
print (type(list1)) #Understand that this would be a dataframe

#accessing row of ith record
titanic_train.iloc[890] #this gived the 891st row data
titanic_train.iloc[755] #this gives the 756th row data

titanic_train[10:20] #from index 10 to index 20
titanic_train.iloc[10:20] 

#fetch first n records
titanic_train.head(10)

#fetch last n records
titanic_train.tail(10)

titanic_train.iloc[10:11]

#iloc gives all the columns of the records
#loc gives specified columns

#access by columns names of a group of data
# .loc takes Rows and Columns
# .loc[rows, columns]
# Below statement gives the index 10 to index 20 rows and 'Name' & 'Age' columns
titanic_train.loc[10:20,('Name','Age')] 

# Conditional access of dataframes
# Here we fetched the rows of "female" records 
# And then give only age col
# here also take the Rows of 'female' and the column as 'Age'
titanic_train.loc[titanic_train.Sex == 'female','Age']
#after the fetch give the m to n rows of the resulting dataframe
titanic_train.loc[titanic_train.Sex == 'female','Age'].iloc[10:20]
# This first takes the index 10 to 20 and then perform the remaining operation
titanic_train.loc[titanic_train.Sex == 'female','Age'].loc[10:20]


# Grouping of the columns
# .size() gives the count of the remaining columns grouped by the given cols
# .mean() gives the mean of the remaining columns grouped by the given cols
# similarly other functions are .max(), .min() etc..,
titanic_train.groupby(['Pclass']).size()
titanic_train.groupby(['Pclass','Sex']).size()
titanic_train.groupby(['Embarked','Pclass']).mean()
titanic_train.groupby(['Embarked','Pclass']).max()

# After the grouping the operation give only the 'Fare' Column
titanic_train.groupby(['Embarked','Pclass']).mean()['Fare']

#.loc is working before the selection .iloc is working after the selection

titanic_train.loc[titanic_train.Sex == 'female','Sex']
titanic_train.loc[titanic_train.Sex == 'female','Age'].loc[10:20]
titanic_train.loc[titanic_train.Sex == 'female','Age'].iloc[10:20]

# dataframe.columns gives the column names and the resulting would be a dataframe
# .tolist() --> converts this dataframe to a list 
titanic_train.columns.tolist()

titanic_train.loc[titanic_train.Age == 28,'Age'].loc[100:200].tolist()

titanic_train.groupby(['Pclass','Age','Sex']).size()

