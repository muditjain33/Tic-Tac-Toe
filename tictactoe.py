"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    # Returns starting state of the board.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xcount=0
    ycount=0
    e=0
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==X):
                xcount=xcount+1
            elif(board[i][j]==O):
                ycount=ycount+1
            else:
                e=e+1
    if(xcount>ycount):
        return O
    elif(ycount>=xcount):
        return X
    
    # Returns player who has the next turn on a board.

def actions(board):
    a=set()
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==EMPTY):
                a.add((i,j))
    return a    
    # Returns set of all possible actions (i, j) available on the board.



def result(board, action):
    if(board[action[0]][action[1]]==EMPTY):
        board2=copy.deepcopy(board)
        board2[action[0]][action[1]]=player(board)
        return board2
    else:
        raise Exception("Invalid Choice")
    # Returns the board that results from making move (i, j) on the board.


def winner(board):
    # checking horizontally
    for i in range(0,3):
        if(board[i][0]!=EMPTY):
            pre=board[i][0]
        else:
            continue
        switch=0
        for j in range(1,3):
            if(board[i][j]==EMPTY):
                switch=1
                break
            elif(board[i][j]!=pre):
                switch=1
                break
        if(switch==0):
            return pre

    # checking vertically  
    for i in range(0,3):
        if(board[0][i]!=EMPTY):
            pre=board[0][i]
        else:
            continue
        switch=0
        for j in range(1,3):
            if(board[j][i]==EMPTY):
                switch=1
                break
            elif(board[j][i]!=pre):
                switch=1
                break
        if(switch==0):
            return pre

    # checking diagonally
    if(board[1][1]==X):
        if(board[0][0]==X and board[2][2]==X):
            return X
        if(board[0][2]==X and board[2][0]==X):
            return X
    elif(board[1][1]==O):
        if(board[0][0]==O and board[2][2]==O):
            return O
        if(board[0][2]==O and board[2][0]==O):
            return O
    return None        
    # Returns the  winner of the game, if there is one.


def terminal(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==EMPTY):
                if(winner(board)!=None):
                    return True
                else:
                    return False
    return True
    # Returns True if game is over, False otherwise.

def utility(board):
    if(winner(board)==X):
        return 1
    elif(winner(board)==O):
        return -1
    else:
        return 0
    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

def min_value(state):
    if(terminal(state)):
        return utility(state)
    v=float('inf')
    for action in actions(state):
        v=min(v,max_value(result(state,action)))
    return v

def max_value(state):
    if(terminal(state)):
        return utility(state)
    v=float('-inf')
    for action in actions(state):
        v=max(v,min_value(result(state,action)))
    return v

def empty_board(board):
    for i in board:
        for j in i:
            if(j!=EMPTY):
                return False
    return True

def minimax(board):
    if(terminal(board)):
        return None
    if(player(board)==X):
        if(empty_board(board)==True):
            return (0,1)
        v=float('-inf')
        n=float('-inf')
        for action in actions(board):
            v=max(v,min_value(result(board,action)))
            if(v>n):
                n=v
                s=action
    else:
        v=float('inf')
        n=float('inf')
        for action in actions(board):
            v=min(v,max_value(result(board,action)))
            if(v<n):
                n=v
                s=action
    return s
    # Returns the optimal action for the current player on the board.