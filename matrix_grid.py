import sys
import time as tm
import numpy as np
import random as rnd
import element as el
import pygame as pg
from drawSquares import drawMatrix

pg.init()
x = el.Element()


DISPLAYSURF = pg.display.set_mode((306, 393))
pg.display.set_caption('Tetris 1.0')

grid = np.zeros((9,7))
stable_arr = x.element_arr
blank_line = [0,0,0,0,0,0,0]

white = pg.Color(255,255,255)

DISPLAYSURF.fill(white)
pg.display.update()

#def rotate(element):
#    return zip(element[::-1])


def check_if_touching(ting,bottom):
    try:
        if bottom == [1,1]:
            if ting.any():
                return True
        else:
            if bottom[0] == 1 and ting[0] == 1:
                return True
            elif bottom[1] == 1 and ting[1] == 1:
                return True
    except ValueError:
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
            tm.sleep(0.7)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        grid[y:y+z,x:x+j+1] = np.zeros((i.shape[0],i.shape[1]+1))
                        x += 1
                    elif event.key == pg.K_LEFT:
                        x -= 1
                    #elif event.key == pg.K_SPACE:
                        #space_pressed = True
            grid[y:y+z,x:x+j] = i
            grid[y-1:y, x:x+j] = blank_line[x:x+j]
            drawMatrix(grid,DISPLAYSURF)
            pg.display.update()
            if check_if_touching(grid[y+z:y+z+1,x:x+j],grid[y+z-1:y+z,x:x+j]):
                break
        tm.sleep(5)
