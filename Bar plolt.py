import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
data={
      'Job_Role':['Manager','Developer','Analyst','Manager','Developer',
                  'Analyst','Manager','Developer','Analyst','Developer'],
      'Salary':[120000,85000,65000,125000,87000,
                70000,13000,95000,60000,40000]}
df=pd.DataFrame(data)
plt.figure(figsize=(10,8))
sns.barplot(x='Job_Role',y='Salary',data=df,estimator=sum,palette='viridis')
plt.tittle('salary Distribution by Job Role')
plt.xlable('Job Role')
plt.ylable('Total Salary')
plt.show()