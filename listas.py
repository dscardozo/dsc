"""
Lista

Listas em Python funcional como vetores?matrizes (arrays)em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagems C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este arra
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

  Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
  Qualquer tipo de dados: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipode dado.

As listas em Python são respresentadas por colchetes: []

    # Podemos facilmente checar se determinado valor está contido na lista

num = 10
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

    # Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

    # Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

    # Adicionar elementos em listas
Para adicionar elementos em listas, utilizamos a função append
print(lista1)
lista1.append(42)
print(lista1)

# OBs: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 51)  # TypeError

lista1.append([8, 3, 1]) #Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')
lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valos adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo valor')
print(lista1)

"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G','e','e','k','','U','n','i','v','e','r','s','i','t','y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')





