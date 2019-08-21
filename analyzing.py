import pandas as pd
import numpy as np

#data_frame
df = pd.read_csv('test.csv')

# print(df['idade'])
# ##<class 'pandas.core.series.Series'>
# print(df.head())
# #<class 'pandas.core.frame.DataFrame'>

day = []
time = []
for cell in df['timestamp']:
    dt = cell.split(" ")
    day.append(dt[0])
    time.append(dt[1])

data = data.drop(columns="timestamp")
df['day'] = day
df['dia'] = day


# print(df.head())
# #<class 'pandas.core.frame.DataFrame'>

# export_csv = df.to_csv ('test1.csv', index = None, header=True)
#  #Don't forget to add '.csv' at the end of the path
