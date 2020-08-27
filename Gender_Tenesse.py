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


import numpy as np
import numpy.random
from numpy.linalg import matrix_rank

my_array = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

unique, counts = np.unique(my_array, return_counts=True)
count = np.asarray(counts)
print(count)

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 


# Now we will print the items greater than 5 
print('The items greater than 5 are:' )
print(x[x > 5])

nan_array = np.array([ np.nan,   1.,   2.,  np.nan,   3.,   4.,   5.])
nan_array = nan_array[~np.isnan(nan_array)]
print(nan_array)

rand_arr = np.random.rand(10,10)
print(rand_arr)
print(np.max(rand_arr))
print(np.min(rand_arr))

rand_vect = np.random.random(10)
print(np.mean(rand_vect))

neg_arr = np.arange(10)
neg_arr[(neg_arr>2) & (neg_arr<10)] *= -1
print(neg_arr)

ran_arr = np.random.rand(3,3)
# print(ran_arr)
nar = ran_arr[:,2].argsort()
ran_arr = ran_arr[nar]
# print(ran_arr)
ran_arr = ran_arr[ran_arr[:,1].argsort(kind='mergesort')]
ran_arr = ran_arr[ran_arr[:,0].argsort(kind='mergesort')]
print(ran_arr)

sum_arr = np.arange(16).reshape(4,4)
print(sum_arr)
print(np.sum(sum_arr))

swap_array = np.array([[4,3,1], [5,7,0], [9,9,3], [8,2,4]])
print(swap_array)
swap_array[[1,0]] = swap_array[[0,1]]
print(swap_array)

mat_arr = np.arange(10)
print(matrix_rank(mat_arr))

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('middle_tn_schools.csv')

print(df.describe())

grouped = df.groupby('school_rating').reduced_lunch.mean().reset_index()
print(grouped)

print(grouped.corr())

plt.scatter(df['reduced_lunch'], df['school_rating'])
plt.xlabel('Reduced Lunch')
plt.ylabel('School Rating')
plt.show()

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.xticks(rotation=90)
plt.colorbar()
plt.show()
