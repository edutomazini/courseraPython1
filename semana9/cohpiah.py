import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

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
    frase = re.sub(r'[^\w\s\-]', '',frase)
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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

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
        for frases in listafrases:
            count = count + 1
    return count / len(listaSentencas)

def calc_pal(texto):
    count = 0
    listafrases = separa_frases(texto)
    for frases in listafrases:
            count = count + len(frases)
    return count / len(listafrases)

def calcula_assinatura(texto):
    #wal = float(input("Entre o tamanho medio de palavra:"))
    #ttr = float(input("Entre a relação Type-Token:"))
    #hlr = float(input("Entre a Razão Hapax Legomana:"))
    #sal = float(input("Entre o tamanho médio de sentença:"))
    #sac = float(input("Entre a complexidade média da sentença:"))
    #pal = float(input("Entre o tamanho medio de frase:"))
    
    wal = calc_wal(texto)
    ttr = calc_ttr(texto)
    hlr = calc_hlt(texto)
    sal = calc_sal(texto)
    sac = calc_sac(texto)
    pal = calc_pal(texto)
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

#assinatura = le_assinatura()
#print(assinatura)

#le_textos()

texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
assinatura = calcula_assinatura(texto)
print(assinatura)