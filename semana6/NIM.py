def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if (m > n):
        partida()

    if n % (m+1) == 0:
        print('\nVocê começa!')
        vezDe = '\nVocê'
    else:
        print('\nComputador começa!')
        vezDe = '\nO computador'

    while n > 0:
        if vezDe == '\nVocê':
            pecas = usuario_escolhe_jogada(n, m)
        else:
            pecas = computador_escolhe_jogada(n, m)

        n = n-pecas

        if pecas == 1:
            print(vezDe, 'tirou uma peça.')
        else:
            print(vezDe, 'tirou', pecas, 'peças.')

        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
            else:
                print('Agora restam', n, 'peças no tabuleiro.')

        if vezDe == '\nVocê':
            vezDe = '\nO computador'
        else:
            vezDe = '\nVocê'


def computador_escolhe_jogada(n, m):
    for i in range(1, n):
        if (n-i) % (m+1) == 0:
            return i
    if m <= n:
        return m
    else:
        return n


def usuario_escolhe_jogada(n, m):
    p = int(input('\nQuantas peças você vai tirar? '))
    if (p > m or m-p < 0 or p <= 0):
        print('\nOops! Jogada inválida! Tente de novo.')
        p = usuario_escolhe_jogada(n, m)
    return p


partida()
