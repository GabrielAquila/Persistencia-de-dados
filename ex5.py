arquivo = open("arq.txt", "r", encoding='UTF-8')

ano= int(input('digite o ano atual: '))

for i in arquivo:
    pessoa = i.split(' ')
    print(f'>>>{pessoa[0]} {ano - int(pessoa[3])}<<<')

arquivo.close()