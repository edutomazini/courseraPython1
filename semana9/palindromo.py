# Nomes que ajudam a entender intuitivamente o problema
def eh_palindromo(palavra):
    letra = 0
    while letra < len(palavra):
        if palavra[letra] != palavra[len(palavra) - letra - 1]:
            return False
    return True