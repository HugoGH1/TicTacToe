from random import randrange
import random
import os, sys

board=["-", "-", "-", 
        "-", "X", "-", 
        "-", "-", "-"]
player = "O"
game = True
winner = None


#TABLERO
def displayBoard(board):
    os.system("clear")
    print(board[0]," | ",board[1]," | ",board[2]," | ")
    print("- -+- - -+- - -+")
    print(board[3]," | ",board[4]," | ",board[5]," | ")
    print("- -+- - -+- - -+")
    print(board[6]," | ",board[7]," | ",board[8]," | ")
    print("- -+- - -+- - -+")


'''def EnterMove(board):
    global winner, maq
    displayBoard(board)
    TurnoPla(board)
    TurnoMaq(board)'''

#GANADOR POR LINEA 
def HorizontalWin(board):
    global winner
    if (board[0] == board[1] == board[2]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[3] == board[4] == board[5]) and board[3]!= "-":
        winner = board[3]
        return True
    elif (board[6] == board[7] == board[8]) and board[6]!= "-":
        winner = board[6]
        return True
    return False

def VerticalWin(board):
    global winner
    if (board[0] == board[3] == board[6]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[1] == board[4] == board[7]) and board[1]!= "-":
        winner = board[1]
        return True
    elif (board[2] == board[5] == board[8]) and board[2]!= "-":
        winner = board[2]
        return True
    return False

def DiagonalWin(board):
    global winner
    if (board[0] == board[4] == board[8]) and board[0]!= "-":
        winner = board[0]
        return True
    elif (board[2] == board[4] == board[6]) and board[2]!= "-":
        winner = board[2]
        return True
    return False
    
#EMPATE
def Empate(board):
    global game
    if "-" not in board:
        print("WOW!, EMPATE!!")
        game = False

#REVISAR SI ALGUIEN HA GANADO
def Win(board):
    global winner
    if HorizontalWin(board) or VerticalWin(board) or DiagonalWin(board):
        print(f"El ganador es:", winner)
        quit()
        
def TurnoPla(board):
    Valido = False
    while Valido != True:
        entrada = int(input("Elige un numero del 1-9: "))
        if entrada >= 1 and entrada <= 9 and entrada != 5 and board[entrada-1] == "-":
            board[entrada-1] = "O"
            Valido = True
        else:
            print("Movimiento invalido, intenta de nuevo")

def TurnoMaq(board):
    Valido = False
    while Valido != True:
        maq = int(randrange(1,10))
        if board[maq-1] == "-":
            board[maq-1] = "X"
            Valido = True

while game != False:
    displayBoard(board)
    TurnoPla(board)
    displayBoard(board)
    Win(board)
    TurnoMaq(board)
    displayBoard(board)
    Win(board)
    Empate(board)

    