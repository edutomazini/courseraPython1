def partida():
    global n,m
    n = int(input("Quantas pecas? "))
    m = int(input("Limite de pecas por jogada? "))
    print('')

    if n%(m+1) == 0:
        mudajogador = 0
        print('Você começa!')
        print('')
        usuario_escolhe_jogada()
    else:
        mudajogador = 1
        print('Computador começa!')
        print('')
        computador_escolhe_jogada()
   
    while n > 0:
        if mudajogador == 0:
            mudajogador = 1
            computador_escolhe_jogada()
        else:
            mudajogador = 0
            usuario_escolhe_jogada()
 
def computador_escolhe_jogada():
    global n,m
    for i in range(1,n+1):
        if (n-i)%(m+1)!=0:
            p = n-i
            if p == 1:
                n = n - p
                print('O computador tirou uma peça')
                if (n == 1):
                    print('Agora resta apenas uma peça no tabuleiro.')
                    print('')
                else:
                    print('Agora restam',n,'peças no tabuleiro.')
                    print('')
                break  
            else:
                n = n - p
                print('O computador tirou', p, 'pecas')
                if (n == 1):
                    print('Agora resta apenas uma peça no tabuleiro.')
                    print('')
                else:
                    print('Agora restam',n,'peças no tabuleiro.')
                    print('')
                break
        else:
            p=1
            n = n - p
            print('O computador tirou', p, 'pecas')
            if (n == 1):
                print('Agora resta apenas uma peça no tabuleiro.')
                print('')
            else:
                print('Agora restam',n,'peças no tabuleiro.')
                print('')
            break
 
def usuario_escolhe_jogada():
    global n,m
    p = int(input('Quantas peças você vai tirar? '))

    while (p>m or m-p < 0 or p <= 0):
        print('Oops! Jogada inválida! Tente de novo.')
        p = int(input('Quantas peças você vai tirar? '))
  
    if p == 1:
        print('Voce tirou uma peça')
    else:
        print('Você tirou', p, 'pecas')
   
    n = n - p
    if (n == 1):
        print('Agora resta apenas uma peça no tabuleiro.')
        print('')
    else:
        print('Agora restam',n,'peças no tabuleiro.')
        print('')

partida()
print(n)
print(m)