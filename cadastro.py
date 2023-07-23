# aux = 0
# for count in range(0,5):
#     usuario = input('Digite seu mail ')
#     senha = input('Digite sua senha ')
#     senha2 = input('Confirme sua senha ')
#     aux = aux + 1
#     while(senha != senha2):
#          print('As senhas Não concordan, Porfavor Digite novamente.')
#          senha = input('Digite sua senha ')
#          senha2 = input('Confirme sua senha ')
    
#     print('Usuario numero', aux, 'Cadastrado!')
    

num = int(input('Digite un numero:'))


for count in range (1,11):
    
    
    total= num * count
    print(num,' x ',count,' = ', total)