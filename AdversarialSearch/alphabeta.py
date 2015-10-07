import numpy as np
import math as math

#Kevin Wang
#github:xorkevin

class Inp:
    def __init__(self):
        self._inputs = []

    def clearInputs(self):
        self._inputs = []

    def addInp(self, aInput):
        '''aInput should be a tuple (x, y, z, ...)'''
        self._inputs.append(aInput)


class State:
    def __init__(self, aState, aInput, prevInput):
        self._state = aState
        self._inp = aInput
        self._prevInput = prevInput

    def nextStates(self):
        states = []
        for inp in self._input:
            states.append(self.nextState(inp))
        # return states

    def nextState(self, aInput):
        currentState = self._state
        # return next state

    def heuristic(self):
        score = 0
        #return score


def alphabeta(self, state, depth, a, b, maxTurn):
    alpha = a
    beta = b
    children = state.nextStates()

    if depth == 0 or len(children) == 0:
        return state

    futureState = None
    v = None
    if maxTurn:
        v = -math.inf
        for child in children:
            x = alphabeta(child, depth-1, alpha, beta, False)
            if v > x.heuristic():
                v = x.heuristic()
                futureState = x
            alpha = max(alpha, v)
            if beta <= alpha:
                break
    else:
        v = math.inf
        for child in children:
            x = alphabeta(child, depth-1, alpha, beta, True)
            v = min(v, x.heuristic())
            if v < x.heuristic():
                v = x.heuristic()
                futureState = x
            beta = min(beta, v)
            if beta <= alpha:
                break

    return futureState
