import pandas as pd

# df = pd.read_csv('C:/Users/Kumar/bank-data.csv',usecols=['job'],index_col=False,sep=',')
df = pd.read_csv('C:/Users/Kumar/bank-data.csv',index_col=False)
# 
# print(df['job'].to_string(index=False))
# print(df.iloc[[1]])
# print(df[['job']].to_string(index=False))
# list1 = df[['job']].to_string(index=False)

list2 = df['job'].values.tolist()

# print(list2)

jobs = set(list2)

print(jobs)
    # print(rows)

profession = input('Enter your Profession: ')

if profession in jobs:
    print('Your are eligible')
else:
    print('You are not eligible')

# for p in profession:
#     print(map(str,rows[1]))
