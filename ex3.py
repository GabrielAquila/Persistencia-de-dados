# Exercício 03

# Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário grave diversos caracteres nesse arquivo até que o mesmo entre com o caractere “0” (zero). 

arquivo = open("arquivo.txt", "a", encoding= 'UTF-8')


caract = input('Informe uma caractere: ')
while caract != 0:
    caract = input('Informe uma caractere: ')
    arquivo.write( str(caract) + '\n')
    if caract == str(0):
        break
arquivo.close()