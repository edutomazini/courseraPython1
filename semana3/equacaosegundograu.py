import math
print("entre com os valores de a, b e c da equacao ax2 + bx +c")
a = float(input("digite a: "))
b = float(input("digite b: "))
c = float(input("digite c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("solucoes x1 e x2")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x1 = -b / (2*a)
    x2 = x1
    print("solucoa unica x1 = x2")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("a equacao nao tem solucoes reais")
