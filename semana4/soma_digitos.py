n = input("Digite um número inteiro: ")
tamanho = len(n)
soma = 0


while tamanho > 0:
    soma = soma + int(n[tamanho-1])
    tamanho = tamanho - 1

print(soma)