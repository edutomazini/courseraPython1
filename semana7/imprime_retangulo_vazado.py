l = int(input('digite a largura: '))
a = int(input('digite a altura: '))
y = l
x = a

while a > 0:
    while l > 0:
        if l == y or l == 1 or a == x or a == 1:
            caracter = '#'
        else:
            caracter = ' '
        print(caracter, end='')
        l = l - 1
    print('')
    a = a - 1
    l = y
