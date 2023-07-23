# def hello(name):
#     return f' Hello, {name}, welcome back'

# greeting_msg = hello('Silvia')
# print(greeting_msg)

# def sum(num1, num2):
#     total = num1 + num2
#     return total
   
# result = sum(3,5)
# print(f' Resultado da soma {result}')

# def student_condicion(grade1: float, grade2: float, grade3: float, grade4: float):
#     average = (grade1 + grade2 + grade3 + grade4) / 4
#     if (average >7):
#         return 'Aprovado'
#     else:
#         return 'Reprobado'

# result = student_condicion(6, 8, 5, 5)
# print(f'Situaçao do aluno {result}')

#Resltado
personas_peso = []
personas_altura = []
resultado = []
def peso_altura(personas_peso, personas_altura):
    imc = personas_peso / (personas_altura ** 2)
    return imc

for i  in range (1, 5):
    peso = float(input('Digite seu Peso '))
    altura = float(input('Digite sua altura '))
    personas_peso.append(peso)
    personas_altura.append(altura)
    result = peso_altura(peso, altura)
    resultado.append(result)
    print(f'O imc do Usuario ', i, 'e', result)
    print(resultado)


    