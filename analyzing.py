import pandas as pd
import numpy as np

""" https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html """

#df == data frame
df = pd.read_csv('test.csv')
print(df.head())


# TYPE df['column'])
# <class 'pandas.core.series.Series'>
# TYPE df.head()
# <class 'pandas.core.frame.DataFrame'>
df['timestamp'] =  pd.to_datetime(df['timestamp'])

# for i in df['timestamp']:
#     print(type(i))
#     break
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>


# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome

print(df.head())


export_csv = df.to_csv ('test1.csv', index = None, header=True)
