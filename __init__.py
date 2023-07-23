def soma(num1, num2):
    total = num1 + num2
    return total

def quadrado(num):
    total1 = num ** 2
    return total1

def area(largura, altura, tipo):
    if tipo == 1:
        calculo_area = largura * largura
    elif tipo == 2:
        calculo_area = largura * altura
        
    elif tipo == 3:
        calculo_area = (largura * altura) / 2
    
    else:
        calculo_area = 'Tipo incompativel'
        
    return calculo_area

def letras(texto):
    total_letras = len(texto)
    espacios = 0
    signos = 0
    for i in texto:
        if i == " ":
            espacios = espacios + 1
            
        elif i == "?" or i == "." or i =="," or i  == '!' or i == ';':
            signos + 1
    
        
        
       
    return total_letras

def fatorial(num1):
    total_fatorial = (num1 * num1) * num1
    return total_fatorial
