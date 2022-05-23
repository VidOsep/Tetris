import pygame as pg

def drawMatrix(matrix,display):

    white = (255, 255, 255)
    red = (200,50,50)

    x_pos = 0
    y_pos = 0
    margin = 0
    width = 20
    height = 20


    for i in range(20):
        for j in range(10):

            if matrix[i][j] == 1:
                pg.draw.rect(display, red, (x_pos, y_pos, width, height))
            else:
                pg.draw.rect(display, white, (x_pos, y_pos, width, height))

            x_pos += width + margin
        y_pos += height + margin
        x_pos = 5