import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Hurricanes.csv')

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(df['Year'],df['Hurricanes'])
plt.show()