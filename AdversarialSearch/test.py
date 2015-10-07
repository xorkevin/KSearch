import numpy as np
import connect4 as c4
#Kevin Wang
#github:xorkevin

# x = np.matrix([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
#     ])
#
# y = np.matrix([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
#     ])
#
# print(str(x == y))
#
# print(str(x[1, 1]))
#
# row = np.matrix([5, 6, 7, 8])
#
# print(str(row))
#
# for i in range(0, len(x)):
#     print(str(len(x[i])))
#
# print('range')
#
# y = range(4, 0, -1)
# for i in y:
#     print(str(i))


game = c4.Connect4Game(c4.HumanPlayer(), c4.HumanPlayer())

game.game()
