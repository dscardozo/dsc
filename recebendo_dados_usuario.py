"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
-Aspas simples; ('Danilo')
-Aspas duplas; ("Danilo")
-Aspas triplas; ('''Danilo''')
"""
#-Aspas duplastriplas; ("""Danilo""")

#entrada de dados

print("Qual o seu nome? ")
nome = input() #Input -> entrada

# Exemplo de print 'antigo 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de print moderno 3.x
# Exemplo de print 'mais atual'  3.7
print(f'Seja bem-vindo(a) {nome}')

#print("Qual a sua idade? ")
idade = int(input('Qual a sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print moderno 3.x
#print('O {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual'  3.7
print(f'O {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'O {nome} nasceu em {2021 - int(idade)}')