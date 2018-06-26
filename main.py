import sys
import time as tm
import numpy as np
import random as rnd
import element as el
import pygame as pg
from drawSquares import drawMatrix

pg.init()
indexOfTetronim = el.Element()


DISPLAYSURF = pg.display.set_mode((306, 393))
pg.display.set_caption('Tetris 1.0')

grid = np.zeros((20, 10))
stable_arr = indexOfTetronim.element_arr
blank_line = np.zeros((1, 10))

white = pg.Color(255, 255, 255)

DISPLAYSURF.fill(white)
pg.display.update()

# def rotate(element):
#     return zip(element[::-1])


def check_if_touching(last_zero, bottom):
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


while True:
    tm.sleep(1)
    ele_arr = stable_arr
    rnd.shuffle(ele_arr)
    for tetronim in ele_arr:
        indexOfTetronim = rnd.randint(0, 4)
        x = tetronim.shape[1]
        y = tetronim.shape[0]
        for loopCycle in range(20):
            tm.sleep(0.7)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        grid[loopCycle:loopCycle + y, indexOfTetronim:indexOfTetronim + x + 1] \
                            = np.zeros((tetronim.shape[0], tetronim.shape[1] + 1))
                        indexOfTetronim += 1
                    elif event.key == pg.K_LEFT:
                        indexOfTetronim -= 1
            grid[loopCycle:loopCycle + y, indexOfTetronim:indexOfTetronim + x] = tetronim
            grid[loopCycle - 1:loopCycle, indexOfTetronim:indexOfTetronim + x] \
                = blank_line[indexOfTetronim:indexOfTetronim + x]
            drawMatrix(grid, DISPLAYSURF)
            pg.display.update()
            if check_if_touching(grid[loopCycle + y:loopCycle + y + 1, indexOfTetronim:indexOfTetronim + x],
                                 grid[loopCycle + y - 1:loopCycle + y, indexOfTetronim:indexOfTetronim + x]):
                break
        tm.sleep(5)
