import pandas as pd
import numpy as np
import math

games = ['com.dts.freefireth',
         'com.supercell.clashroyale',
         'com.nianticlabs.pokemongo',
         'com.supercell.clashofclans',
         'com.king.candycrushsaga',
         'com.mobile.legends',
         'com.tencent.ig',
         'com.miniclip.eightballpool',
         'com.playrix.township',
         'com.king.candycrushsodasaga',
         'com.kiloo.subwaysurf',
         'com.imangi.templerun2']

gamesLegend = ['Garena Free Fire',
               'Clash Royale',
               'Pokémon GO',
               'Clash of Clans',
               'Candy Crush Saga',
               'Mobile Legends- Bang Bang',
               'PUG MOBILE',
               '8 Ball Pool',
               'Township',
               'Candy Crush Soda Saga',
               'Subway Surfers',
               'Temple Run 2']


def por_minuto():
    dado={'nome':[]}
    for i in range(len(games)):
        csv = 'data/' + games[i] + '.csv'
        df = pd.read_csv(csv)
        batteryPerMinute = []
        for index, row in df.iterrows():
            minuto = np.divide(row['ElapsedTimestamp'] , 60 )
            batmin =  np.divide(row['Battery_Used'], minuto)
            if batmin < 0.05:# isn't outlier
                batteryPerMinute.append(batmin)
        dado[gamesLegend[i]] = batteryPerMinute
    del dado['nome']
    return(dado)

def Medicoes(dado):
    metricas = {} #{'nome_jogo': media, mediana, desvio_padrao}
    for i in gamesLegend:
        metricas[i] = [np.mean(dado[i]),np.median(dado[i]),np.std(dado[i])]
    return(metricas)

def Maior_Menor(dfMedias):
    print('maior')
    print(dfMedias.idxmax())  
    print(dfMedias.max())
    print('menor')  
    print(dfMedias.idxmin())  
    print(dfMedias.min())
    return()


#-------------------------Main---
data = por_minuto()
medidas = Medicoes(data)
dfm = pd.DataFrame.from_dict(medidas,orient='index')
dfm.columns = ['media','mediana','std']
# print(dfm)
Maior_Menor(dfm)


