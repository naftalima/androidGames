import pandas as pd
import numpy as np

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
    csv = games[i] + '.csv'
    df = pd.read_csv(csv)
    print('Jogo: ', gamesLegend[i])
    print('Mean:')
    print(df.mean())
    print('Median:')
    print(df.median())
    print('Standard deviation:')
    print(df.std())
    print("----------------------------------")

# ('Jogo: ', 'Tiles Hop: Forever Dancing Ball')
# Mean:
# Battery_Used          0.064615
# ElapsedTimestamp    693.807692
# dtype: float64
# Median:
# Battery_Used          0.02
# ElapsedTimestamp    146.50
# dtype: float64
# Standard deviation:
# Battery_Used           0.100369
# ElapsedTimestamp    1239.015674
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'aquapark.io')
# Mean:
# Battery_Used          0.061053
# ElapsedTimestamp    597.263158
# dtype: float64
# Median:
# Battery_Used          0.05
# ElapsedTimestamp    331.00
# dtype: float64
# Standard deviation:
# Battery_Used          0.054456
# ElapsedTimestamp    662.978619
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'Garena Free Fire')
# Mean:
# Battery_Used           0.117455
# ElapsedTimestamp    1924.367183
# dtype: float64
# Median:
# Battery_Used          0.05
# ElapsedTimestamp    510.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.155721
# ElapsedTimestamp    6226.076824
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'Subway Surfers')
# Mean:
# Battery_Used           0.062542
# ElapsedTimestamp    2245.888361
# dtype: float64
# Median:
# Battery_Used          0.04
# ElapsedTimestamp    362.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.063128
# ElapsedTimestamp    9803.253742
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'Run Race - Corrida 3D')
# Mean:
# Battery_Used           0.087586
# ElapsedTimestamp    3150.637931
# dtype: float64
# Median:
# Battery_Used          0.03
# ElapsedTimestamp    493.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.146638
# ElapsedTimestamp    6498.677770
# dtype: float64
# ----------------------------------
# ('Jogo: ', '8 Ball Pool')
# Mean:
# Battery_Used           0.140544
# ElapsedTimestamp    1783.736402
# dtype: float64
# Median:
# Battery_Used          0.07
# ElapsedTimestamp    612.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.162734
# ElapsedTimestamp    4551.628064
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'ROBLOX')
# Mean:
# Battery_Used           0.107182
# ElapsedTimestamp    3530.627273
# dtype: float64
# Median:
# Battery_Used          0.045
# ElapsedTimestamp    387.000
# dtype: float64
# Standard deviation:
# Battery_Used            0.148248
# ElapsedTimestamp    11752.836599
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'Angry Birds 2')
# Mean:
# Battery_Used           0.036667
# ElapsedTimestamp    2820.266667
# dtype: float64
# Median:
# Battery_Used          0.02
# ElapsedTimestamp    223.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.049377
# ElapsedTimestamp    7274.800031
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'PUBG MOBILE LITE')
# Mean:
# Battery_Used           0.183721
# ElapsedTimestamp    3156.930233
# dtype: float64
# Median:
# Battery_Used           0.11
# ElapsedTimestamp    1230.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.184520
# ElapsedTimestamp    7066.455579
# dtype: float64
# ----------------------------------
# ('Jogo: ', 'Magic Tiles 3')
# Mean:
# Battery_Used           0.045517
# ElapsedTimestamp    1746.931034
# dtype: float64
# Median:
# Battery_Used          0.03
# ElapsedTimestamp    280.00
# dtype: float64
# Standard deviation:
# Battery_Used           0.042053
# ElapsedTimestamp    5054.294715
# dtype: float64
# ----------------------------------