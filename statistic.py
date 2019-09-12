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

def Medicoes():
    medidas = []
    ### nome, media, mediana, desvio padrao
    for i in range(len(games)-1):
        csv = 'data/' + games[i] + '.csv'
        df = pd.read_csv(csv)
        list_porMin = []
        for index, row in df.iterrows():
            minuto =   np.divide(row['ElapsedTimestamp'] , 60 )
            porMin = np.divide(row['Battery_Used'], minuto)
            list_porMin .append(porMin)
        medidas.append([gamesLegend[i],np.mean(list_porMin),np.median(list_porMin),np.std(list_porMin)])
    return(medidas)


def VioBoxPlt()
    data={'nome': []}
    for i in range(len(games)-1):
        csv = 'data/' + games[i] + '.csv'
        df = pd.read_csv(csv)
        perSecond = []
        for index, row in df.iterrows():
            minuto =   np.divide(row['ElapsedTimestamp'] , 60 )
            porSegundo = np.divide(row['Battery_Used'], minuto)
            perSecond.append(porSegundo)
        data[gamesLegend[i]] = perSecond
    del data['nome']

    fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(9,4))
    axes[0].violinplot(data['Garena Free Fire'], showmeans = False, showmedians=True)
    axes[0].set_title('Violin plot')

    axes[1].boxplot(data['Garena Free Fire'])
    axes[1].set_title('Box plot')

    return(plt.show())

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




# print(Medicoes())
# [
# ['Garena Free Fire', 0.012170479054470839, 0.007629020194465219, 0.026555653153621014],
#  ['CLash Royale', 0.007801094621036076, 0.004868191372439386, 0.015021152152397514], 
#  ['Pokémon GO', 0.006743040423301644, 0.006507142857142856, 0.004451988563760966],
#  ['Clash of Clans', 0.009341849467959983, 0.006666666666666671, 0.014311391763193966],
#  ['Candy Crush Saga', 0.032623590247064106, 0.005660377358490563, 0.10748828068021696],
#  ['Mobile Legends- Bang Bang', 0.011013458566150556, 0.00759493670886076, 0.015791555627991453], 
#  ['PUG MOBILE', 0.020856744254217838, 0.011941225333279307, 0.05742843748470973], 
#  ['8 Ball Pool', 0.011568850585342237, 0.00757193336698637, 0.015350708799005583], 
#  ['Township', 0.010753715332584015, 0.007174887892376678, 0.014464733809207183],
#  ['Candy Crush Soda Saga', 0.06238340100487589, 0.023076923076922964, 0.11950605788318647], 
#  ['Subway Surfers', 0.010496265251695062, 0.007029529694306497, 0.017205487064180597]
# ]