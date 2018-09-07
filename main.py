import sys
import time as tm
import numpy as np
import random as rnd
import element
import pygame as pg
from drawSquares import drawMatrix

pg.init()

DISPLAYSURF = pg.display.set_mode((200, 400))
pg.display.set_caption('Tetris 1.0')

grid = np.zeros((20, 10))

white = pg.Color(255, 255, 255)

DISPLAYSURF.fill(white)
pg.display.update()

elements = element.Element()

while True:
    tm.sleep(1)
    elements.chooseRandom()
    element = elements.element
    elementX = rnd.randint(0, 7)
    x = element.shape[1]
    y = element.shape[0]
    for i in range(20):
        tm.sleep(0.5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    elements.drawToGrid(grid,i,elementX+1,element)
                    elementX += 1
                elif event.key == pg.K_LEFT:
                    elements.drawToGrid(grid,i,elementX-1,element)
                    elementX -= 1
        elements.drawToGrid(grid,elementX,i,element)
        grid[i - 1:i, elementX:elementX + x] \
            = np.zeros((1,x))
        drawMatrix(grid, DISPLAYSURF)
        pg.display.update()
        if elements.isTouching(grid[i + y:i + y + 1, elementX:elementX + x],
                             grid[i + y - 1:i + y, elementX:elementX + x]):
            break