import time as tm
import numpy as np
import random as rnd
import element as el

x = el.Element()

grid = np.matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])

while True:
    tm.sleep(1)
    element_arr = x.element_arr
    element_arr = rnd.shuffle(element_arr)
    for i in element_arr:
        x = rnd.randint(0,4)
        grid[0:4,x:x+2] = i
        print grid
        tm.sleep(3)
