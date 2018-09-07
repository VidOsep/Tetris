import numpy as np
import random

class Element:
    def __init__(self):
        element1 = np.matrix([[0, 1], [0, 1], [1, 1]])
        element2 = np.matrix([[1], [1], [1], [1]])
        element3 = np.matrix([[1, 1], [1, 1]])
        element4 = np.matrix([[0, 1], [1, 1], [0, 1]])
        self.element_arr = [element1, element2, element3, element4]

    def chooseRandom(self):
        self.element = random.choice(self.element_arr)

    def isTouching(self,last_zero, bottom):
        try:
            if bottom == [1, 1]:
                if last_zero.any():
                    return True
            else:
                if bottom[0] == 1 and last_zero[0] == 1:
                    return True
                elif bottom[1] == 1 and last_zero[1] == 1:
                    return True
        except ValueError:
            if last_zero.any():
                return True

    def drawToGrid(self,grid,topX,topY,element):
        x = element.shape[1]
        y = element.shape[0]
        grid[topY:topY+y,topX:topX+x] = element

