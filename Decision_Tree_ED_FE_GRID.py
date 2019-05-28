# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:34:58 2019

@author: YellapuP
"""

import pandas as pd
import os
from sklearn import tree
from sklearn import model_selection
from sklearn.externals import joblib
import numpy as np

# Change directory to the train, test datasets
os.getcwd()
os.chdir('C:\\Pavan Kumar Yellapu\\Pavan Workspace\\Learning\\prisonbreak263\\titanic')

# read the train data
t_train = pd.read_csv('train_data.csv')
# read the test data
t_test = pd.read_csv('test.csv')

t_test['Survived'] = None

titanic = pd.concat([t_train, t_test])

titanic.shape
titanic.info()
titanic.describe()

# EDA

# extract title from Name

def extract_title(name):
    return name.split(',')[1].split('.')[0].strip()

titanic['Title'] = titanic['Name'].map(extract_title)

# Use index = False if an new index for this data is not required
# this line is for understanding purpose only
titanic.to_csv('titanic_comb.csv',index=False)

titanic.info()

# Fill Age and Fare columns with the mean values of those columns

# Filling the data using .isnull() 
titanic['Age'][titanic['Age'].isnull()] = titanic['Age'].mean()
titanic['Fare'][titanic['Fare'].isnull()] = titanic['Fare'].mean()
titanic.info()

titanic['Age'].mode()
titanic['Age'].mean()

titanic['Fare'].mean()
titanic['Fare'].mode()

# Feature Enginering

titanic.info()

# Categorize Age column into groups

def Age_Cat(age):
    if (age >= 0 and age <= 10):
        return 'Child'
    elif age <= 25:
        return 'Young'
    elif age <= 50:
        return 'Middle'
    else:
        return 'Old'

titanic['Age_Cat'] = titanic['Age'].map(Age_Cat)
titanic.info()

# Categorize Fare Column

titanic['Family_Size'] = titanic['SibSp'] + titanic['Parch'] + 1
titanic.info()

def Family_Size_Cat(size):
    if size == 1:
        return 'Single'
    elif size <= 3:
        return 'Small'
    elif size <= 5:
        return 'Medium'
    else:
        return 'Large'

titanic['Family_Size_Cat'] = titanic['Family_Size'].map(Family_Size_Cat)
titanic.info() 

# 1-HOT Encoding for the categorical Columns
# Categorical Columns : Pclass, Age_Cat, Embarked, Sex, Family_Size_Cat, Title

titanic1 = pd.get_dummies(titanic,columns=['Pclass','Age_Cat','Embarked',
                                            'Sex','Family_Size_Cat','Title'])

titanic1.info()
titanic1.shape

titanic_train = titanic1.iloc[0:t_train.shape[0]]
titanic_test = titanic1.iloc[t_train.shape[0]:]
titanic_train.shape
titanic_test.shape

# X-axis columns

print (type(titanic_train))

titanic_train.info()
x_train = titanic_train.drop(['PassengerId','Age','SibSp','Parch','Cabin','Name','Survived','Ticket','Family_Size'], axis=1, inplace=False)
x_test = titanic_test.drop(['PassengerId','Age','SibSp','Parch','Cabin','Name','Survived','Ticket','Family_Size'], axis=1, inplace=False)

x_train.info()


y_train = t_train['Survived']
y_train.shape
titanic_train.info()

print (np.unique(y_train))

dec_tree = tree.DecisionTreeClassifier(random_state = 1)

print (list(range(2,10,2)))

params = {'max_depth':list(range(2,10,2)),
              'min_samples_split':list(range(2,8,2)),
              'criterion':['gini','entropy']}

params1 = {'max_depth':[2,5,7],
              'min_samples_split':[2,5,9],
              'criterion':['gini','entropy']}


dec_tree_grid = model_selection.GridSearchCV(dec_tree, params1, cv=10)

dec_tree_grid.fit(x_train, y_train)

dec_tree_grid.grid_scores_
dec_tree_grid.best_score_
dec_tree_grid.score(x_train, y_train)

dec_tree_grid.best_estimator_

dec_tree_grid.best_params_


titanic_test['Survived'] = dec_tree_grid.predict(x_test)

titanic_test.to_csv('titanic_test_est.csv',columns=['PassengerId','Survived'],index=False)

os.getcwd()

