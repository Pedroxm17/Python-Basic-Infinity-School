def retorna_info_mesagem(msg):
    total_caracteres = len(msg)
    espacos = 0 
    pontuacoes = 0
    
    for letra in msg:
        if letra == ' ':
            espacos += 1
            
        if letra == '.' or letra == ','  or letra == ':' or letra == ';':
            pontuacoes += 1
            
    quantidade_letras = total_caracteres - espacos - pontuacoes
    
    return quantidade_letras, espacos, pontuacoes


minha_mensagem = input('Digite uma mensagem ')

totais_caracteres = retorna_info_mesagem(minha_mensagem)

print(totais_caracteres)