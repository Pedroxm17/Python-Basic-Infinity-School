'''problema
faca uma progama que pessa o nome do usuario
se o nome for 'prata': que nome bonito 
se se o nome for 'faustao 
nome = input('digite o nome do usuario:')
if nome == 'Prata':
    print('nome bonito!!')
elif nome == 'faustao':
    print('o loca meu')
    elif nome == 'carol' or nome == 'joyce'
    print('f ola {nome}tudo bem?')
else:
    print('nome sem identificação')
'''
'''1. Escreva um programa para aprovar ou não o empréstimo bancário da compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar o imóvel. 
O valor da prestação não poderá exceder 30% do salário, caso exceda, o empréstimo será negado'''

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o salário do comprador: "))
anos_pagamento = int(input("Digite em quantos anos será feito o pagamento: "))

valor_prestacao = valor_casa / (anos_pagamento * 12)  # Valor da prestação mensal
limite_prestacao = salario_comprador * 0.3  # 30% do salário

if valor_prestacao <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f'o valor da pestação é: {valor_prestacao}')
    
else:
    print("Empréstimo negado!")
    print(print(f'o valor da pestação é: {valor_prestacao}'))

    
''' 2. Faça um programa que leia dois números inteiros e os compare, mostrando na tela somente uma das seguintes mensagens: 
O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois números são iguais.'''
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro valor é maior.")
elif numero2 > numero1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois números são iguais.")
    


    
