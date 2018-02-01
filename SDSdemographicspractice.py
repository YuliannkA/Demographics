import pandas as pd

stats = pd.read_csv('Demographics/DemographicData.csv')
stats.head()

import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.rcParams['figure.figsize'] = 8,4

vis1 = sns.distplot(stats["InternetUsers"])
vis2 = sns.boxplot(data=stats, x="IncomeGroup",y="BirthRate")
vis3 = sns.lmplot(data=stats, x="InternetUsers",y="BirthRate",fit_reg=False, hue='IncomeGroup', \
                 scatter_kws={"s":100})
