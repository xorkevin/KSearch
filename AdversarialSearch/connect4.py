import numpy as np
import alphabeta as AB
import math as math

#Kevin Wang
#github:xorkevin

class Connect4State(AB.State):
    def __init__(self, aState, aInp, prevInp):
        '''aState should be a 6*7 matrix (row major)'''
        if aState is None:
            self._state = np.matrix(np.zeros((6, 7)))
        else:
            self._state = aState
        self._inp = aInp
        self._prevInp = prevInp

    def nextStates(self):
        states = []
        for inp in self._inp:
            states.append(self.nextState(inp))
        # return states

    def nextState(self, aInp):
        id, nextId, col = aInp
        currentState = self._state
        r, c = currentState.shape
        for i in range(0, r+1):
            if i == r:
                currentState[i-1, col] = id
                break
            elif currentState[i, col] != 0:
                currentState[i-1, col] = id
                break
        inp = AB.Inp()
        for i in range(0, c):
            if currentState[0, i] == 0:
                inp.addInp((nextId, id, i))
        return Connect4State(currentState, inp, aInp)

    def heuristic(self):
        score = 0
        #return score

    def __str__(self):
        x = ''
        r,c = self._state.shape
        for i in range(0, r):
            for j in range(0, c):
                x += str(int(self._state[i, j])) + ' '
            x += '\n'
        return x


class Connect4Game:
    def __init__(self, a, b):
        self._player1 = a
        self._player2 = b

        self._idp1 = 1
        self._idp2 = 2
        self._idnought = 0

        inp = AB.Inp()
        for i in range(0, 7):
            inp.addInp((self._idp1, self._idp2, i))

        self._state = Connect4State(None, inp, None)

    def game(self):
        winner = self.win(self._state)
        turnA = True
        while winner == self._idnought:
            player = None
            id = None
            nextId = None
            if turnA:
                turnA = False
                player = self._player1
                id = self._idp1
                nextId = self._idp2
                print('player 1: \n')
            else:
                turnA = True
                player = self._player2
                id = self._idp2
                nextId = self._idp1
                print('player 2: \n')

            print(str(self._state))
            print('0 1 2 3 4 5 6 \n')

            move = player.move(self._state, id, nextId)
            while move not in self._state._inp._inputs:
                move = player.move(self._state, id, nextId)
            self._state = self._state.nextState(move)
            winner = self.win(self._state)
        print('finish')
        print(str(self._state))

    def win(self, state):
        nought = self._idnought
        p1 = self._idp1
        p2 = self._idp2

        row = np.matrix([True, True, True, True])
        diagonal1 = np.matrix([
            [True, False, False, False],
            [False, True, False, False],
            [False, False, True, False],
            [False, False, False, True]
            ])

        r, c = state._state.shape

        sieveP1 = np.matrix(state._state == p1)
        for i in range(0, r):
            for j in range(0, c - row.shape[1]+1):
                if (sieveP1[i, j:j+row.shape[1]] == row).all():
                    return p1
        sieveP1T = sieveP1.T
        for i in range(0, c):
            for j in range(0, r - row.shape[1]+1):
                if (sieveP1T[i, j:j+row.shape[1]] == row).all():
                    return p1
        for i in range(0, r - diagonal1.shape[0]+1):
            for j in range(0, c - diagonal1.shape[1]+1):
                if np.diagonal(sieveP1[i:i+diagonal1.shape[0], j:j+diagonal1.shape[1]] == diagonal1).all():
                    return p1
        sieveRotP1 = np.rot90(sieveP1)
        for i in range(0, c - diagonal1.shape[0]+1):
            for j in range(0, r - diagonal1.shape[1]+1):
                if np.diagonal(sieveRotP1[i:i+diagonal1.shape[0], j:j+diagonal1.shape[1]] == diagonal1).all():
                    return p1

        sieveP2 = np.matrix(state._state == p2)
        for i in range(0, r):
            for j in range(0, c - row.shape[1]+1):
                if (sieveP2[i, j:j+row.shape[1]] == row).all():
                    return p2
        sieveP2T = sieveP2.T
        for i in range(0, c):
            for j in range(0, r - row.shape[1]+1):
                if (sieveP2T[i, j:j+row.shape[1]] == row).all():
                    return p2
        for i in range(0, r - diagonal1.shape[0]+1):
            for j in range(0, c - diagonal1.shape[1]+1):
                if np.diagonal(sieveP2[i:i+diagonal1.shape[0], j:j+diagonal1.shape[1]] == diagonal1).all():
                    return p2
        sieveRotP2 = np.rot90(sieveP2)
        for i in range(0, c - diagonal1.shape[0]+1):
            for j in range(0, r - diagonal1.shape[1]+1):
                if np.diagonal(sieveRotP2[i:i+diagonal1.shape[0], j:j+diagonal1.shape[1]] == diagonal1).all():
                    return p2

        return nought


class Player:
    def __init__(self):
        pass

    def move(self, state):
        x = 0
        return x


class HumanPlayer(Player):
    def move(self, state, id, nextId):
        return (id, nextId, int(input('Enter column from 0-6: ')))


class AIPlayer(Player):
    def move(self, state, id, nextId):
        return AB.alphabeta(state, -1, -math.inf, math.inf, True)

'''
Todo:
- implement calculating next states
'''
