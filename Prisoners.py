import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("prisoners.csv")
# print(df)
sliced_df = df.head(5)
sliced_df = sliced_df.append(df.tail(5))
print(sliced_df)


print("###############################")
# print(df.describe())
print("No. of Columns: ",len(df.columns))
df1 = df.loc[(df['No. of Inmates benefitted by Elementary Education']==0) & (df['No. of Inmates benefitted by Adult Education']==0) & (df['No. of Inmates benefitted by Higher Education']==0) & (df['No. of Inmates benefitted by Computer Course']==0)]
print(df1)

df["total_benefitted"] = df.iloc[:,2:6].sum(axis=1)
print(df)

list1 = {"STATE/UT":"Total","YEAR":2013}
list1.update(df.iloc[1:,2:7].sum())
print(list1)
df2 = df.append(list1, ignore_index=True)
print(df2)
# print(df)

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
states = df["STATE/UT"].values
totalBen = df["total_benefitted"].values
axes.bar(states,totalBen)
# axes.set_xticks(label="State/UT",rotation='vertical')
axes.set_title('Inmates by State / UT')
plt.xticks(rotation=90)
axes.set_ylabel("Number Of Inmates")
axes.set_xlabel("State/UT")
plt.tight_layout()
plt.show()


