# vamos printar 3 listas 

a = ['a1','a2', 'a3', 'a4', 'a5', 'a6', 'a7']
b = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7']
c = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']


for i in range (7):

    print(a[i] + ' ' + b[i] + ' ' + c[i])


resposta1 = (input('Escolha uma carta e digite em qual fileira está: (a, b ou c) '))


if (resposta1=='a'):

    lista1 = b+a+c
   
if (resposta1=='c'):

    lista1 = a+c+b

if(resposta1=='b'):
    lista1 = a+b+c


contador = 3
lista2 = [lista1[i::contador] for i in range(7)]

a = lista2[0]
b = lista2[1]
c = lista2[2]

for i in range(7):

    print(a[i] + ' ' + b[i] + ' ' + c[i])

resposta2 = (input('Digite em qual fileira está AGORA: (a, b ou c) '))

if (resposta2 == 'a'):

    lista3 = b+a+c
   
if (resposta2 == 'c'):

    lista3 = a+c+b

if(resposta2 =='b'):
    lista3 = a+b+c

contador = 3
lista4 = [lista3[i::contador] for i in range(7)]

a = lista4[0]
b = lista4[1]
c = lista4[2]


for i in range(7):

    print(a[i] + ' ' + b[i] + ' ' + c[i])

resposta3 = (input('Digite em qual fileira está AGORA: (a, b ou c) '))

if (resposta3 == 'a'):

    lista5 = b + a + c
   
if (resposta3 == 'c'):

    lista5 = a + c + b

if(resposta3 == 'b'):
    lista5 = a + b + c

print('sua escolha foi ' + lista5[10]) 
