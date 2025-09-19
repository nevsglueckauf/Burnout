import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats 
import scipy.stats as st

# A first look at the data
#df = pd.read_csv("dta/train.csv")

df_train = pd.read_csv("dta/train.csv")
#df = pd.read_csv("dta/test.csv")
#print(len(df_train))
#print(df_train.columns)

# Representing categorical data using Letter Value Boxplots
#fig, ax = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(10,5))
#sns.boxenplot(x="Gender", y="Burn Rate", data=df_train, palette="winter", linewidth=0.0, ax=ax[0])
#sns.boxenplot(x="Company Type", y="Burn Rate", data=df_train, palette="winter", linewidth=0.0, ax=ax[1])
#sns.boxenplot(x="WFH Setup Available", y="Burn Rate", data=df_train, palette="winter", linewidth=0.0, ax=ax[2])
#plt.tight_layout()

sns_plot = sns.pairplot(df_train, height=2.5, corner=True)


plt.show()

# ['Employee ID', 'Date of Joining', 'Gender', 'Company Type',
#       'WFH Setup Available', 'Designation', 'Resource Allocation',
#       'Mental Fatigue Score', 'Burn Rate'],