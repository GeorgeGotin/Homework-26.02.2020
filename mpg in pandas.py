import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('mpg')
print(df)
df['mark']=[i[0:i.find(' ') if i.find(' ') != -1 else len(i)] for i in df['name']]
print(df)
sns.lineplot(x='cylinders',y='mpg',hue='mark',data=df)
plt.plot(df['cylinders'],df['mpg'],'o')
for i in range(df.shape[0]):
	plt.annotate(df['name'][i],xy=(df['cylinders'][i],df['mpg'][i]))
plt.show()
