

def maior_primo(n):
    n = int(n)
    if éPrimo(n):
        return n
    
    while n >= 2:
        if éPrimo(n):
            return n
        n = n - 1

    return n

def éPrimo(k):
    k = int(k)
    count = 2
    primo = True

    while count < k:
        if k % count == 0:
            primo = False
            break
        count = count + 1

    return primo

x = input('x')
print(maior_primo(x))