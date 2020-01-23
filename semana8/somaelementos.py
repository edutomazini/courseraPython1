def soma_elementos(lista):
  soma = 0
  for elemento in lista:
    soma = soma + elemento
  return soma

lista = [2, 4, 2, 2, 3, 3, 1]
#lista = input('lista: ')
#lista = [1,5,6,8,45,1,25,4,1,4,5,2,1,4,5,2,1,1]
print(soma_elementos(lista))
