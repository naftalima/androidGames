import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

color = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple',
         'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','deeppink']

ax = plt.gca()
for i in range(len(games)-1):
    csv = games[i] + '.csv'
    df = pd.read_csv(csv)
    # df = df['Battery_Used'].round(decimals=3)
    ax = df.plot(kind='scatter',x='ElapsedTimestamp',y='Battery_Used',color=color[i],label=gamesLegend[i],ax=ax)
# ax = plt.gca()
# i=6
# csv = games[i] + '.csv'
# df = pd.read_csv(csv)
# # df = df['Battery_Used'].round(decimals=3)
# ax = df.plot(kind='scatter',x='ElapsedTimestamp',y='Battery_Used',color=color[i],label=gamesLegend[i],ax=ax)
# plt.legend(loc='lower left', numpoints=1, bbox_to_anchor=(0.7,0.5))
plt.show()