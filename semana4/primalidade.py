n = int(input("Digite um número inteiro: "))
count = 2
primo = "primo"

while count < n:
    if n%count == 0:
        primo = "não primo"
        break
    count = count + 1

print(primo)