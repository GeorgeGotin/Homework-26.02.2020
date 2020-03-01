import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')
print(df)
sns.lmplot(x='age',y='survived',col='pclass',palette='deep',hue='alone',data=df)
plt.show()
