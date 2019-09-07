a = [0.4,0.2, 0.19, 0.18, 0.18, 0.35, 0.34, 0.31,0.30,0.29,0.28,0.9]
inicio = []
fim = []
print(a)
for i in range(len(a)-1):
    diff=a[i+1]-a[i]

    print("final - inicial = ",a[i+1],"-",a[i],"=",diff)

    if i == 0:
        print("START")
        print("inicio: ",a[i])
        inicio.append(a[i])
    
    if diff < - 0.03 or diff > 0.0:
        print("STOP")
        print('fim: ',a[i],'|| inicio:', a[i+1])
        inicio.append(a[i+1])
        fim.append(a[i])

    if i == len(a) -2:
        print("END")
        print('fim: ',a[i+1])
        fim.append(a[i+1])    

    


print("inicio: ", inicio, "LEN:", len(inicio))
print("fim: ", fim, "LEN:", len(fim))