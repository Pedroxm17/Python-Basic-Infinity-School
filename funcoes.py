from random import randint
#
# def retorna_info_mesagem(msg):
#     total_caracteres = len(msg)
#     espacos = 0 
#     pontuacoes = 0
    
#     for letra in msg:
#         if letra == ' ':
#             espacos += 1
            
#         if letra == '.' or letra == ','  or letra == ':' or letra == ';':
#             pontuacoes += 1
            
#     quantidade_letras = total_caracteres - espacos - pontuacoes
    
#     return quantidade_letras, espacos, pontuacoes


# minha_mensagem = input('Digite uma mensagem ')

# totais_caracteres = retorna_info_mesagem(minha_mensagem)

# print(totais_caracteres)


# def fatorial(num1):
   
#     contador = 1
#     for count in range(1, num1+1):
#         contador *= count
#     return contador


# total = int(input('Digite um Numero: '))

# resultado = fatorial(total)

# print(resultado)

# def sorteo (lista):
#     for i in range (0, 5):
#         numeros = randint(1,10)
#         lista.append(numeros)
#     return lista





# mi_lista = sorteo([])

# def num_par(mi_lista):
#     for count in mi_lista:
#         if(mi_lista[count] % 2 == 0):
#             mi_lista.append(num_par)
#         else:
#             mi_lista.pop([0])
#     return num_par

# print(mi_lista)

# def validacion(msg):
    
#     for count in range(msg):
#         if(count == "@"):
#             print('Email valido')
#         else:
#             print('Email invalido')
            
#     return validacion

# email = str(input('Digite um email'))

# total = validacion(email)

# print(total)

def verifica_email(email):
    count_at = 0
    count_dot = 0 
    posicao_at = 0
    posicao = 0
    for letra in email:
        posicao += 1
        if letra == '@':
            count_at += 1
            posicao_at = posicao
        if letra == '.':
            count_dot += 1
            posicao_dot = posicao
            
    if count_at > 0 and count_dot > 0 and posicao_at < posicao_dot:
        return 'Sucesso!'
    else:
        return 'Email Invalido'
    
email_usuario = input('Digite seu email ')
resultado_validacao = verifica_email(email_usuario)

print(resultado_validacao)
