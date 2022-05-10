arquivo = open("arquivo.txt", "r", encoding= 'UTF-8')

lista = ['a', 'e', 'i', 'o', 'u']
soma = 0

for i in arquivo:
    for x in i:
        if x in lista:
            soma += 1

print(soma)
arquivo.close()