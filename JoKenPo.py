import time
import random
from random import randint

ppt = ('Pedra', 'Papel', 'Tesoura')


while True:
    aleatorio = random.randint(0, 2)
    print("""Suas opções:
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    [4] - Sair
    """)
    jogada = int(input(
        'JoKenPo, faça sua jogada:')
        )
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    if jogada == 4:
        break

    print(f'Você escolheu {ppt[jogada-1]}')
    print(f'Computador escolheu {ppt[aleatorio]}')

    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    if jogada == 1:
        if aleatorio == 0:
            print('Empate, computador tirou Pedra')
            time.sleep(3)
        
        elif aleatorio == 1:
            print('Você perdeu, computador tirou Papel')
            time.sleep(3)

        else:
            print('Você ganhou!, computador tirou Tesoura')
            time.sleep(3)

    elif jogada == 2:
        if aleatorio == 0:
            print('Você ganhou, computador tirou Pedra')
            time.sleep(3)

        elif aleatorio == 1:
            print('Empate, computador tirou Papel')
            time.sleep(3)

        else:
            print('Você perdeu, computador tirou Tesoura')
            time.sleep(3)

    elif jogada == 3:
        if aleatorio == 0:
            print('Você perdeu, computador tirou Pedra')
            time.sleep(3)

        elif aleatorio == 1:
            print('Você ganhou, computador tirou Papel')
            time.sleep(3)

        else:
            print('Empate, computador tirou Tesoura')
            time.sleep(3)
        
    else:
        print('Jogada inválida')