def main():
    escolha = int(input('Bem-vindo ao jogo do NIM! Escolha:\n'
                        '1 - para jogar uma partida isolada\n'
                        '2 - para jogar um campeonato\n '))
    if escolha == 1:
        return 'Voce escolheu uma partida isolada!', partida()

    if escolha == 2:
        return 'Voce escolheu um campeonato!', campeonato()


def computador_escolhe_jogada(n, m):
    pecas_retiradas = n - ((n // (m + 1)) * (m + 1))
    if pecas_retiradas == 0:
        return m
    m = pecas_retiradas
    while m > n:
        m = m - 1
        pecas_retiradas = m
    if n < m:
        m = n
    if n % m == 0:
        m = m - 1
    if pecas_retiradas == n or m == 0:
        m = pecas_retiradas
    pecas_restantes = n - m
    n = pecas_restantes
    if m == 1:
        print('o computador removeu uma peça \n')
    else:
        print(f'o computador removeu {m} peças \n')
    if pecas_restantes != 0:
        print(f'Agora restam apenas {pecas_restantes} peças \n')
    else:
        print("Fim do jogo! O computador ganhou \n")
    return pecas_retiradas


def usuario_escolhe_jogada(n, m):
    pecas_retiradas = int(input('Quantas peças você vai tirar? \n'))
    #pecas_restantes = n - pecas_retiradas
    #if pecas_retiradas > m or pecas_retiradas > n or pecas_retiradas <= 0:
        #print('Oops! Jogada inválida! Tente de novo \n')
    while pecas_retiradas > m or pecas_retiradas > n or pecas_retiradas <= 0:
        # o valor de pecas_retiradas não tá atualizando
        print('Oops! Jogada inválida! Tente de novo \n')
        pecas_retiradas = int(input('Quantas peças você vai tirar? \n'))
    #if pecas_retiradas <= m:
    if pecas_retiradas == 1:
        print(f'voce removeu uma peça \n')
    if pecas_retiradas == n:
        print(f'Você removeu {pecas_retiradas} peças \n'
              f'Fim de jogo! Você ganhou.')
    else:
        print(f'voce removeu {pecas_retiradas} peças \n')

    pecas_restantes = n - pecas_retiradas
    if pecas_restantes == 1:
        print(f'Resta {pecas_restantes} peça \n')
    else:
        print(f'Restam {pecas_restantes} peças \n')
    return pecas_retiradas
    #else:
        #if pecas_retiradas == n:
            #print(f'Você removeu {pecas_retiradas} peças \n'
                  #f'Fim de jogo! Você ganhou.')
            #return pecas_retiradas


def partida():
    n = int(input('Quantas peças? \n'))
    m = int(input('Limite de peças por jogada? \n'))
    pecas_retiradas = 0
    while n < m:
        n = int(input('Quantas peças? \n'))
        m = int(input('Limite de peças por jogada? \n'))

    if n % (m + 1) == 0:
        print('Você começa! \n')

    else:
        print('Computador começa! \n')

    while n > 0:
        if n % (m + 1) == 0:
            pecas_retiradas = usuario_escolhe_jogada(n, m)
        else:
            pecas_retiradas = computador_escolhe_jogada(n, m)
        n = n - pecas_retiradas


def campeonato():
    jogo = 0
    while jogo < 3:
        print("**** Rodada", (jogo + 1), "! **** \n")
        partida()
        jogo = jogo + 1
    print("**** Final do Campeonato! **** \n"
          "Placar: Você 0 x 3 computador \n")


main()
