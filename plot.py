import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

color = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple',
         'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan',
         'deeppink','yellow']

ax = plt.gca()
for i in range(len(games)-1):
    csv = 'data/' + games[i] + '.csv'
    df = pd.read_csv(csv)
    ax = df.plot(kind='scatter',x='ElapsedTimestamp',y='Battery_Used',color=color[i],label=gamesLegend[i],ax=ax)
plt.show()


