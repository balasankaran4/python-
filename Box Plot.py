import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
data={
      'Student':['John','Emnily','Michael','Sarah','David','Anna','Tom','James','Laura','Alice'],
      'Maths':[85,78,92,88,76,95,83,67,74,89],
      'Science':[90,82,94,85,80,95,78,88,76,90],
      'English':[78,85,91,88,76,84,75,90,77,88],
      'History':[70,75,80,68,73,88,84,67,82,90]}
exam=pd.DataFrame(data)
examScore=pd.melt(exam,id_vars=["Student"],var_name="Subject",value_name="Score")
plt.figure(figsize=(10,6))
sns.boxplot(x="Subject",y="Score",data=examScore)

plt.title('Distribution of Student Exam Score')
plt.xlable('Subject')
plt.ylabel('Scores')
plt.show()