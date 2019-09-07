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
    # print("version_name",key)
    for key0, val0 in val.items():
        print("device_id", key0)
        print(val0[-1][1])
        for j in val0:
            print(j[1])
        n = len(val0)
        for i in range(n-1):
            print("timestamp: ",val0[i][0])
            print("battery level: ",val0[i][1])

            if  i == 0: #inicio da lista
                dateInit.append(val0[i][0])
                batteryInit.append(val0[i][1])
                print("START","inicio: ", val0[i][1])

            diff =  val0[i+1][1] - val0[i][1]
            if ( diff < -0.03 ) or ( diff > 0.0): #parou 
                print("STOP","fim: ", val0[i][0], "inicio do prox:", val0[i+1][0])

                dateFinal.append(val0[i][0])
                batteryFinal.append(val0[i][1])
                dateInit.append(val0[i+1][0])
                batteryInit.append(val0[i+1][1])

            if i == n-2: ##fim da lista
                print("timestamp: ",val0[i+1][0])
                print("battery level: ",val0[i+1][1])
                dateFinal.append(val0[i+1][0])
                batteryFinal.append(val0[i+1][1]) 
                print("END", "final:", val0[i+1][1])


        break 
    break
                   

print("inicio: ", batteryInit)
print(len(batteryInit))
print("fim: ",batteryFinal)
print(len(batteryFinal))

#export_csv = dfFreeFire.to_csv ('test1.csv', index = None, header=True)
# df = df.drop(columns="coluna") #delete coluna
# df['colunaNome'] = listaValores #add colunaNome
# print(df.head())


                # diff =  val0[i+1][0] - val0[i][0] 
                # # <class 'pandas._libs.tslib.Timedelta'>
                # # diff.seconds <class 'int'>