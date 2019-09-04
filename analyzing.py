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
    #                                        #NESTED LIST
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


dataf = { 'Tinicial': [] , 'Tfinal': [], 'Binicial': [], 'Bfinal': [] }
for key, val in freefire.items():
    for key0, val0 in val.items():
        n = len(val0)
        tempos = []
        for i in range(n-1):
            if (i[1] - i[+1] > 0.3): # pois parou
                
            else:
                tempo.append(i[0])
                dataf['Tinicial'].append(tempo[0])
                dataf['Tfinal'].append(tempo[-1])


        # count=0
        # tempos=[]
        # while len(val0) > count:
        #     # val[count][0] : <class 'pandas._libs.tslib.Timestamp'>      -Timestamp
        #     # val[count][1] : <class 'float'>                             - Battery_Level
        #     if (val0[count][1] - val0[count+1][1] > 0.3) or (val0[count][1]) : #parou de usar
                
        #     else:
        #         tempos.append(val0[count][1])

        #     count+=1
        
    #         break
    #     break
    # break


#export_csv = dfFreeFire.to_csv ('test1.csv', index = None, header=True)
# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())
