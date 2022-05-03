lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maiorvalor=lista[0]
menorvalor=lista[0]
listaPares=[]
ocorrencia=0
mediaElementos=0
somanegativo=0 


for index in range(0,len(lista)):
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]

    if menorvalor>lista[index]:
        menorvalor=lista[index]

    if lista[index]%2==0:
        listaPares.append(lista[index])

    if lista[index]==lista[0]:
        ocorrencia+=1
    mediaElementos+=lista[index]

    if lista[index]<0:
        somanegativo+=lista[index]

mediaElementos/=len(lista)
print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listaPares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média de elementos: {mediaElementos}')
print(f'Números negativos: {somanegativo}')