import sys
import numpy as np
import element
import pygame as pg
from drawSquares import drawMatrix

pg.init()

DISPLAYSURF = pg.display.set_mode((400, 400))
pg.display.set_caption('Tetris 1.0')

"""
pg.mixer.init()
pg.mixer.music.load("ginandjuice.mp3")
pg.mixer.music.set_volume(0.7)
pg.mixer.music.play()
"""

grid = np.zeros((20, 10), dtype=int)
colors = np.empty((20,10),dtype=object)

BG = pg.Color(0, 64, 128)

# za debuggiranje
el = element.Element(3)

score = 0

#initialize font
pg.font.init()
bigf = pg.font.SysFont('Comic Sans MS', 40)
smallf = pg.font.SysFont('Comic Sans MS', 20)


def title(x, y):
    title_ = bigf.render('TETRIS', True, (255, 255, 255))
    subtitle_ = smallf.render('MADE BY VID', True, (255, 255, 255))
    
    title_rect = title_.get_rect(center=(200/2, 50))
    subtitle_rect = subtitle_.get_rect(center=(200/2, 100))

    DISPLAYSURF.blit(title_, title_rect)
    DISPLAYSURF.blit(subtitle_, subtitle_rect)

def scoreBlit(score):
    score_ = smallf.render("Tocke: " + str(score), True, (255, 255, 255))
    score_rect = score_.get_rect(center=(200/2, 300))

    DISPLAYSURF.blit(score_, score_rect)

def checkForLines():
    global grid
    global score
    for i in range(len(grid)):
        if np.sum(grid[i])==10:
            score+=10
            grid = np.delete(grid,i,axis=0)
            grid = np.concatenate((np.zeros((1,10),dtype=int),grid))


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
                el.rotateRight(grid)
            elif event.key == pg.K_a:
                # zarotiraj trenutni tetronim
                el.shiftElArrayLeft()
            elif event.key == pg.K_DOWN:
                if t==750:
                    t=100
                else:
                    t=750
                pg.time.set_timer(PREMIKDOL, t)
        # lokalno definiran event
        if event.type == PREMIKDOL:
            prejsnja = grid
            prejsnjac = colors
            grid,colors = el.draw(grid,colors)
            if not(el.moveDown(prejsnja)):    # tetronimo doseze konec
                # preveri za ustvarjene linije

                checkForLines()

                el = element.Element(3)
                if el.isColliding(el.x,el.y,grid):
                    pg.quit()
                    sys.exit()
            else:
                grid = prejsnja
                colors = prejsnjac

    # izris matrike
    prejsnja = grid
    prejsnjac = colors
    grid,colors = el.draw(grid,colors)

    DISPLAYSURF.fill(BG)
    title(0,0)
    scoreBlit(score)

    drawMatrix(grid,colors, DISPLAYSURF)
    grid = prejsnja
    colors = prejsnjac

    pg.display.update()
