import matplotlib.pyplot as plt
import pandas as pd 

data = {
    'Month': ['2023-01','2023-02','2023-03','2023-04','2023-05',
              '2023-06','2023-07','2023-08','2023-09','2023-10'],
    'Sales': [15000,18000,21000,22000,25000,
              23000,24000,27000,30000,32000]
}

sales = pd.DataFrame(data)
sales['Month'] = pd.to_datetime(sales['Month'])

plt.figure(figsize=(10,6))
plt.plot(sales['Month'], sales['Sales'], marker='o', linestyle='-', color='blue')
plt.title('Monthly Sales Trends') 
plt.xlabel('Month')                 
plt.ylabel('Sales')                
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()                 
plt.show()
