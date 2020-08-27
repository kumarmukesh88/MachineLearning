import pandas as pd


df = pd.read_csv("Salaries.csv",usecols = [i for i in range(12)])

df_salary_cost = df[['Year','TotalPay']].groupby('Year').mean()
print(df_salary_cost)

print('#####################################')
df_highest = df[df['Year']==2014][['JobTitle','TotalPay']].groupby("JobTitle").mean()
# print(df_highest)
print(df_highest[df_highest["TotalPay"]==df_highest["TotalPay"].max()])


print('#####################################')
sal_saved = df[df['Year']==2014][['OvertimePay']].sum()
print(sal_saved)


print('#####################################')
df_top = df[df['Year']==2014][['JobTitle','TotalPay']]
df_top5 = df_top.sort_values('TotalPay',ascending=False).head()
print(df_top5)

print('#####################################')
df_highest_sal = df[['EmployeeName','Year','TotalPayBenefits']]
print(df_highest_sal[df_highest_sal["TotalPayBenefits"]==df_highest_sal["TotalPayBenefits"].max()])
