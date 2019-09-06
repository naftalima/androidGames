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

dateInit = []
batteryInit =[]
dateFinal = []
batteryFinal =[]
for key, val in freefire.items():
    print("version_name",key)
    for key0, val0 in val.items():
        print("device_id", key0)
        n = len(val0)
        dateInit.append(val0[0][0])
        batteryInit.append(val0[0][1])
        for i in range(n-1):
            print("timestamp: ",val0[i][0])
            print("battery level: ",val0[i][1])
            if ( val0[i][1] - val0[i+1][1] > 0.03) or (val0[i][1] - val0[i+1][1] <= 0): # pois parou
                dateFinal.append(val0[i][0])
                batteryFinal.append(val0[i][1])
                dateInit.append(val0[i+1][0])
                batteryInit.append(val0[i+1][1])
            else:
                if i == n-2: ##fim da lista
                    dateFinal.append(val0[i+1][0])
                    batteryFinal.append(val0[i+1][1])
                  
        break           
    break
print("OLAAAAAAAAAAAAAAAAAAAAA")
print(batteryInit)
print(len(batteryInit))
print(batteryFinal)
print(len(batteryFinal))

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
