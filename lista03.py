
# dados = {'nome': 'Luan', 'idade': 35, 'email': 'luan@gmail.com'}

# dados_lista = ['Luan', 35, 'luan@gmail.com']


# # pegar a idade do dicionario dados
# valor_idade = dados['idade']


# print(valor_idade)

# dados['email'] = 'luanferreira@yahoo.com'

# print(dados)

# # introducir mas llaves al diccionario
# dados['Empresa'] = 'Infinity School'

# print(dados)

# #lista retorna as chaves daquele diccionario
# print(list(dados))

# #remove uma determinada chave do diccionario

# del dados ['email']


# #items retorna uma lista com uma tupla separados chave valor | importante para o for

# print(dados.items())

# for chave, valor in dados.items():
#     print(f'{chave}, -  {valor}')
   
#    #podemos ter uma chave que contenha uma lista 
# dados2 = {
#     'nome': 'Tereza',
#     'idade': 29,
#     'email': 'tereza@gmail.com',
#     'linguagens': ['Python', 'java', 'PHP']
    
# }
# print(dados2)

# for key, value in dados2.items():
#     print(f'{key}, - {value}')
    
    
#criar um programa em python que solicita ao usuario os seus dados nome, sexo, estado civil e naturalidade e armazene num diccionario

user_name = input('Digite seu nome: ')
user_gender = input('Digite seu genero: ')
user_status = input('Digite seu estado civil: ')
user_from = input('Cidade onde nasceu: ')

user_data = {
    
    'name': user_name,
    'gender': user_gender,
    'status': user_status,
    'from': user_from
}
print(user_data)

for key, value in user_data.items:
    print(f'{key} - {value}')

# # update atualiza um valor da chave

# user_data.update({'status': 'solteiro'})