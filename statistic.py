import pandas as pd
import numpy as np
import math

games = ['com.amanotes.beathopper', 'com.cassette.aquapark',
         'com.dts.freefireth', 'com.kiloo.subwaysurf',
         'com.mgc.runnergame','com.miniclip.eightballpool',
         'com.roblox.client', 'com.rovio.baba' 	,
         'com.tencent.iglite', 'com.youmusic.magictiles', 'me.pou.app']

gamesLegend = [ 'Tiles Hop: Forever Dancing Ball','aquapark.io',
                'Garena Free Fire','Subway Surfers',
                'Run Race - Corrida 3D','8 Ball Pool', 
                'ROBLOX', 'Angry Birds 2',
                'PUBG MOBILE LITE','Magic Tiles 3','Pou']

for i in range(len(games)-1):
    print(gamesLegend[i])
    csv = 'data/' + games[i] + '.csv'
    df = pd.read_csv(csv)
    perSecond = []
    for index, row in df.iterrows():
        perSecond.append(np.divide(row['Battery_Used'],row['ElapsedTimestamp']).tolist())
        print(type(np.divide(row['Battery_Used'],row['ElapsedTimestamp'])))
    print(perSecond)
    break

    # , df.mean(),'median',df.median())
