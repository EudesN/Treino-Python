aluno1 = ['Maria', 'F','Ciência da Computação','Laboratório de Programação', 9]
aluno2 = ['Carla', 'F','Ciência da Computação', 'Engenharia de Software I', 8.5]
aluno3 = ['Ana', 'F','Ciência da Computação','Compiladores', 7.7]
aluno4 = ['Francisco', 'M', 'Ciência da Computação', 'Probalidade e Estatística', 10]
aluno5 = ['Pedro', 'M', 'Matemática', 'Algebra I', 7]
aluno6 = ['Joana', 'F','Matemática', 'Algebra I', 7]
aluno7 = ['Roberto','M','Física', 'Física I', 9]
aluno8 = ['Daniele', 'F', 'Física', 'Física II', 5.8]

# Crie uma lista contendo os 8 alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8]

# Crie uma listra contendo apenas os alunos do Curso de Ciência da Computação

lista_alunos_computacao = []

for aluno in lista_alunos:
    if aluno[2]  == 'Ciência da Computação':
        lista_alunos_computacao.append(aluno[0])

# Crie uma lista contendo apenas os alunos de matemática
lista_alunos_matematica = []

for aluno in lista_alunos:
    if aluno[2] == 'Matemática':
        lista_alunos_matematica.append(aluno[0])


# Crie uma lista contendo apenas os alunos de física
lista_alunos_fisica = []
for aluno in lista_alunos:
    if aluno[2] == 'Física':
        lista_alunos_fisica.append(aluno[0])


# Crie uma lista contendo apenas os alunos homens
lista_alunos_homens = []

for aluno in lista_alunos:
    if aluno[1] == 'M':
        lista_alunos_homens.append(aluno[0])

# crie uma lista contendo apenas as alunas mulheres
lista_alunas_mulheres = []

for aluno in lista_alunos:
    if aluno[1] == 'F':
        lista_alunas_mulheres.append(aluno[0])

# crie uma lsita contendo apenas alunos com notas superiores a 7
lista_alunos_maior_7 = []

for aluno in lista_alunos:
    if aluno[4] > 7:
        lista_alunos_maior_7.append(aluno[0])

# Crie uma lista na ordem alfabética crescente contendo os 8 alunos
lista_alunos_crescente = []

for aluno in lista_alunos:
    lista_alunos_crescente.append(aluno[0])
lista_alunos_crescente.sort()

# Crie uma lista na ordem alfabética decrescente contendo os 8 alunos
lista_alunos_decrescente = []

for aluno in lista_alunos:
    lista_alunos_decrescente.append(aluno[0])
lista_alunos_decrescente.sort(reverse= True)

print("Alunos matriculados em Matemática:", lista_alunos_matematica)
print("Alunos matriculados em Ciência da Computação:", lista_alunos_computacao)
print("Alunos matriculados em Física:", lista_alunos_fisica)
print("As alunas mulheres são:", lista_alunas_mulheres)
print("Os alunos homens são:", lista_alunos_homens)
print("Os alunos com média maior que 7:", lista_alunos_maior_7)
print("Ordem Crescente:", lista_alunos_crescente)
print("Ordem Decrescente:", lista_alunos_decrescente)