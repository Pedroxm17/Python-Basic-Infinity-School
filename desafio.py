from random import randint


random_number = randint(0, 30)
aux = 1
num = int(input('Digite o numero aleatorio '))



while (num != random_number):
    num = int(input('Digite outro numero aleatorio '))
    aux = aux + 1
    if num > random_number:
     print('O numero que voce digito e maior ')
    else:
     print('O numero digitado e menor que o numero aleatorio') 
    
    
   


print('O total do numeros inseridos e: ', aux)
print('Fin do Programa')

