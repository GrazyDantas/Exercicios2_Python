#Implemente um gerador de senhas seguras com diferentes critérios e validação.

minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAIUSCULAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?']

valida = False
while (valida == False):
    senha = input("Digite a senha para validação: ")

    tem8 = False
    temMin = False
    temMai = False
    temNum = False
    temSimb = False

    if (len(senha) >= 8):
        tem8 = True

    i = 0
    while (i < len(senha)):
        caractere = senha[i]

        if (temMin == False):
            j = 0
            while (j < len(minusculas)):
                if (caractere == minusculas[j]):
                    temMin = True
                    break
                j += 1

        if (temMai == False):
            j = 0
            while (j < len(MAIUSCULAS)):
                if (caractere == MAIUSCULAS[j]):
                    temMai = True
                    break
                j += 1

        if (temNum == False):
            j = 0
            while (j < len(numeros)):
                if (caractere == numeros[j]):
                    temNum = True
                    break
                j += 1
                
        if (temSimb == False):
            j = 0
            while (j < len(simbolos)):
                if (caractere == simbolos[j]):
                    temSimb = True
                    break
                j += 1

        i += 1

        temTudo = True
        if tem8 == False:
            print("A senha deve ter no mínimo 8 caracteres")
            temTudo = False
        elif temMin == False:
            print("A senha deve ter pelo menos uma letra minúscula")                            
            temTudo = False
        elif temMai == False:
            print("A senha deve ter pelo menos uma letra maiúscula")
            temTudo = False
        elif temNum == False:
            print("A senha deve ter pelo menos um número")
            temTudo = False
        elif temSimb == False:
            print("A senha deve ter pelo menos um caractere especial")
            temTudo = False
        elif temTudo == True:
            print("A senha é forte e válida")
            valida = True
        else:
            print("Tente uma senha diferente")