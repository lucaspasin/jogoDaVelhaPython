def checkVictory(lista):
    if (lista[0] == lista[1] == lista[2]) or (lista[3] == lista[4] == lista[5]) or (lista[6] == lista[7] == lista[8]) or (lista[0] == lista[3] == lista[6]) or (lista[1] == lista[4] == lista[7]) or (lista[2] == lista[5] == lista[8]) or (lista[0] == lista[4] == lista[8]) or (lista[2] == lista[4] == lista[6]):
        print('\n\nVITÓRIA\n\n')
        return True
    else:
        return False

def board(lista):
    
    print( '  ', lista[0],' | ', lista[1], ' | ' ,lista[2], '\n',
            '-----|-----|-----\n',
            ' ', lista[3], ' | ', lista[4], ' | ' ,lista[5], '\n',
            '-----|-----|-----\n',
            ' ', lista[6], ' | ', lista[7], ' | ' ,lista[8], '\n')

global lista

lista = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
vitoria = False
mark = 'X'

print('\nBem vindos seus cotoco\n')
board(lista)

while vitoria == False:
    print('\nQual sua jogada meu jovem?')
    jogada = input()
    if lista[int(jogada) - 1] == 'X' or lista[int(jogada) - 1] == 'O':       
        print("\nJoga em um vazio panaca")
    else:
        lista[int(jogada) - 1] = mark
        board(lista)
        vitoria = checkVictory(lista)
        if mark == 'X':
            mark = 'O'
        elif mark == 'O':
            mark = 'X'
    

