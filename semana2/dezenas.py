numero = input("Digite um número inteiro: ")
if len(numero) < 2:
    print("O dígito das dezenas é 0")
else:
    print("O dígito das dezenas é",numero[len(numero)-2])
