import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
data={
      'Student':['John','Emnily','Michael','Sarah','David','Anna','Tom','James','Laura','Alice'],
      'Marks':[85,78,92,88,76,95,83,67,74,89]}
Student=pd.DataFrame(data)
sns.histplot(Student['Marks'],kde=True,color='blue',bins=6)
plt.title('Distribution of Student Marks')
plt.xlable('Marks')
plt.ylabel('Frequncy')
plt.show()