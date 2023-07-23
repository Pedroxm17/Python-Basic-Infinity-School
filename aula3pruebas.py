notas = 0
media_notas = 0
Maior_notas = 0
Menor_notas = 100
Notas_finales = []
estado_aluno = []
nome_lista = []
notas = []

for count in range (1,8):
   nomes = input(f'Digite nome aluno nro# {count} ')
   nome_lista.append(nomes)
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
           estado_aluno.append(status_aluno)
else:
    
            status_aluno = 'Aprobado'
            estado_aluno.append(status_aluno)
   
lista = {'nomes_alunos' : nome_lista,
         'notas_alunos' : Notas_finales,
         'Maior': Maior_notas,
         'Menor': Menor_notas,
        'Media': media,
        'status': estado_aluno
                  
   }


for key, value in lista.items():
    print(f'{key} - {value}')

   
