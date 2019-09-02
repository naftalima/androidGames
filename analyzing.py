import pandas as pd
import numpy as np

# TYPE df['column'])
# <class 'pandas.core.series.Series'>
# TYPE df.head()
# <class 'pandas.core.frame.DataFrame'>

#df: data frame
df = pd.read_csv('test.csv')
#print(df.head())
# for i in df:
#     print(i)
# # name, battery_level, version_name, device_id, timestamp

#new empty dataframe 
dfFF = pd.DataFrame() # free fire


## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html 
df['timestamp'] =  pd.to_datetime(df['timestamp'])
# for i in df['timestamp']:
#     print(type(i))
#     break
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

version_name={}
for index, row in df.iterrows():
    if row["name"] == 'com.dts.freefireth':
        if not row["version_name"] in version_name:
            version_name[row["version_name"]] = []
            version_name[row["version_name"]].append(row['device_id'])

        else:
            version_name[row["version_name"]].append(row['device_id'])

# print(version_name)
# print(version_name.keys())
# for i in version_name.items():
#     print(i) # TUPLE (KEY, ITEM)

#export_csv = dfFF.to_csv ('test1.csv', index = None, header=True)
# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())
