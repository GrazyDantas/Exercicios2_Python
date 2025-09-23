#Desenvolva um sistema de notas que calcule média, identifique aprovação/reprovação e trate entradas inválidas
try:
    p1 = float(input("Digite a sua nota da P1: "))  
    p2 = float(input("Digite a sua nota da P2: "))
    if (p1 < 0 or p2 < 0 or p1 > 10 or p2 > 10):
        print("A nota deve ser entre 0 e 10")
    else:
        media = (p1 + p2) / 2

    if (media > 6):
        print("A sua média é:", media,", aprovado!")
    else:
        print("A sua média é:", media,",reprovado")
except:
        print("Por favor digite apenas números!")