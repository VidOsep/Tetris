import numpy as np
import random

class Element:
    def __init__(self,x):
        element1 = [["0","1"], ["0", "1"], ["1", "1"], ["0","0"]]
        element2 = [["1","0"], ["1","0"], ["1","0"], ["1","0"]]
        element3 = [["1", "1"], ["1", "1"],["0","0"],["0","0"]]
        element4 = [["0", "1"], ["1", "1"], ["0", "1"],["0","0"]]
        self.element_arr = [element1, element2, element3, element4]
        self.element = random.choice(self.element_arr)
                
        self.x=x
        self.y=0

    def chooseRandom(self):
        self.element = random.choice(self.element_arr)
        
    def getLastRow(self):
        for i in range(4):
            if int("".join(self.element[i]),2) & 3 == 0:
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

    def drawToGrid(self,grid,topX,topY,element):
        x = element.shape[1]
        y = element.shape[0]
        grid[topY:topY+y,topX:topX+x] = element

