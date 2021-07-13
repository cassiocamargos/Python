'''aluno = {'nome': 'Ana', 'idade': 16, 'nota': 'A', 'aprovação': True}
print(aluno)

aluno['nome'] = 'Jose'
aluno.update({'nome': 'Jose', 'nota': 'B'})
print(aluno)
print(aluno['nome'])

print(aluno.get('endereco'))
print(aluno.get('endereco', 'nao existe'))

aluno.update({'endereco': 'rua a'})
print(aluno.get('endereco', 'nao existe'))

del aluno['idade']
print(aluno)'''



'''aluno = {'nome': 'Ana', 'idade': 16, 'nota': 'A', 'aprovação': True}

for x in aluno:
    print(x)
print()

for x in aluno.keys():
    print(x)
print()

for x in aluno.values():
    print(x)
print()

for x in aluno.items():
    print(x)
print()

for keys, values in aluno.items():
    print(keys, values)'''



'''aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota': 'A', 
    'aprovação': True, 
    'materias': ['matematica', 'fisica', 'ingles']
}

print(aluno)
print(aluno.get('materias'))
print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())'''

