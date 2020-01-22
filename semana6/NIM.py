def campeonato():
    print('\nBem-vindo ao jogo do NIM! Escolha:')
    print('\n1 - para jogar uma partida isolada')
    j = int(input('2 - para jogar um campeonato '))

    if j == 1:
        print('\nVoce escolheu uma partida!')
        partida()
    else:
        print('\nVoce escolheu um campeonato!')
        for i in range(1, 4):
            print('\n**** Rodada', i, '****')
            partida()
        print('\n**** Final do campeonato! ****')
        print('\nPlacar: Você 0 X 3 Computador')

def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if (m > n):
        print('Valores inválidos! Digite novamente')
        partida()

    if n % (m+1) == 0:
        print('\nVoce começa!')
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
    p = int(input('\nQuantas peças Você vai tirar? '))
    if (p > m or p <= 0):
        print('\nOops! Jogada inválida! Tente de novo.')
        p = usuario_escolhe_jogada(n, m)
    return p

campeonato()
