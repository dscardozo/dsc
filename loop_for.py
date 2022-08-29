"""

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

            C ou Java
for(int i = 0; i < 10; i++){
    //execução do loop
}

            Python

for item in interavel:
    //execução do loop


            Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exmplos de iteráveis:
 - String
    nome = 'Geek University'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)
"""

            #Exemplo de for 1 (Iterando em uma string)
""""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista
"""
"""

for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando em uma lista)

for numero in lista:
    print(numero)
"""
            #Exemplo de for 3 (Iterando em uma range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não inclusive

for numero in range(1, 10):
    print(numero)

"""
"""
            Enumerate
            
Enumerate:

((0, 'G'), ((1, 'e')), ((2, 'e')), ((3, 'k')), ((4, ' ')), ((5, 'U'), ....

for indice, letra in enumerate(nome):
    print(nome[indice])


for indice, letra in enumerate(nome):
    print(letra)



for _, letra in enumerate(nome):
    print(letra)

    OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)



for valor in enumerate(nome):
    print(valor)

"""
"""
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


nome = 'Geek University'
for letra in nome:
    print(letra, end='')  #Sem pular linha


                Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal
"""

# Original: U+1F601
# Modificado: U0001F601
emoji = 'U0001F601'

for x in range(3):
    for num in range(1, 11):
        print(f'\U0001F601' * num)

