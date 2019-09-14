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

color = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple',
         'tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan',
         'deeppink','yellow']


def por_minuto():
    """Normalizando os dados por uso em qnto % de bateria é utilizado por minuto"""
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

def vio_box(n):
    data = por_minuto()

    fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(9,4))

    axes[0].violinplot(data[gamesLegend[n]], showmeans = False, showmedians=True)
    axes[0].set_title('Violin plot')

    axes[1].boxplot(data[gamesLegend[n]])
    axes[1].set_title('Box plot')

    plt.show()
    return()

def scatter():
    ax = plt.gca()
    for i in range(len(games)-1):
        csv = 'data/' + games[i] + '.csv'
        df = pd.read_csv(csv)
        ax = df.plot(kind='scatter',x='ElapsedTimestamp',y='Battery_Used',color=color[i],label=gamesLegend[i],ax=ax)
    plt.show()
    return()

