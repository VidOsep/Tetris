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

el = element.Element(3)
el.chooseRandom()

print(el.isTouching(grid))
while True:

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                el.moveRight()
            elif event.key == pg.K_LEFT:
                el.moveLeft()
    drawMatrix(grid, DISPLAYSURF)
    pg.display.update()
