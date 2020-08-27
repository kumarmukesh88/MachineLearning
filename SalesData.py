import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("BigMartSalesData.csv")

data = df[df['Year']==2011][["Amount","Month"]]

# print(df[df['Year']==2011])

total = data.groupby('Month').sum()

print(total)

plt.plot(total,color='red')

plt.xlabel("Year of 2011")
plt.ylabel("Sales")
plt.title("Sales per Month - 2011")
plt.legend(total)
plt.show()

total.plot(kind='bar',color='orange')
# plt.bar(total['Month'],total['Amount'])
plt.show()

#Feb has lowest sales
data = df[df['Year']==2011]
sales_cntry = data.groupby('Country').agg({'Amount':np.sum})

plt.pie(sales_cntry.values,labels=sales_cntry.index)
plt.show()

sales_invoice = df.groupby('InvoiceNo').agg({'Amount':np.sum})
print (sales_invoice)
plt.scatter(sales_invoice.values,sales_invoice.values,color='magenta')
plt.grid(True)
plt.show()