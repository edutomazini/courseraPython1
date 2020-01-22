numero = int(input("digite um numero: "))
Fizz = numero % 3
Buzz = numero % 5
if Fizz == 0 and Buzz == 0:
    print("FizzBuzz")
else:
    print(numero)