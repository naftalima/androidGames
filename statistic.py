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
               'CLash Royale',
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

porSegundo = []
for i in range(len(games)-1):
    print(gamesLegend[i])
    csv = 'data/' + games[i] + '.csv'
    df = pd.read_csv(csv)
    perSecond = []
    for index, row in df.iterrows():
        minuto = row['Battery_Used'] * 1000
        print('veio',minuto)
        minuto = minuto / 60
        print(minuto)
    break


        # print(row['ElapsedTimestamp'])
        # minuto = np.divide(np.floor(row['ElapsedTimestamp']*100000),60)
        # minuto = np.divide(minuto,100000)
        # print('minutos: ', minuto)
        # print('Descarregou:' ,row['Battery_Used'])
        # number = np.divide(np.divide(np.multiply(row['Battery_Used'],100000),minuto),100000)
        # print('Por Segundos:',number)
        