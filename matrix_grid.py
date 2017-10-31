import time as tm
import numpy as np
import random as rnd

grid = np.matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])

element1 = np.matrix([[0,1],[0,1],[1,1]])
element2 = np.matrix([[0,1],[0,1],[0,1],[0,1]])
element3 = np.matrix([[1,1],[1,1]])
element4 = np.matrix([[0,1],[1,1],[0,1]])
element_arr = [element1,element2,element3,element4]

while True:
    tm.sleep(1)
    rnd.shuffle(element_arr)
    for i in element_arr:
        if i == element1:
            grid[0:2,0:3] = i
        elif i == element2:
            grid[0:2,0:3] = i
        elif i == element3:
            grid[0:2,0:4] = i
        elif i == element4:
            grid[0:3,0:3] = i
        print grid
        tm.sleep(3)
