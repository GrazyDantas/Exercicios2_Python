#Crie um programa que analise uma lista de palavras e encontre anagramas usando manipulação de strings

palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()
letras1 = list(palavra1)
letras2 = list(palavra2)

if len(letras1) != len(letras2):
    print(palavra1,"e",palavra2,"não são anagramas, pois têm tamanhos diferentes")
else:
    i = 0
    while i < len(letras1):
        letra = letras1[i]
        try:
            letras2.remove(letra)
        except: 
            print(palavra1,"e",palavra2,"não são anagramas, pois têm letras diferentes")
        i += 1

        if len(letras2) == 0:
           print(palavra1,"e",palavra2,"são anagramas!")