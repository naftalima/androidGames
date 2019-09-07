import pandas as pd
import numpy as np

#df: data frame
df = pd.read_csv('_SELECT_name_battery_level_version_name_device_id_timestamp_FROM_201909071531.csv')
# name, battery_level, version_name, device_id, timestamp

# #new empty dataframe 
# dfFreeFire = pd.DataFrame() # free fire

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


def porUso(jogoAgrupado):

    dfJogo = pd.DataFrame()
    
    dateInit = []
    batteryInit =[]
    dateFinal = []
    batteryFinal =[]
    
    for key, val in jogoAgrupado.items():
        # print("version_name",key)
        for key0, val0 in val.items():
            # print("device_id", key0)
            n = len(val0)
            for i in range(n-1):
                if  i == 0: #inicio da lista
                    dateInit.append(val0[i][0])
                    batteryInit.append(val0[i][1])
                    # print("START","inicio: ", val0[i][1])
                diff =  val0[i+1][1] - val0[i][1]
                if ( diff < -0.03 ) or ( diff > 0.0): #parou 
                    dateFinal.append(val0[i][0])
                    batteryFinal.append(val0[i][1])
                    dateInit.append(val0[i+1][0])
                    batteryInit.append(val0[i+1][1])
                    # print("STOP","fim: ", val0[i][0], "inicio do prox:", val0[i+1][0])
                if i == n-2: ##fim da lista
                    dateFinal.append(val0[i+1][0])
                    batteryFinal.append(val0[i+1][1]) 
                    # print("END", "final:", val0[i+1][1])

    # print("inicio: ", batteryInit)
    # print("inicio: ", dateInit)
    # print(len(dateInit))
    # print("fim: ",batteryFinal)
    # print("fim: ",dateFinal)
    # print(len(dateFinal))

    dfJogo['BatteryLevelFinal'] = batteryFinal
    dfJogo['BatteryLevelInitial'] = batteryInit
    dfJogo['TimestampFinal'] = dateFinal
    dfJogo['TimestampInitial'] = dateInit

    print(dfJogo.head(10))

    batteryused = []
    elapsedtime = []
    for index, row in dfJogo.iterrows():
        battery = row['BatteryLevelInitial'] - row['BatteryLevelFinal']
        time = row['TimestampFinal'] - row['TimestampInitial']
        # # <class 'pandas._libs.tslib.Timedelta'>
        # # diff.seconds <class 'int'>
        batteryused.append(battery)
        elapsedtime.append(time.seconds)

    dfJogo = dfJogo.drop(columns="BatteryLevelFinal")
    dfJogo = dfJogo.drop(columns="BatteryLevelInitial")
    dfJogo = dfJogo.drop(columns="TimestampInitial")
    dfJogo = dfJogo.drop(columns="TimestampFinal")

    dfJogo['Battery_Used'] = batteryused
    dfJogo['ElapsedTimestamp'] = elapsedtime

    dfJogo = dfJogo.set_index("ElapsedTimestamp")
    dfJogo = dfJogo.drop(0, axis=0)

    return(dfJogo)

#     Garena Free Fire: com.dts.freefireth
#     Fun Race 3D: com.slippy.linerusher
#     Among Us: com.innersloth.spacemafia
#     Tomb of the Mask: com.playgendary.tom
#     Subway Surfers: com.kiloo.subwaysurf
#     aquapark.io: com.cassette.aquapark
#     * ROBLOX: com.roblox.client
#     Rocket Sky!: com.dpspace.rocketsky
#     Miraculous: Ladybug & Gato Noir Jogo Oficial: com.crazylabs.lady.bug
#     PUBG MOBILE LITE: com.tencent.iglite
#     Flip Dunk: com.tapped.flipdunk
#     Magic Tiles 3: com.youmusic.magictiles
#     *Pou : me.pou.app
#     Sand Balls: com.water.balls
#     *Meu Talking Tom 2: com.outfit7.mytalkingtom
#     Teste do Minecraft: com.mojang.minecrafttrialpe
#     Run Race - Corrida 3D: com.mgc.runnergame
#     Tiles Hop: Forever Dancing Ball: com.amanotes.beathopper
#     8 Ball Pool: com.miniclip.eightballpool
#     Angry Birds 2: com.rovio.baba

freeFireName= 'com.dts.freefireth'
dfFreefire = porUso(agrupando(freeFireName))
export_csv = dfFreefire.to_csv ('Garena_Free_Fire.csv', header=True)

# funRaceName= 'com.slippy.linerusher'
# dfFunRace = porUso(agrupando(funRaceName))
# export_csv = dfFunRace.to_csv ('Fun_Race_3D.csv', header=True)
