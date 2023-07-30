lista_alunos = [
    {
        'id': 1,
        "nome": 'Renato'
    },
    {
        'id': 2,
        "nome": 'Luciana'
    },
]

#CRUD

#POST
#criar una funçao que coloca a aluna joana(letra minuscula) na lista

def inserir(numero_id:int, nombre:str):
    ingresar_nome = {'id':id, 'nome':nome}
    return ingresar_nome

id = 3
nome = 'joana'

lista_alunos.append(inserir(id, nome))

print(lista_alunos)


#read\get
# criar uma função que leia todos os alunos e imprima

def get_alunos(lista):
    return lista
 
print(get_alunos(lista_alunos))

    

#read\get
# criar uma função que leia por id todo o aluno e imprima

def get_by_id(id:str):
    id_int = int(id) - 1
    return lista_alunos[id_int]

print(get_by_id(3))
    
#POST
#criar una funçao que atualiza a aluna joana na lista com a primeira letra maiuscula

def update_aluno(id:str, nome:str):
    id_int = int(id) - 1
    aluno_update = lista_alunos[id_int]
    aluno_update['nome'] = nome
    return lista_alunos


print(update_aluno(3,'joana'))

#delete
#criar uma função que

def delete_by_id(id:str):
    id_int = int(id)
    lista_alunos.pop(id_int-1)

    return lista_alunos

print(delete_by_id(1))
   
# id_delete = 3
# lista_alunos.pop(id_delete-1)
# print(lista_alunos)