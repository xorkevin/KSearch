import numpy as np

#Kevin Wang
#github:xorkevin

class Connect4State:
    def __init__(self, grid = None):
        '''grid should be a 6*7 matrix (row major)'''
        if grid is None:
            self._state = np.zeros((6, 7))
        else:
            self._state = grid

    def nextState(self, input):
        '''input should be a column 0-6'''
        currentState = self._state
        # should return next state

class Connect4Game:
    def __init__(self):
