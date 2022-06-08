import sys
import numpy as np
import pygame as pg

from element import Element

pg.init()

DISPLAYSURF = pg.display.set_mode((400, 400))
pg.display.set_caption('Tetris')

ARROW_SIZE = (50,50)

arrow_d = pg.image.load("arrow.png")
arrow_d = pg.transform.scale(arrow_d, ARROW_SIZE)

arrow_l = pg.transform.rotate(arrow_d, 90)
arrow_l = pg.transform.scale(arrow_l, ARROW_SIZE)

arrow_u = pg.transform.rotate(arrow_d, 180)
arrow_u = pg.transform.scale(arrow_u, ARROW_SIZE)

arrow_r = pg.transform.rotate(arrow_d, 270)
arrow_r = pg.transform.scale(arrow_r, ARROW_SIZE)

# igralna povrsina sestavljena iz binarne matrike - grid in matrike nizov - colors (oblika in barve)
grid = np.zeros((20, 10), dtype=int)
colors = np.empty((20, 10), dtype=object)

BG = pg.Color(0, 64, 128)  # barva ozadja

el = Element(3)

score = 0

# fonti
pg.font.init()
bigf = pg.font.SysFont('georgia', 40)
smallf = pg.font.SysFont('georgia', 20)
navodilaf = pg.font.SysFont('georgia', 11)


def drawMatrix(matrix, colors, display):
    # izrise igralno povrsino na display
    LIGHT_GREEN = (124, 252, 0)
    LIGHT_BLUE = (32, 178, 170)
    LIGHT_RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)

    PLAYAREABG = pg.Color(10, 10, 10)

    white = (255, 255, 255)
    red = (200, 50, 50)

    start_pos = 200
    x_pos = start_pos
    y_pos = 0
    margin = 0
    width = 20
    height = 20

    for i in range(20):
        for j in range(10):
            if matrix[i][j] == 1:
                if colors[i][j] == "LIGHT_GREEN":
                    pg.draw.rect(display, LIGHT_GREEN, (x_pos, y_pos, width, height))
                elif colors[i][j] == "LIGHT_BLUE":
                    pg.draw.rect(display, LIGHT_BLUE, (x_pos, y_pos, width, height))
                elif colors[i][j] == "LIGHT_RED":
                    pg.draw.rect(display, LIGHT_RED, (x_pos, y_pos, width, height))
                elif colors[i][j] == "YELLOW":
                    pg.draw.rect(display, YELLOW, (x_pos, y_pos, width, height))
                elif colors[i][j] == "PURPLE":
                    pg.draw.rect(display, PURPLE, (x_pos, y_pos, width, height))
                else:
                    pg.draw.rect(display, red, (x_pos, y_pos, width, height))
            else:
                pg.draw.rect(display, PLAYAREABG, (x_pos, y_pos, width, height))
            x_pos += width + margin
        y_pos += height + margin
        x_pos = start_pos


def title(x=0, y=0):
    # izrise naslov na zaslon
    title_ = bigf.render('TETRIS', True, (255, 255, 255))
    subtitle_ = smallf.render('MADE BY VID', True, (255, 255, 255))

    title_rect = title_.get_rect(center=(200 / 2, 50))
    subtitle_rect = subtitle_.get_rect(center=(200 / 2, 100))

    DISPLAYSURF.blit(title_, title_rect)
    DISPLAYSURF.blit(subtitle_, subtitle_rect)


def scoreBlit(score):
    # izrise tocke na zaslon
    score_ = smallf.render("Tocke: " + str(score), True, (255, 255, 255))
    score_rect = score_.get_rect(center=(200 / 2, 370))

    DISPLAYSURF.blit(score_, score_rect)
    
def instructionsBlit():
    # izrise navodila za premikanje
    shift_y = 55
    au_rect = arrow_d.get_rect(center=(200 / 2 - 40, 100+shift_y*1))
    pg.draw.rect(DISPLAYSURF, (255,255,255), au_rect.inflate(3,3))
    DISPLAYSURF.blit(arrow_u, au_rect)
    
    ad_rect = arrow_d.get_rect(center=(200 / 2 - 40, 100+shift_y*2))
    pg.draw.rect(DISPLAYSURF, (255,255,255), ad_rect.inflate(3,3))
    DISPLAYSURF.blit(arrow_d, ad_rect)
    
    al_rect = arrow_d.get_rect(center=(200 / 2 - 40, 100+shift_y*3))
    pg.draw.rect(DISPLAYSURF, (255,255,255), al_rect.inflate(3,3))
    DISPLAYSURF.blit(arrow_l, al_rect)
    
    ar_rect = arrow_d.get_rect(center=(200 / 2 - 40, 100+shift_y*4))
    pg.draw.rect(DISPLAYSURF, (255,255,255), ar_rect.inflate(3,3))
    DISPLAYSURF.blit(arrow_r, ar_rect)

    au_text = navodilaf.render('OBRAT', True, (255, 255, 255))
    au_rect = au_text.get_rect(center=(200 / 2+40, 100+shift_y*1))
    DISPLAYSURF.blit(au_text, au_rect)

    ad_text = navodilaf.render('POSPEŠI PADANJE', True, (255, 255, 255))
    ad_rect = ad_text.get_rect(center=(200 / 2+40, 100+shift_y*2))
    DISPLAYSURF.blit(ad_text, ad_rect)

    al_text = navodilaf.render('PREMIK LEVO', True, (255, 255, 255))
    al_rect = al_text.get_rect(center=(200 / 2+40, 100+shift_y*3))
    DISPLAYSURF.blit(al_text, al_rect)

    ar_text = navodilaf.render('PREMIK DESNO', True, (255, 255, 255))
    ar_rect = ar_text.get_rect(center=(200 / 2+40, 100+shift_y*4))
    DISPLAYSURF.blit(ar_text, ar_rect)



def checkForLines():
    # preverja za polne linije
    global grid, colors, score
    for i in range(len(grid)):
        if np.sum(grid[i]) == 10:  # odkrita polna linija
            score += 10
            grid = np.delete(grid, i, axis=0)
            grid = np.concatenate((np.zeros((1, 10), dtype=int), grid))

            colors = np.delete(colors, i, axis=0)
            colors = np.concatenate((np.empty((1, 10), dtype=object), colors))


MOVEDOWN, t = pg.USEREVENT + 1, 500
pg.time.set_timer(MOVEDOWN, t)

while True:
    # pregled vseh eventov
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
            elif event.key == pg.K_DOWN:
                # toggle hitrejsi padec
                if t == 500:
                    t = 150
                else:
                    t = 500
                pg.time.set_timer(MOVEDOWN, t)
        # lokalno definiran event - premik dol
        if event.type == MOVEDOWN:
            tempgrid = grid
            tempgridc = colors
            grid, colors = el.draw(grid, colors)
            if not (el.moveDown(tempgrid)):  # tetronimo doseze konec
                # preveri za ustvarjene linije
                checkForLines()
                # ustvari nov element, preveri ce ni starih ze pri vrhu
                el = Element(3)
                if el.isColliding(el.x, el.y, grid):
                    pg.quit()
                    sys.exit()
            else:
                grid = tempgrid
                colors = tempgridc

    # izris tetronima na matriko
    tempgrid = grid
    tempgridc = colors
    grid, colors = el.draw(grid, colors)

    # izris besedila
    DISPLAYSURF.fill(BG)
    title()
    scoreBlit(score)
    instructionsBlit()

    # izris matrike grid na zaslon
    drawMatrix(grid, colors, DISPLAYSURF)
    grid = tempgrid
    colors = tempgridc

    pg.display.update()
