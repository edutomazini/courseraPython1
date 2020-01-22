n = input("Digite um número inteiro: ")
tamanho = len(n)
verifica = "nao"

while tamanho > 1:
    if (n[tamanho-1] == n[tamanho-2]):
        verifica = "sim" 
        break
    tamanho = tamanho - 1

print(verifica)