def fizzbuzz(numero):
    numero = int(numero)
    Fizz = numero % 3
    Buzz = numero % 5
    if Fizz == 0 and Buzz == 0:
        return "FizzBuzz"
    elif Fizz == 0:
        return "Fizz"
    elif Buzz == 0:
        return "Buzz"
    else:
        return numero