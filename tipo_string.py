"""
Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre '_',"_",'''_''' e
"""
#"""_""".

#nome = """Danilo"""
#print(nome)
#print(type(nome))

#nome = "Danilo's Bar"
#print(nome)
#print(type(nome))

#nome = "Danilo's \nBar"
#print(nome)
#print(type(nome))

nome = 'Danilo Cardoso'
#print(nome.upper())
#rint(nome.lower())
print(nome.split()[0])
print(nome[0:6]) #Transforma em uma lista de strings
"""
[::-1] -> Comece do primeiro elemento até o último e inverta
"""
print(nome[::-1]) # Inversão da string Pythonico

print(nome.replace('D','v'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])