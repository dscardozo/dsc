"""
                    Ranges
 - Precisamos conhecer o loop for para usar os ranges.
 - Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória,
mas sim de maneira especificada.

    Formas Gerais:

     #Forma 1

range(valor_da_parada)

OBS: valor_da__parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma1
for num in range(11):
    print(num)

    #Forma 2

range(valor_de_inicio, valor_de_parada)


for num in range(1, 11):
    print (num)

    #Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_da__parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo 3

for num in range(0, 55, 5):
    print(num)




    #Forma 4 (Inversa)

range(valor_inicio, valor_de_parada, passo)

# Exemplo 4

for num in range(10, -1, -1):
    print(num)


"""




