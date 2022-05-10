# Exercício 01

# Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada linha).
arquivo = open("numero.txt", "a", encoding= 'UTF-8')

for linha in range(10):
    numero = input('Informe o numero: ')
    arquivo.write( str(numero) + '\n')
arquivo.close()
