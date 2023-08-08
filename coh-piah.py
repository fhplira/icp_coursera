import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
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

    assinatura_infectada = as_a
    assinatura_para_comparacao = as_b
    soma_dos_tracos = 0
    while len(as_b) > 0:
        for elemento in as_a:
            traco = elemento - as_b[0]
            soma_dos_tracos = soma_dos_tracos + abs(traco)
            del as_b[0]
    grau_de_similaridade = soma_dos_tracos / 6

    return grau_de_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass
    lista_palavras = []
    lista_palavras_formatadas = []
    lista_frases = []
    lista_frases_formatadas = []
    lista_sentencas = separa_sentencas(texto)
    lista_sentencas_formatadas = []
    for sentenca in separa_sentencas(texto):
        novas_frases = separa_frases(texto)
        for frase in novas_frases:
            novas_palavras = separa_palavras(texto)
    lista_frases.extend(novas_frases)
    lista_palavras.extend(novas_palavras)

    for sentenca in lista_sentencas:
        sentenca = sentenca.lstrip()
        lista_sentencas_formatadas.append(sentenca)

    # tamanho médio da palavra
    # média simples do número de caracteres por palavras
    soma_caracteres_palavras = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                caracteres = len(palavra)
                soma_caracteres_palavras = soma_caracteres_palavras + caracteres
    wal = soma_caracteres_palavras / len(lista_palavras)  # deu bom

    # relação type-token
    # número de palavras diferentes dividido pelo número total de palavras
    for palavras in lista_palavras:
        caracteres_especiais = '.,;":!?'
        for item in range(len(caracteres_especiais)):
            palavras = palavras.replace(caracteres_especiais[item], '')
        lista_palavras_formatadas.append(palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras_formatadas)
    ttr = palavras_diferentes / len(lista_palavras)  # deu bom

    # razão hapax legomana
    # número de palavras que aparecem uma única vez dividido pelo total de palavras
    hlr = n_palavras_unicas(lista_palavras_formatadas) / len(lista_palavras)  # deu bom

    # tamanho médio da sentença
    # média simples do número de caracteres por sentença
    soma_caracteres_sentencas = 0
    for sentenca in lista_sentencas:
        sentenca = sentenca.rstrip()
        caracteres_sentenca = len(sentenca)
        soma_caracteres_sentencas = soma_caracteres_sentencas + caracteres_sentenca
    sal = (soma_caracteres_sentencas) / len(lista_sentencas)  # deu bom

    # complexidade da sentença
    # média simples do número de frases por sentença
    total_de_frases = 0
    for sentenca in lista_sentencas:
        numero_de_frases_por_sentenca = len(separa_frases(sentenca))
        total_de_frases = total_de_frases + numero_de_frases_por_sentenca
    sac = total_de_frases / len(lista_sentencas)  # deu bom

    # tamanho médio da frase
    # média simples do número de caracteres por frase
    soma_caracteres_frases = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            caracteres_frase = len(frase)
            soma_caracteres_frases = soma_caracteres_frases + caracteres_frase
    for sentenca in lista_sentencas_formatadas:
        lista_frases_formatadas.extend(separa_frases(sentenca))
    pal = soma_caracteres_frases / len(lista_frases_formatadas)

    as_b = [wal, ttr, hlr, sal, sac, pal]

    return as_b

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_de_textos = textos
    as_b = ass_cp

    lista_dos_graus_de_similaridade_para_analise = []
    for texto in lista_de_textos:
        assinatura_do_texto = calcula_assinatura(texto)
        gs_do_texto = compara_assinatura(as_b, assinatura_do_texto)
        lista_dos_graus_de_similaridade_para_analise.append(gs_do_texto)

    indice_do_texto_infectado = lista_dos_graus_de_similaridade_para_analise.index(min(lista_dos_graus_de_similaridade_para_analise))  # esse mostra o índice
    numero_do_texto_infectado = indice_do_texto_infectado + 1

    return numero_do_texto_infectado

def main():
    '''Essa função monta* as coisas'''
    lista_de_textos = le_textos()
    as_a = le_assinatura()
    texto_infectado = avalia_textos(lista_de_textos, as_a)

    return f'O autor do texto {texto_infectado} está infectado com COH-PIAH'


