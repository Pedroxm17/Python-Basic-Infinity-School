weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura: '))

imc = weight / (height * height)

if (imc < 18.5):
    print("Abaixo do peso ideal")
elif (imc >= 18.5 and imc <= 24.9):
    print("Peso ideal")
elif (imc >= 25 and imc <= 29.9):
    print("Levemente acima do peso")
    
else:
    print('Obesidade grau 1')
    

print(imc) 
    
