#Crie um programa que valide um número de telefone brasileiro e formate-o corretamente usando try/except

tel = input("Digite o seu número de telefone: ")
tellen = len(tel)

try:
    if (tellen != 11):
            print("Digite todos os números")
    else:
        tel = int(tel)
        tel = str(tel)
        telFormatado = '({}) {}-{}'.format(tel[0:2], tel[2:7] ,tel[7:])
        print(telFormatado)
except:
     print("digite apenas números!")