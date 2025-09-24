import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
data={
      'company A':[100,101,102,103,104,109],
      'company B':[95,96,97,98,99,100],
      'company C':[110,112,114,116,118,120],
      'company D':[90,89,88,87,86,85]}
stock=pd.DataFrame(data)
correlation=stock.corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation,annot=True,cmap='coolwarm',fmt="4f",linewidths=19)
plt.tittle('Correlation Heatmap of Stock Prices')
plt.xlable('Stock')
plt.ylable('Stocks')
plt.show()