f = open("data/jogos.txt", "r")
games=[]
for line in f:
    linha = line.split(": ")
    games.append([linha[0],linha[1]])
print(games)
f.close() 