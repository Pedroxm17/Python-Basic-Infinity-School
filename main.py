height = float(input('Digite a altura: '))
gender = input('Digite seu sexo: ')

if (gender == 'f'):
    weight = (62.1 * height) - 44.7
      
elif (gender == 'm'):
    weight = ( 72.7 * height) - 58
    
else:
    
    error = 'y'

if (error == 'y'):
   print('sexo invalido. impossivel calcular')
else:
    print('O peso Ideal e ', weight)
    


 
    

    
 
    


