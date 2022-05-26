import sys
import time as tm
import numpy as np
import random as rnd
import element
import pygame as pg
from drawSquares import drawMatrix

pg.init()

DISPLAYSURF = pg.display.set_mode((400, 400))
pg.display.set_caption('Tetris 1.0')

pg.mixer.init()
pg.mixer.music.load("ginandjuice.mp3")
pg.mixer.music.set_volume(0.7)
pg.mixer.music.play()

grid = np.zeros((20, 10), dtype=int)
colors = np.empty((20,10),dtype=object)

BG = pg.Color(0, 64, 128)


DISPLAYSURF.fill(BG)
pg.display.update()

# za debuggiranje
el = element.Element(3)

score = 0

#initialize font
pg.font.init()
bigf = pg.font.SysFont('Comic Sans MS', 40)
smallf = pg.font.SysFont('Comic Sans MS', 20)


def title(x, y):
    naslov = bigf.render('TETRIS', True, (255, 255, 255))
    subnaslov = smallf.render('MADE BY VID', True, (255, 255, 255))
    
    naslov_rect = naslov.get_rect(center=(200/2, 50))
    subnaslov_rect = subnaslov.get_rect(center=(200/2, 100))


    DISPLAYSURF.blit(naslov, naslov_rect)
    DISPLAYSURF.blit(subnaslov, subnaslov_rect)


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
    
    title(0,0)
    
    pg.display.update()
