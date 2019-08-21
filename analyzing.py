import pandas as pd
import numpy as np

#df = data frame
df = pd.read_csv('test.csv')

# df['column'])
# <class 'pandas.core.series.Series'>
# df.head()
# <class 'pandas.core.frame.DataFrame'>

day = []
time = []
for cell in df['timestamp']:
    dt = cell.split(" ")
    # print(dt)
    # break
    day.append(dt[0])
    time.append(dt[1])

df = df.drop(columns="timestamp")
df['day'] = day
df['dia'] = time

# print(df.head())

export_csv = df.to_csv ('test1.csv', index = None, header=True)
#Don't forget to add '.csv' at the end of the path
