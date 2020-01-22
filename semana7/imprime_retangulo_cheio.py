l = int(input('digite a largura: '))
a = int(input('digite a altura: '))
y = l
while a > 0:
    while l > 0:
        print('#',end='')
        l = l - 1
    print('')
    a = a - 1
    l = y
