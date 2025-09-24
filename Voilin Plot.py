import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
data={
      'Subject':[
                 'Math','Math','Math','Math','Math','Science','Science','Science',
                 'Science','Science','English','English','English','English',
                 'English','History','History','History','History','History',],
      'Grade':[85,78,92,88,76,95,83,67,74,89,
                88,75,82,91,85,80,77,90,85,72]}
grades=pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.violinplot(x='Subject',y='Grade',data=grades,palette='muted')
plt.tittle('Distribution of Students\'Grades By Subject')
plt.xlable('Subject')
plt.ylable('Grade')
plt.show()