tabela=('Flamengo','Palmeiras','Atlético Mineiro','Grêmio','Athletico Paranaense','Santos','São Paulo','Internacional','Fluminense','Corinthians','Fortaleza','Bahia','Ceará','Cruzeiro','América Mineiro','Atlético Goianiense','Chapecoense','Botafogo','Botafogo','Vasco da Gama','Red Bull Bragantino')

primeiros=tabela[0:5]
ultimos=tabela[16:20]
alf=sorted(tabela)
chap=(tabela.index('Chapecoense'))

print(f'Os cinco primeiros colocados são: \n {primeiros} \nOs 4 últimos colocados são: \n{ultimos} \nOs qualificados postos em ordem alfabética são: \n{alf}\ne o time >CHAPECOENSE< ficou em {chap}º lugar.')