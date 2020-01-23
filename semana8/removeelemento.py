def remove_repetidos(lista):
  listaret = []
  for elemento in lista:
    if elementoinlista(elemento, listaret) == False:
      listaret.append(elemento)
  listaret.sort()
  return listaret

def elementoinlista(item, lista):
  for elemento in lista:
    if elemento == item:
      return True
  return False

lista = [2, 4, 2, 2, 3, 3, 1]
#lista = input('lista: ')
#lista = [1,5,6,8,45,1,25,4,1,4,5,2,1,4,5,2,1,1]
lista = remove_repetidos(lista)
print(lista)
