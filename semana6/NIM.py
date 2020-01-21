def partida():
    vezDe = ''
    pecas = 0
    n = int(input('Quantas pecas? '))
    m = int(input('Limite de pecas por jogada? '))
    print('')

    if n%(m+1) == 0:
        print('Você começa!')
        print('')
        pecas = usuario_escolhe_jogada(n,m)
        vezDe = 'O computador'

    else:
        print('Computador começa!')
        print('')
        pecas = computador_escolhe_jogada(n,m)
        vezDe = 'Voce'
    n = n-pecas

    print('n1',n)
    print('pecas1', pecas)
    print('vezDe1', vezDe)
    print('-----------------')

    while n > 0:
        if vezDe == 'Voce':
            pecas = usuario_escolhe_jogada(n,m)
            vezDe = 'O computador'
        else:
            pecas = computador_escolhe_jogada(n,m)
            vezDe = 'Voce'
        n = n-pecas
        print('n2',n)
        print('pecas2', pecas)
        print('vezDe2', vezDe)
        print('-----------------')
 
def computador_escolhe_jogada(n,m):
    for i in range(1,n):
        if (n-i)%(m+1)==0:
            return i
    return m
 
def usuario_escolhe_jogada(n,m):
    p = int(input('Quantas peças você vai tirar? '))
    if (p>m or m-p < 0 or p <= 0):
        print('Oops! Jogada inválida! Tente de novo.')
        p = usuario_escolhe_jogada(n,m)
    return p

partida()