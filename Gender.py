import numpy as np
import pandas as pd


# salary, gender, age, phd = np.genfromtxt("SalaryGender.csv",delimiter = ",",skip_header=1, unpack=True)
# print(data)
# print(Salary)

data = pd.read_csv("SalaryGender.csv",delimiter = ",")
salary, gender, age, phd = np.array(data['Salary']),np.array(data['Gender']),np.array(data['Age']),np.array(data['PhD'])

# print(salary)
phd_data = pd.DataFrame()

phd_data['Gender'] = gender
phd_data['PhD'] = phd

male,female = 0,0

for index, row in phd_data.iterrows():
    if row['PhD'] == 1:
        if row['Gender'] == 1:
            male+=1
        else:
            female+=1


print(male)
print(female)            

df = pd.DataFrame()

df['Age'] = age
df['PhD'] = phd

for index, row in df.iterrows():
    if row['PhD'] == 0:
       df.drop(index,inplace=True)
        
print(df)


print('Total Phd: ', int(male)+int(female))


