import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler



df = pd.read_csv("cereal.csv")
plt.hist([df["sugars"],df["vitamins"]],color=["orange","green"])
plt.xlabel("Sugar and Vitamins")
plt.legend(["Sugar","Vitamin"])
plt.show()


mnftr_dict = {'N': 'Nabisco','Q': 'Quaker Oats','K': 'Kelloggs','R': 'Raslston Purina','G': 'General Mills' ,'P' :'Post' ,'A':'American Home Foods Products'}
df["manufactures"] = [mnftr_dict[key] for key in df["mfr"]]
print(df)

grp_df = df.groupby(["manufactures"],as_index=False).count()
count = df["manufactures"].value_counts()

x = grp_df["manufactures"]
y = grp_df["mfr"]

plt.bar(x,y)
plt.xlabel("manufactures")
plt.xticks(rotation=90)
plt.ylabel("Count")
plt.show()

X = df.iloc[:,3:15].values
Y = df["rating"].values
print(X,Y)
print("####################################")

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.25, random_state=10)

l_model = LinearRegression()


# sc = StandardScaler()
 
# x_train = sc.fit_transform(x_train)
 
# x_test = sc.transform(x_test)

l_model.fit(x_train,y_train)

print(x_train)
print("####################################")
print(y_train)
print("####################################")

predicted_rating = l_model.predict(x_test)
y_pred = predicted_rating
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
print("####################################")
print(l_model.score(y_test,predicted_rating))
plt.scatter(np.array(predicted_rating), np.array(y_test))
plt.show()


