import pandas as pd
import numpy as np

#df: data frame
df = pd.read_csv('test.csv')
# name, battery_level, version_name, device_id, timestamp

#new empty dataframe 
dfFreeFire = pd.DataFrame() # free fire

# str into  <class 'pandas._libs.tslib.Timestamp>
df['timestamp'] =  pd.to_datetime(df['timestamp'])

def agrupando(nome):
    version_name={} # dicionario de listas de Series 
    ## Name:
    ##Version_Name = {'Device_id' : [[timestamp, battery level]]} 
    for index, row in df.iterrows():
        if row["name"] == nome:
            if not row["version_name"] in version_name:
                version_name[row["version_name"]] = []
                version_name[row["version_name"]].append([row['timestamp'],row['battery_level']])
            else:
                version_name[row["version_name"]].append([row['timestamp'],row['battery_level']])
    return(version_name)


gamename= 'com.dts.freefireth'
print(agrupando(gamename))


#export_csv = dfFreeFire.to_csv ('test1.csv', index = None, header=True)
# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())
