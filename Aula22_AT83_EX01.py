pares=[]

nu1=int(input("Digite o primeiro valor: "))
nu2=int(input("Digite o segundo valor: "))
nu3=int(input("Digite o terceiro valor: "))
nu4=int(input("Digite o quarto valor: "))

lista=nu1,nu2,nu3,nu4


nove=(lista.count(9))
tres=(lista.index(3))

for index in range(0,len(lista)):
    if lista[index]%2==0:
        pares.append(lista[index])

result=input(f'O número nove apareceu {nove} vezes diante os números ditos. \nJá o número três apareceu {tres} \n{pares} foram ditos os números pares.')