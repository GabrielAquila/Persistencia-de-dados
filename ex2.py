# Exercício 02

# Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório de todos os números contidos no arquivo.

arquivo = open("numero.txt", "r", encoding= 'UTF-8')

soma = 0
for linha in arquivo:
    inter = int(linha)
    soma += inter
    print(soma)

arquivo.close()