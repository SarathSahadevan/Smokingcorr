import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix 



df=pd.read_excel('CleanedDataset.xlsx')

#==============================================================================
# df.describe()
# 
# 
# df.info()
# corrp=df.corr(method='pearson')
# 
# sci=scipy.stats.stats.spearmanr(df)
#==============================================================================


#Creating a new column having AgeGroup
age_group = ['20-29','30-39','40-49','50-59','60-69'] #Split labels
age_bins = [20,29,39,49,59,100] #Split intervals
df['Age_group'] = pd.cut(df['Age'], bins=age_bins, labels=age_group)
df['Age_group']= df['Age_group'].astype(str)



#Creating a new column having Usage
bins = [0.0, 0.20, 0.40, 0.60, 0.80,1.00] #Split intervals
labels = [1,2,3,4,5] #Split labels
df['Usage'] = pd.cut(df['Diary entry rate (narrow sense)'], bins=bins, labels=labels)
df['Usage'] = df['Usage'].fillna(1)
df['Usage']= df['Usage'].astype(int)

corrp=df.corr(method='pearson')
corrp=df.corr(method='kendall')
corrp=df.corr(method='spearman')
#replacing sex
df['Sex'].replace({'f':0,'m':1},inplace=True)

#correlation checking
dcorr=df['Age'].corr(df['Diary Entry Date.1'])



scatter_matrix(corr,figsize=(16,12),alpha=0.8)




scatter_matrix(corrk,figsize=(16,12),alpha=0.8)

scatter_matrix(corrp,figsize=(16,12),alpha=0.8)

scatter_matrix(corrs,figsize=(16,12),alpha=0.8)






