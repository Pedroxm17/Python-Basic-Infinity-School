sum_of_salary = 0
count_of_people = 0

for count in range(0, 5):
    salary = float(input('Digite seu salario: '))
    num_of_children = int(input("Numero de Filhos: "))
    
if (salary <=1500):
  count_of_people += 1
        
if (num_of_children > 3):
    
  sum_of_salary += salary
    
print(sum_of_salary)