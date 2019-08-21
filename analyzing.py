import pandas as pd
#import numpy as np

#data_frame
df = pd.read_csv('test.csv')

print(df['idade'])
##<class 'pandas.core.series.Series'>

for cell in df['hogwarts house']:
    print(cell)
    #<type 'str'>

print(df.head())
#<class 'pandas.core.frame.DataFrame'>
