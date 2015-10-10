import numpy as np
import math as math

#Kevin Wang
#github:xorkevin

class Inp:
    def __init__(self):
        self._inputs = []

    def clearInputs(self):
        self._inputs = []

    def addInp(self, aInp):
        '''aInp should be a tuple (x, y, z, ...)'''
        self._inputs.append(aInp)


class State:
    def __init__(self, aState, aInp, prevInp):
        self._state = aState
        self._inp = aInp
        self._prevInp = prevInp

    def nextStates(self):
        states = []
        for inp in self._inp:
            states.append(self.nextState(inp))
        # return states

    def nextState(self, aInp):
        currentState = self._state
        # return next state

    def heuristic(self):
        score = 0
        #return score


def alphabeta(state, depth, a, b, maxTurn):
    alpha = a
    beta = b
    children = state.nextStates()

    if depth == 0 or len(children) == 0:
        # print('hello')
        # print(str(state))
        return state

    print(str(len(children)))

    futureState = None
    v = None
    if maxTurn:
        v = -math.inf
        for child in children:
            x, y = alphabeta(child, depth-1, alpha, beta, False)
            if v > y:
                v = y
                futureState = x
            alpha = max(alpha, v)
            if beta <= alpha:
                break
    else:
        v = math.inf
        for child in children:
            x, y = alphabeta(child, depth-1, alpha, beta, True)
            if v < y:
                v = y
                futureState = x
            beta = min(beta, v)
            if beta <= alpha:
                break

    return (futureState, v)
