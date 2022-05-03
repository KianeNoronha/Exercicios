from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram: ', end='')
for num in n:
    print(f'{num}', end=' ')

print(f'\n O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')