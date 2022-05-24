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

grid = np.zeros((20, 10), dtype=int)
colors = np.empty((20,10),dtype=object)

WHITE = pg.Color(255, 255, 255)

DISPLAYSURF.fill(WHITE)
pg.display.update()

# za debuggiranje
el = element.Element(3)

PREMIKDOL,t = pg.USEREVENT+1,750
pg.time.set_timer(PREMIKDOL, t)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                # premik desno
                el.moveRight(grid)
            elif event.key == pg.K_LEFT:
                # premik levo
                el.moveLeft(grid)
            elif event.key == pg.K_UP:
                # zarotiraj trenutni tetronim
                el.rotateRight()
            elif event.key == pg.K_DOWN:
                # zarotiraj trenutni tetronim
                if t==750:
                    t=200
                else:
                    t=750
                pg.time.set_timer(PREMIKDOL, t)
        # lokalno definiran event
        if event.type == PREMIKDOL:
            prejsnja = grid
            prejsnjac = colors
            grid,colors = el.draw(grid,colors)
            if not(el.moveDown(prejsnja)):    
                el = element.Element(3)
            else:
                grid = prejsnja
                colors = prejsnjac

    # izris matrike
    prejsnja = grid
    prejsnjac = colors
    grid,colors = el.draw(grid,colors)
    drawMatrix(grid,colors, DISPLAYSURF)
    grid = prejsnja
    colors = prejsnjac
    pg.display.update()
