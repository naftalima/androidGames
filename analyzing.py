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
dfout = pd.DataFrame()


## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html 
df['timestamp'] =  pd.to_datetime(df['timestamp'])
# for i in df['timestamp']:
#     print(type(i))
#     break
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>



export_csv = dfout.to_csv ('test1.csv', index = None, header=True)

# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())
