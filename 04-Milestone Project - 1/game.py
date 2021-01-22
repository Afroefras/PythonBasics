import time
import numpy as np
import pandas as pd
from IPython.display import clear_output

def tic_tac():
    tablero = pd.DataFrame(np.zeros((3,3)))
    dic_tic = {0:'-', 1:'X',10:'O'}
    player1 = str(input('Quién es el 1er jugador/a: '))
    player2 = str(input('Quién es el 2o jugador/a: '))
    clear_output()
    print(f'{player1} ...VS... {player2}\n...\n...\nFIGHT!')
    uno = time.time()
    while time.time() - uno < 2:
        pass
    else:
        clear_output()
        
    '''Comienza el juego!!!'''
    win = 0
    winner = 'Nadie'
    print('Este es el tablero, cada celda representa un número del 1-9')
    print(tablero.replace(dic_tic))
    while win == 0:
        for player in [player1,player2]:
            turno = 'X' if player == player1 else 'O'
            valor = 1 if turno == 'X' else 10
            play = int(input(f'Turno de {player}, juega {turno} en qué posición? (1-9): '))
            x = (play-1)//3
            y = 2 if play%3 == 0 else play%3-1
            while tablero.iloc[x,y] != 0 or play not in range(1,10):
                print(f'\nPosición ocupada o fuera de rango, {player}! Elige otra opción!')
                play = int(input(f'\nJuega {turno} en qué posición? (1-9): '))
                x = (play-1)//3
                y = 2 if play%3 == 0 else play%3-1
            else:
                tablero.iloc[x,y] = valor
                clear_output()
            print(tablero.replace(dic_tic))
            win = 1 if 3*valor in ([tablero[x].sum() for x in tablero.columns] + 
                                   [sum(tablero.iloc[x,:]) for x in tablero.columns] + 
                                   [np.trace(tablero), np.trace(np.fliplr(tablero))]
                                  ) else win
            winner = player if win == 1 else winner
            win = 1 if tablero.min().min() > 0 else win
            if win == 1:
                break
    else:
        print(f'{winner} gana!')