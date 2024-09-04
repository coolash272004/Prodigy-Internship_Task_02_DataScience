# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings

plt.style.use('seaborn-v0_8-whitegrid')
warnings.filterwarnings("ignore")

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('F:/Prodigy_Projects/Task2/dataset/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

#Load and Check the data
train_df = pd.read_csv("F:/Prodigy_Projects/Task2/dataset/train.csv")
#test_df = pd.read_csv("D:/Prodigy_Projects/Task2/dataset/test.csv")
print(train_df.columns)
#print(test_df.columns)
print(train_df.head())
print(train_df.describe())
print(train_df.info())


#Categorical Variable Analysis

def pie_chart(variable:str):
    """
    input: variable ex: "Sex"
    output: barplot & value count
    """
    # get feature
    var = train_df[variable]
    #count number of categorical variable(value/sample)
    varValue = var.value_counts()
    print('===>', variable)
    
    #visualize 
    plt.figure(figsize=(9,6))
    mylabels = ["Female", "Male"]
    color = ['red','green']
    plt.pie(varValue, labels=mylabels, colors=color)
    plt.legend(title = 'Sex : ')
    plt.title(variable)
    plt.show()

    print('<===', varValue)
    
    print("{}: \n {}".format(variable, varValue))

category1 = ["Survived", "Sex", "Pclass", "Embarked", "SibSp", "Parch"]
category2 = ["Survived", "Sex"]

for c in category2:
    pie_chart(c)



