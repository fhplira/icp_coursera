#palavra = 'sdskjdkm,?!kj.,;'
#caracteres_especiais = ",.;!;?"
#for x in range (len(caracteres_especiais)):
#    palavra = palavra.replace(caracteres_especiais[x], '')
#print(palavra)


#lista_de_frases = ['Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei', ' Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes', ' Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge', ' No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade']
#lista_de_frases_sem_espacos = []
#for frase in lista_de_frases:
    #frase = frase.strip()
    #lista_de_frases_sem_espacos.append(frase)
#print(lista_de_frases_sem_espacos)
    #lista_de_frases_com_espaço.append(frase)
    #frase.rstrip()
    #lista_de_frases_sem_espaço.append(frase)
#print(lista_de_frases_com_espaço)
#print(lista_de_frases_sem_espaço)
import re

#lista_de_sentencas = ['Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei', ' Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes', ' Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge', ' No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade']
#sentencas_sem_espacos_finais = []
#lista_frases = []
#caracteres_totais_frases = 0
##for sentenca in lista_de_sentencas:
 #   sentenca = sentenca.strip()
 #   sentencas_sem_espacos_finais.append(sentenca)

#for elemento in sentencas_sem_espacos_finais:
 #   frases = re.split(r'[.,:;]+', elemento)
 #   for frase in frases:
 #       frase = frase.strip()
  #      lista_frases.append(frase)
 #       caracteres_frase = len(frase) + 1
 #   caracteres_totais_frases = caracteres_totais_frases + caracteres_frase

#print(sentencas_sem_espacos_finais)
#print(lista_frases)
#print(caracteres_totais_frases)

#lista_frases = [' hoje quero comer bolo', ' amanhã talvez não']
#soma_caracteres_frases = 0
#for frase in lista_frases:
 #   frase = frase.lstrip()
 #   caracteres_frase = len(frase)
 #   soma_caracteres_frases = soma_caracteres_frases + caracteres_frase
#pal = soma_caracteres_frases / len(lista_frases)
#print(pal)

#lista = [1,2,3,4]
#lista_2 = lista[:]
#print(lista_2)

#print(main())

#print(compara_assinatura([4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5], [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]))
#Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.
#Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.

#[4.51, 0.693, 0.55, 70.82, 1.82, 38.5]

frase = ' o rato roeu a roupa do rei de roma'
frase = frase.strip()
comprimento_frase = len(frase)
print(frase)
print(comprimento_frase)