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
    # version_name={ #NESTED DICT
    #     'Version_Name': {'Device_Id': [ [timestamp, battery level] ] }
    # }                                     #NESTED LIST
    version_name={0.0: {0: []}}
    for index, row in df.iterrows():
        if row["name"] == nome:  #para todos os dados do jogo selecionado
            #agrupando pela versão
            if not row["version_name"] in version_name: 
                version_name[row["version_name"]] = {} # cria
            #agrupando pelo dispositivo
            if not row['device_id'] in version_name[row["version_name"]]: 
                version_name[row["version_name"]][row['device_id']] = [] #cria
            version_name[row["version_name"]][row['device_id']].append([row['timestamp'],row['battery_level']]) #insere
    del version_name[0.0]
    return(version_name)

gamename= 'com.dts.freefireth'
freefire = agrupando(gamename)
# print(freefire)

for key, val in freefire.items():
    for key0, val0 in val.items():
        for i in val0:
            print(type(i))
            print(i)
            break
        break
    break


#export_csv = dfFreeFire.to_csv ('test1.csv', index = None, header=True)
# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())

