import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
data={
      'Job_Role':['Engineer','Manager','Analyst','Engineer','Manager',
                  'Analyst','Engineer','Manager','Analyst','Engineer'],
      'Salary':[70000,80000,60000,72000,85000,
                58000,71000,82000,61000,75000]}
salary=pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.boxplot(x='Job_Role',y='Salary',data=salary)
plt.tittle('salary Distribution by Job Role')
plt.xlable('Job Role')
plt.ylable('Salary')
plt.show()