import time as tm
import numpy as np
import random as rnd
import element as el

x = el.Element()

grid = np.matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
stable_arr = x.element_arr
blank_line = [0,0,0,0,0,0,0]

while True:
    tm.sleep(1)
    ele_arr = stable_arr
    rnd.shuffle(ele_arr)
    for i in ele_arr:
        x = rnd.randint(0,4)
        for y in range(10):
            grid[y:y+4,x:x+2] = i
            print grid
            grid[y:y+1, 0:7] = blank_line
            tm.sleep(0.7)
        print grid
        tm.sleep(5)
