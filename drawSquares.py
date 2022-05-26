import pygame as pg

def drawMatrix(matrix,colors,display):

    LIGHT_GREEN = (124,252,0)
    LIGHT_BLUE = (32,178,170)
    LIGHT_RED = (255,0,0)
    YELLOW = (255,255,0)
    PURPLE = (128,0,128)

    PLAYAREABG = pg.Color(10, 10, 10)
    
    white = (255, 255, 255)
    red = (200,50,50)

    start_pos=200
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