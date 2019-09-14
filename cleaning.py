import pandas as pd
import numpy as np
import math

#df: data frame
df = pd.read_csv('data/_SELECT_name_battery_level_version_name_device_id_timestamp_FROM_201909111900.csv')
# name, battery_level, version_name, device_id, timestamp

# str into  <class 'pandas._libs.tslib.Timestamp>
df['timestamp'] =  pd.to_datetime(df['timestamp'])

def games_names():
    f = open("data/jogos.txt", "r")
    jogos=[]
    for line in f:
        linha = line.split(": ")
        jogos.append([linha[0],linha[1]])
    f.close()
    for  i in range(len(jogos)):
        jogos[i][1] = jogos[i][1].replace('\n','')
    return(jogos)

def url(jogosnomes):
    urls= []
    for i in jogosnomes:
        urls.append(i[1])
    return(urls)

def GamesMostUsed(listOfGames):
    """Os com mais dados do top 20 da playstore"""
    amount = []
    for i in listOfGames:
        qtd=0
        for index, row in df.iterrows():
            if row["name"] == i:
                qtd+=1
        amount.append(qtd)
        # print(i,"qtd: ",qtd)
    gamesGood = []
    for i in range(len(amount)):
        if amount[i] > 1000:
            gamesGood.append(listOfGames[i])
    return(gamesGood)

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
    """Separando por uso e deletando os repetidos"""
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
    # print("inicio: ", batteryInit, dateInit)
    # print("fim: ",batteryFinal,dateFinal)
    dfJogo['BatteryLevelFinal'] = batteryFinal
    dfJogo['BatteryLevelInitial'] = batteryInit
    dfJogo['TimestampFinal'] = dateFinal
    dfJogo['TimestampInitial'] = dateInit
    # print(dfJogo.head(10))
    batteryused = []
    elapsedtime = []
    for index, row in dfJogo.iterrows():
        battery = np.subtract(row['BatteryLevelInitial'], row['BatteryLevelFinal'] )
        time = np.subtract( row['TimestampFinal'] , row['TimestampInitial'] )
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
    dfJogo = dfJogo.set_index("Battery_Used")
    dfJogo = dfJogo.drop(0, axis=0)

    return(dfJogo)

def exportCSV(gamesList):
    """Exportando cada uso de cada jogo em um csv com nome do jogo"""
    for i in gamesList:
        nameG = i
        dfG = porUso(agrupando(nameG))
        arqName = 'data/' + nameG + '.csv'
        export_csv = dfG.to_csv (arqName, header=True)

#--------------------------MAIN-----------------------#

# games =  url(games_names())
# selected_games = GamesMostUsed(games)
# exportCSV(selected_games)

#########33CRIAR UM DICIONARIO
games =  url(games_names())

for i in games:
    nameG = i
    print(i)
    dictG = agrupando(nameG)
    print(len(dictG),"versoes")
    users = 0
    for key in dictG: #key == versionname
        users += len(dictG[key])
    print(users,"usuarios")

# com.dts.freefireth
# 24 versoes
# 320 usuarios
# com.supercell.clashroyale
# 20 versoes
# 73 usuarios
# com.nianticlabs.pokemongo
# 18 versoes
# 22 usuarios
# com.igg.android.lordsmobile
# 7 versoes
# 8 usuarios
# com.supercell.brawlstars
# 11 versoes
# 31 usuarios
# com.supercell.clashofclans
# 36 versoes
# 144 usuarios
# com.king.candycrushsaga
# 31 versoes
# 54 usuarios
# com.mobile.legends
# 45 versoes
# 318 usuarios
# com.tencent.ig
# 8 versoes
# 37 usuarios
# com.playrix.gardenscapes
# 5 versoes
# 6 usuarios
# com.miniclip.eightballpool
# 15 versoes
# 45 usuarios
# com.playrix.township
# 6 versoes
# 12 usuarios
# jp.konami.duellinks
# 6 versoes
# 6 usuarios
# com.king.candycrushsodasaga
# 12 versoes
# 17 usuarios
# com.rovio.baba
# 9 versoes
# 12 usuarios
# com.hcg.cok.gp
# 0 versoes
# 0 usuarios
# com.king.farmheroessaga
# 10 versoes
# 11 usuarios
# com.youmusic.magictiles
# 15 versoes
# 23 usuarios
# com.kiloo.subwaysurf
# 33 versoes
# 141 usuarios
# com.imangi.templerun2
# 23 versoes
# 43 usuarios
