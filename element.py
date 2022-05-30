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
        e5 = np.array([[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,0]], dtype=int)
        e6 = np.array([[0,1,0,0], [0,1,0,0], [1,1,1,0], [0,1,0,0]], dtype=int)
        e7 = np.array([[1,1,1,0,1], [0,0,1,0,1], [1,1,1,1,1], [1,0,1,0,0],[1,0,1,1,1]], dtype=int)


        colors = ["LIGHT_GREEN","LIGHT_BLUE","LIGHT_RED","YELLOW","PURPLE"]
        element_arr = [e1,e2,e3,e4,e5,e6,e7]
        self.element = random.choice(element_arr)
        self.color = random.choice(colors)

    def getLastRow(self):
        a,b=0,0
        for i in range(len(self.element[0])):
            if np.sum(self.element[i]) != 0:
                if a==0:
                    b=i
                a+=1
        return a+b

    def getLastCol(self):
        a,b=0,0
        for i in range(len(self.element)):
            if np.sum(self.element[:,i]) != 0:
                if a==0:
                    b=i
                a+=1
        return a+b

    def isColliding(self,x,y,grid):
        # preveri ce se tetronim na poziciji prekriva z igralno povrsino
        new = np.zeros((20,10),dtype=int)
        iy = self.getLastRow()
        ix = self.getLastCol()
        try:
            new[y:y+iy,x:x+ix] = self.element[0:iy,0:ix]
        except:
            return True
        overlap = np.bitwise_and(new,grid)
        if np.sum(overlap) > 0:
            return True
        return False

    def shiftElArrayLeft(self):
        # zamakne obliko tetronima v levo
        self.element = self.element[:,1:]
        new_column = np.zeros((len(self.element),1))
        self.element = np.append(self.element, new_column, axis=1)

    def moveToLeftUp(self):
        # prestavi tetronim v zgornji levi kot matrike
        while np.sum(self.element[:,0]) == 0:
            self.shiftElArrayLeft()

    def moveDown(self,grid):
        # premakne tetronimo navzdol
        if self.y+self.getLastRow()>19 or self.isColliding(self.x,self.y+1,grid):
            return False
        else:
            self.y += 1
            return True

    def moveRight(self,grid):
        # premakne tetronimo v desno
        if self.x+self.getLastCol()>=18 or self.isColliding(self.x+1,self.y,grid):
            return False
        else:
            self.x += 1
            return True

    def moveLeft(self,grid):
        # premakne tetronimo v levo
        if self.x<1 or self.isColliding(self.x-1,self.y,grid):
            return False
        else:
            self.x -= 1
            return True

    def rotateRight(self,grid):
        # rotacija za 90 stopinj
        old = self.element
        self.element = np.rot90(self.element)
        self.moveToLeftUp()
        try:
            if not self.isColliding(self.x,self.y,grid):
                return True
            else:
                self.element = old
                return False
        except:
            return False
    def drawColors(self,new,colors):
        for i in range(len(new)):
            for j in range(len(new[0])):
                if new[i][j]:
                    colors[i][j] = self.color
        return colors

    def draw(self, grid, colors):
        new = np.zeros((20,10),dtype=int)
        iy = self.getLastRow()
        ix = self.getLastCol()
        new[self.y:self.y+iy,self.x:self.x+ix] = self.element[0:iy,0:ix]

        colors = self.drawColors(new,colors)

        return np.bitwise_or(new,grid),colors
