# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GT70b7TTGeUkkDd_VrqYmQ3XGvuEPLfi
"""

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
sns.set(style="white", color_codes=True)
from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data["data"], columns=data.feature_names)
df["Species"] = data.target
df.dropna(inplace=True)
df

df["Species"].value_counts()

flower_maping = {'setosa': 0, 'versicolor': 1, 'virginica': 2}

df.head()

x_train = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].values
y_train = df[['Species']].values

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)

model.score(x_train, y_train)