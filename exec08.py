#Crie um programa que simule um jogo da velha com validação de jogadas e detecção de vitória.

L1 = ["_", "_", "_"]
L2 = ["_", "_", "_"]
L3 = ["_", "_", "_"]

fim = False
jogadas = 0
jogador = "X"

while (fim == False):
    print("=========== Jogo da Velha ===========")
    print("   C0  C1  C2")
    print("L1 {} | {} | {}".format(L1[0], L1[1], L1[2]))
    print("L2 {} | {} | {}".format(L2[0], L2[1], L2[2]))
    print("L3 {} | {} | {}".format(L3[0], L3[1], L3[2]))

    jogadaValida = False
    while (jogadaValida == False):
        try:
            linha = int(input(f"Jogador ({jogador}), escolha uma Linha (1, 2, ou 3): "))
            coluna = int(input("Agora escolha uma coluna (0, 1, 2): "))


            if (linha == 1):
                linha = L1
            elif (linha == 2):
                linha = L2
            elif (linha == 3):
                linha = L3
            else:
                print("Linha inválida, tente novamente")
                continue

            if (coluna >= 0 and coluna <= 2):
                if linha[coluna] == "_":
                    linha[coluna] = jogador
                    jogadaValida = True
                    jogadas += 1
                else:
                    print("Posição ocupada, tente novamente")
            else:
                print("Coluna inválida, tente novamente")
        except:
            print("Entrada inválida, tente novamente")

    vencedor = ""

    if (L1[0] == L1[1] and L1[1] == L1[2] and L1[0] != "_"):
        vencedor = L1[0]
    elif (L2[0] == L2[1] and L2[1] == L2[2] and L2[0] != "_"):
        vencedor = L2[0]
    elif (L3[0] == L3[1] and L3[1] == L3[2] and L3[0] != "_"):
        vencedor = L3[0]
    elif (L1[0] == L2[0] and L2[0] == L3[0] and L1[0] != "_"):
        vencedor = L1[0]
    elif (L1[1] == L2[1] and L2[1] == L3[1] and L1[1] != "_"):
        vencedor = L1[1]
    elif (L1[2] == L2[2] and L2[2] == L3[2] and L1[2] != "_"):
        vencedor = L1[2]
    elif (L1[0] == L2[1] and L2[1] == L3[2] and L1[0] != "_"):
        vencedor = L1[0]
    elif (L1[2] == L2[1] and L2[1] == L3[0] and L1[2] != "_"):
        vencedor = L1[2]

    if (vencedor != ""):
        print(f"Parabéns, o jogador ({vencedor}) venceu!")
        fim = True
    elif (jogadas == 9):
        print("O jogo terminou em empate!")
        fim = True

    if (jogadaValida == True):
        if (jogador == "X"):
            jogador = "O"
        else:
            jogador = "X"

print("====== Fim do Jogo ======")
print("   C0  C1  C2")
print("L1 {} | {} | {}".format(L1[0], L1[1], L1[2]))
print("L2 {} | {} | {}".format(L2[0], L2[1], L2[2]))
print("L3 {} | {} | {}".format(L3[0], L3[1], L3[2]))