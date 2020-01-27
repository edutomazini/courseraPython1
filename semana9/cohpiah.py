import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("\n\nEntre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    '''Exclui pontuacao'''
    frase = re.sub(r'[^\w\s\-]', '', frase)
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    soma = 0
    for i in range(0, 6):
        soma = soma + abs(as_a[i] - as_b[i])
    soma = soma / 6
    return soma


def calc_wal(texto):
    count = 0
    listaPalavras = separa_palavras(texto)
    for palavra in listaPalavras:
        count = count + len(palavra)
    return count / len(listaPalavras)


def calc_ttr(texto):
    listaPalavras = separa_palavras(texto)
    nPalavrasDiferentes = n_palavras_diferentes(listaPalavras)
    return nPalavrasDiferentes / len(listaPalavras)


def calc_hlt(texto):
    listaPalavras = separa_palavras(texto)
    nPalavrasUnicas = n_palavras_unicas(listaPalavras)
    return nPalavrasUnicas / len(listaPalavras)


def calc_sal(texto):
    count = 0
    listaSentencas = separa_sentencas(texto)
    for sentenca in listaSentencas:
        count = count + len(sentenca)
    return count / len(listaSentencas)


def calc_sac(texto):
    count = 0
    listaSentencas = separa_sentencas(texto)
    for sentenca in listaSentencas:
        listafrases = separa_frases(sentenca)
        count = count + len(listafrases)
    return count / len(listaSentencas)


def calc_pal(texto):
    count = 0
    listaTotalFrases = []
    listaSentencas = separa_sentencas(texto)
    for sentenca in listaSentencas:
        listafrases = separa_frases(sentenca)
        listaTotalFrases = listaTotalFrases + listafrases

    for frases in listaTotalFrases:
        count = count + len(frases)
    return (count) / len(listaTotalFrases)


def calcula_assinatura(texto):
    # wal
    count = 0
    listaPalavras = separa_palavras(texto)
    #print(listaPalavras)
    #listaPalavras = ['Navegadores', 'antigos', 'tinham', 'uma', 'frase', 'gloriosa', 'Navegar', 'é', 'preciso', 'viver', 'não', 'é', 'preciso', 'Quero', 'para', 'mim', 'o', 'espírito', 'desta', 'frase', 'transformada', 'a', 'forma', 'para', 'a', 'casar', 'como', 'eu', 'sou', 'Viver', 'não', 'é', 'necessário', 'o', 'que', 'é', 'necessário', 'é', 'criar', 'Não', 'conto', 'gozar', 'a', 'minha', 'vida', 'nem', 'em', 'gozá-la', 'penso', 'Só', 'quero', 'torná-la', 'grande', 'ainda', 'que', 'para', 'isso', 'tenha', 'de', 'ser', 'o', 'meu', 'corpo', 'e', 'a', 'minha', 'alma', 'a', 'lenha', 'desse', 'fogo', 'Só', 'quero', 'torná-la', 'de', 'toda', 'a', 'humanidadeainda', 'que', 'para', 'isso', 'tenha', 'de', 'a', 'perder', 'como', 'minha', 'Cada', 'vez', 'mais', 'assim', 'penso', 'Cada', 'vez', 'mais', 'ponho', 'da', 'essência', 'anímica', 'do', 'meu', 'sangue', 'o', 'propósito', 'impessoal', 'de', 'engrandecer', 'a', 'pátria', 'e', 'contribuir', 'para', 'a', 'evolução', 'da', 'humanidadeÉ', 'a', 'forma', 'que', 'em', 'mim', 'tomou', 'o', 'misticismo', 'da', 'nossa', 'Raça']
    for palavra in listaPalavras:
        count = count + len(palavra)
    wal = count / len(listaPalavras)

    # ttr
    nPalavrasDiferentes = n_palavras_diferentes(listaPalavras)
    ttr = nPalavrasDiferentes / len(listaPalavras)

    # hlr
    nPalavrasUnicas = n_palavras_unicas(listaPalavras)
    hlr = nPalavrasUnicas / len(listaPalavras)

    # sal e sac
    countsal = 0
    countsac = 0
    count = 0
    listaTotalFrases = []
    listaSentencas = separa_sentencas(texto)
    for sentenca in listaSentencas:
        countsal = countsal + len(sentenca)
        listafrases = separa_frases(sentenca)
        countsac = countsac + len(listafrases)
        listaTotalFrases = listaTotalFrases + listafrases
    sal = countsal / len(listaSentencas)
    sac = countsac / len(listaSentencas)

    # pal
    for frases in listaTotalFrases:
        count = count + len(frases)
    pal = (count) / len(listaTotalFrases)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_textos = []
    # ass_textos.append(ass_cp)

    for texto in textos:
        ass_textos.append(calcula_assinatura(texto))
    # print(ass_textos)

    avalia_ass = []
    for ass in ass_textos:
        avalia_ass.append(compara_assinatura(ass_cp, ass))

    pos_menor_valor = 1
    menor_valor = avalia_ass[0]

    for i in range(1, len(avalia_ass)):
        if avalia_ass[i] < menor_valor:
            pos_menor_valor = i + 1

    return pos_menor_valor

assinatura = le_assinatura()
# print(assinatura)

textos = le_textos()

pos_menor_valor = avalia_textos(textos, assinatura)

print('\nO autor do texto', pos_menor_valor, 'está infectado com COH-PIAH')


#texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."

#assinatura = calcula_assinatura(texto)
# print(assinatura)
