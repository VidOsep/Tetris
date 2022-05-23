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

WHITE = pg.Color(255, 255, 255)

DISPLAYSURF.fill(WHITE)
pg.display.update()

# za debuggiranje
el = element.Element(3)
el.chooseRandom()

print(el.isTouching(grid))

PREMIKDOL,t = pg.USEREVENT+1,1000
pygame.time.set_timer(MOVEEVENT, t)


while True:

    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                # premik desno
                el.moveRight()
            elif event.key == pg.K_LEFT:
                # premik levo
                el.moveLeft()
            elif event.key == pg.K_UP:
                # zarotiraj trenutni tetronim
                pass
                el.rotateRight()

        # lokalno definiran event
        if event.type==PREMIKDOL:
            el.moveDown()

    # izris matrike
    drawMatrix(grid, DISPLAYSURF)
    pg.display.update()
