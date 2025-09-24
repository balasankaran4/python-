import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
data={
      'Hight':[60,62,65,67,70,72,75,78,80,82],
      'Weight':[115,120,130,140,150,160,170,180,190,200]}
hight=pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.regplot(x='Hight',y='Weight',data=hight,marker='o',color='blue')
plt.title('Scattar plot')
plt.xlabel('Hight(inches)')
plt.ylable('Weight(pounds)')
plt.grid()
plt.show()