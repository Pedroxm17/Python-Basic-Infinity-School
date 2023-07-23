# user_name = input('Digite seu nome: ')
# user_sobrenome = input('Digite seu sobrenome: ')
# user_idade = float(input('Digite sua idade: '))
# user_email = input('Digite seu email: ')

# user_data = {
    
#     'name': user_name,
#     'sobrenome': user_sobrenome,
#     'idade': user_idade,
#     'email': user_email
# }

# for k, v in user_data.items():
#     print(f'{k} - {v}')

notas = 0
media_notas = 0
Maior_notas = 0
Menor_notas = 100
Notas_finales = []
status_aluno = []
nome = input(f'Digite nome aluno: ')
for count in range (1,5):
   notas = float(input(f'Digite a nota # {count} '))
   Notas_finales.append(notas)
   
   media_notas = notas + media_notas

   if(Menor_notas> notas):
       Menor_notas = notas

   
   if(Maior_notas < notas ):
       Maior_notas = notas   

media = (media_notas / 4)
if(media <7):
          
           status_aluno = 'Reprobado'
else:
    
            status_aluno = 'Aprobado'
   
lista = {'nomes_alunos' : nome,
         'notas_alunos' : Notas_finales,
         'Maior': Maior_notas,
         'Menor': Menor_notas,
        'Media': media,
        'status': status_aluno
                  
 

   }

print(lista)
   

    