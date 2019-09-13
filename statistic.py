import pandas as pd
import numpy as np
import math
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
    metricas = {'jogo':['media','mediana','desvio_padrao']} #{'nome': media, mediana, desvio_padrao}
    for i in gamesLegend:
        metricas[i] = [np.mean(dado[i]),np.median(dado[i]),np.std(dado[i])]
    return(metricas)


data = por_minuto() # df = pd.DataFrame.from_dict(data) #ValueError: arrays must all be same length
# print(data.keys())

n = 1
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(9,4))

axes[0].violinplot(data[gamesLegend[0]]), showmeans = False, showmedians=True)
axes[0].set_title('Violin plot')

axes[1].boxplot(data[gamesLegend[0]])
axes[1].set_title('Box plot')

plt.show()

# medidas = Medicoes(data)
# print(medidas)

# {'jogo': ['media', 'mediana', 'desvio_padrao'],
#  'Garena Free Fire': [0.009903134923123488, 0.007428685683817649, 0.008591887075332936],
#  'CLash Royale': [0.006153860128782758, 0.004800000000000003, 0.005568869438875517],
#  'Pokémon GO': [0.006743040423301644, 0.006507142857142856, 0.004451988563760966],
#  'Clash of Clans': [0.007800643231207369, 0.006666666666666637, 0.0062687925898687585],
#  'Candy Crush Saga': [0.008836041931589477, 0.005125467164975972, 0.009271498156189993],
#  'Mobile Legends- Bang Bang': [0.009396748890152419, 0.007484798145043008, 0.007145288454864934],
#  'PUG MOBILE': [0.013220770893705153, 0.011501714845663879, 0.010478974369538156],
#  '8 Ball Pool': [0.008767966430073017, 0.0075000000000000075, 0.006155757649017347],
#  'Township': [0.009720163002845799, 0.00710084033613446, 0.008049447293382134],
#  'Candy Crush Soda Saga': [0.017144963977093093, 0.015409187709157291, 0.013083622789410816],
#  'Subway Surfers': [0.007806103634012653, 0.006666666666666653, 0.006344042847891743],
#  'Temple Run 2': [0.01270062048451816, 0.008571428571428572, 0.009605317898837156]
#  }

#
# for key in data:
#     data[key].sort()
#     t = 0
#     for x in data[key]:
#       print(x)
#       if x <= 0.05:
#         t+=1
#     print(t)
#     break


