from random import choice
from random import shuffle

lista=[]

while True:
    lista=str(input('Digite o nome das pessoas que compraram a rifa (quando quiser parar digite 0): '))
    lista.append(lista)
    if lista=='0':
        break

shuffle(lista)
ale=choice(lista)
print(f'A pessoa sorteada foi {ale}')