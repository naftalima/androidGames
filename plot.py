import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

games = ['com.amanotes.beathopper', 'com.cassette.aquapark',
         'com.dts.freefireth.', 'com.kiloo.subwaysurf',
         'com.mgc.runnergame','com.miniclip.eightballpool',
         'com.roblox.client', 'com.rovio.baba' 	,
         'com.tencent.iglite', 'com.youmusic.magictiles', 'me.pou.app']

df = pd.read_csv('com.kiloo.subwaysurf.csv')

# df.plot.scatter(x='ElapsedTimestamp', y="Battery_Used")
df.plot(kind='scatter',x='ElapsedTimestamp',y='Battery_Used',color='red')
plt.show()