import numpy as np
import random


class Element:
    def __init__(self, x):
        self.chooseRandom()

        self.x = x
        self.y = 0

    def chooseRandom(self):
        e1 = np.array([[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]], dtype=int)
        e2 = np.array([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], dtype=int)
        e3 = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=int)
        e4 = np.array([[0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]], dtype=int)

        element_arr = [e1, e2, e3, e4]
        self.element = random.choice(element_arr)

    def getLastRow(self):
        a,b=0,0
        for i in range(4):
            if np.sum(self.element[i]) != 0:
                if a==0:
                    b=i
                a+=1
        return a+b

    def getLastCol(self):
        a,b=0,0
        for i in range(4):
            if np.sum(self.element[:,i]) != 0:
                if a==0:
                    b=i
                a+=1
        return a+b

    def isColliding(self,x,y,grid):
        new = np.zeros((20,10),dtype=int)
        ix = self.getLastRow()
        iy = self.getLastCol()
        new[x:y+iy,x:x+ix] = self.element[0:iy,0:ix]

        overlap = np.bitwise_and(new,grid)
        if np.sum(overlap) > 0:
            return True

    def isTouching(self, grid):
        try:
            ix = self.getLastRow()
            bottom = self.element[ix]
            grid_bottom = grid[self.y + ix + 1][self.x:self.x + 2]
            if int("".join(self.element[ix]), 2) & int("".join(grid_bottom), 2):
                return True
        except ValueError:
            pass
            # return True
        return False

    def moveDown(self):
        self.y += 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def rotateRight(self):
        # rotacija za 90 stopinj
        self.element = np.rot90(self.element)

    def draw(self, grid):
        new = np.zeros((20,10),dtype=int)
        iy = self.getLastRow()
        ix = self.getLastCol()
        new[self.y:self.y+iy,self.x:self.x+ix] = self.element[0:iy,0:ix]

        return np.bitwise_or(new,grid)
