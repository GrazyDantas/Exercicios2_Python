#implemente um conversor de bases numéricas (decimal, binário, octal, hexadecimal) com validação.

num = input("Digite o número a ser convertido: ")
base = input("Digite a base(decimal, binario, octal e hexadecimal): ").lower()
if base == "decimal":
    base = 10
elif base == "binario":
    base = 2
elif base == "octal":
    base = 8
elif base == "hexadecimal":                               
    base = 16                                  
else:
    print("Base inválida")

try:
    decimal = int(num, base)
except:
    print("Digite apenas números")                                                                                     
         
                                                                                                        
binario = bin(decimal)[2:]
octal = oct(decimal)[2:]
hexadecimal = hex(decimal)[2:].upper()
decimal = str(decimal)
print("Binário:",binario)
print("Octal:",octal)
print("Hexadecimal:",hexadecimal)
                        