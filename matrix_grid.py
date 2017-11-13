import time as tm
import numpy as np
import random as rnd
import element as el

x = el.Element()

grid = np.matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
stable_arr = x.element_arr
blank_line = [0,0,0,0,0,0,0]


def check_if_touching(ting):
    if ting.any():
       return True

while True:
    tm.sleep(1)
    ele_arr = stable_arr
    rnd.shuffle(ele_arr)
    for i in ele_arr:
        x = rnd.randint(0,4)
        if i.shape == (2,2):
            z = 2
            j = 2
            k = 8
        elif i.shape == (3,2):
            z = 3
            j = 2
            k = 7
        elif i.shape == (4,1):
            z = 4
            j = 1
            k = 6
        for y in range(k):
            grid[y:y+z,x:x+j] = i
            print grid
            grid[y:y+z-(z-1), x:x+j] = blank_line[x:x+j]
            if check_if_touching(grid[y+z:y+z+1,x:x+j]):
                break
            tm.sleep(0.7)
        tm.sleep(5)
