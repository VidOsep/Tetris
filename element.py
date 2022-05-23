import numpy as np
import random

class Element:
    def __init__(self,x):
        self.chooseRandom()

        self.x=x
        self.y=0

    def chooseRandom(self):
        e1 = np.array([[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]])
        e2 = np.array([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]])
        e3 = np.array([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]])
        e4 = np.array([[0,1,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]])

        element_arr = [e1, e2, e3, e4]
        self.element = random.choice(element_arr)
        
    def getLastRow(self):
        for i in range(4):
            if  == 0:
                return i
        return 3

    def isTouching(self, grid):
        try:
            ix = self.getLastRow()
            bottom = self.element[ix]
            grid_bottom = grid[self.y+ix+1][self.x:self.x+2]
            if int("".join(self.element[ix]),2) & int("".join(grid_bottom),2):
                return True
        except ValueError:
            pass
            #return True
        return False
    
    def moveDown(self):
        self.y-=1
    
    def moveRight(self):
        self.x+=1
        
    def moveLeft(self):
        self.x-=1

    def rotateRight(self):
        np.rot90(self.element)

    def draw(self, grid, topX, topY, element):

        grid[topY:topY+y,topX:topX+x] = element

