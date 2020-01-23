lista = []
lista.append(['edu',50])
lista.append(['pietro',13])
print(lista)
print(len(lista))
print(lista[0][0])

flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1

primos = [2,3,5,7,11,13,17]
for i in primos:
    i = i**3
    print(i)
print(primos)

pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5, 10):
    print(pares[x])

def éPrimo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1

    if x % fator == 0:
        return False
    else:
        return True
    
limite = int(input('Limite máximo: '))
n = 2
while n < limite:
    if éPrimo(n):
        print(n,end=', ')
    n = n + 1