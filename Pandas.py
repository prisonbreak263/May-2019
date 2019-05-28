# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:18:48 2019

@author: YellapuP
"""

# this has infor for dataframes

#Dataframes

import pandas as pd
print (pd.__version__)
titanic_train = pd.read_csv('C:/Pavan Kumar Yellapu/Pavan Workspace/Learning/prisonbreak263/titanic/train_data.csv')
print (titanic_train)
print (type(titanic_train))
#titanic_train1 = pd.read_clipboard() --> this reads the clipboard
#print (titanic_train1)

#no of rows and columns
#datatypes of the each and every columns

titanic_train.shape
titanic_train.info()
titanic_train.describe()

titanic_train.loc[titanic_train.Sex == 'female','Age'].iloc[10:20]
titanic_train.loc[titanic_train.Sex == 'female','Age'].loc[10:20]
titanic_train['Sex'] #Gives all the Sex column values
titanic_train.Sex[0] #gives first row of Sex column
titanic_train.Fare
titanic_train['Fare'][0] 

# Gives the Columns Names
titanic_train.columns()
titanic_train.columns.tolist() # gives those columns as a list

titanic_train.loc[titanic_train.Age == 28,'Age'].loc[100:200].tolist()

list1 = titanic_train[['Survived','Sex','Age']]
print (list1)
print (type(list1)) #Understand that this would be a dataframe

#accessing row of ith record
titanic_train.iloc[890] #this gived the 891st row data
titanic_train.iloc[755] #this gives the 756th row data

titanic_train[10:20]
titanic_train.iloc[10:20]

#fetch first n records
titanic_train.head(10)

#fetch last n records
titanic_train.tail(10)

titanic_train.iloc[10:11]

#iloc gives all the columns of the records
#loc gives specified columns

#access by columns names of a group of data
titanic_train.loc[10:20,('Name','Age')]

#conditional access of dataframes
#here we fetched the rows of "female" records 
#and then give only age col
titanic_train.loc[titanic_train.Sex == 'female','Age']
#after the fetch give the m to n rows of the resulting dataframe
titanic_train.loc[titanic_train.Sex == 'female','Age'].iloc[10:20]

titanic_train.loc[titanic_train.Sex == 'female','Age']


#grouping of columns
#.size() gives the count of the remaining columns grouped by the given cols
#.mean() gives the mean of the remaining columns grouped by the given cols
titanic_train.groupby(['Pclass']).size()
titanic_train.groupby(['Pclass','Sex']).size()
titanic_train.groupby(['Embarked','Pclass']).mean()
titanic_train.groupby(['Embarked','Pclass']).max()

titanic_train.groupby(['Embarked','Pclass']).mean()['Fare']


#.loc is working before the selection .iloc is working after the selection

titanic_train.loc[titanic_train.Sex == 'female','Sex']
titanic_train.loc[titanic_train.Sex == 'female','Age'].loc[10:20].tolist()
titanic_train.loc[titanic_train.Sex == 'female','Age'].iloc[10:20].tolist()

titanic_train.columns.tolist()


titanic_train.loc[titanic_train.Age == 28,'Age'].loc[100:200].tolist()


titanic_train.groupby(['Pclass','Age','Sex']).size()



