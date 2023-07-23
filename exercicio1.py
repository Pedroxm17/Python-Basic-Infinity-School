# series = ['Breaking Bad', 'Game of Thrones', 'The Walking Dead', 'Wandinha', 'Friends', 'Stranger Things', 
#           'Black Mirrors', 'Casa de Papel', 'Prision Break', 'Os aneis do Poder', 'You', 'Panico']

# # print('_' *15 )
# # print('Minha Lista de Series')
# # print('_' *15 )
# # print(f'As 5 Primeias são {series[0:5]}')
# # print('As ultimas 4', series[-4:])

# print(f'Series em ordem alfabetica {sorted(series)}')
# print(f'Stranger Things esta na posição {series.index("Stranger Things")}')

# numbers = [2, 5, 7, 1, 6, 8, 9, 3, 10, 0]
# soma = 0
# max = 0
# min = 0 

# for number in numbers:
#     soma += number
#     if number > max:
#         max = number
        
#     if number < min:
#         min = number
  
# print('A soma e: ',soma)
# print('O Numero Maior e: ',max)
# print('O numero Menor e: ',min)
listapar = []
listaimpar = []
aux = 0
for count in range(0, 10):
  numeros =  int(input('Digite un Numero: '))
  aux+= 1
  if (numeros % 2)==0:
       listapar.append(numeros) 
  else:
           listaimpar.append(numeros)

print(listapar)
print(listaimpar)

    