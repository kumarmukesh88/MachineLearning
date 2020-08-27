import pandas as pd
from sklearn.preprocessing import LabelEncoder 


math_df = pd.read_csv('MathScoreTerm1.csv')
ds_df = pd.read_csv('DSScoreTerm1.csv')
phy_df = pd.read_csv('PhysicsScoreTerm1.csv')

math_df.drop(['Name','Ethinicity'],axis=1,inplace=True)
ds_df.drop(['Name','Ethinicity'],axis=1,inplace=True)
phy_df.drop(['Name','Ethinicity'],axis=1,inplace=True)

math_df.fillna(0,inplace=True)
ds_df.fillna(0,inplace=True)
phy_df.fillna(0,inplace=True)

merged = pd.concat([math_df,ds_df,phy_df])


labelencoder = LabelEncoder()
merged['Sex'] = labelencoder.fit_transform(merged['Sex'])

merged.to_csv('FinalScore.csv',index=False)


