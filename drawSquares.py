import pygame as pg

def drawMatrix(matrix,display):

    white = (255, 255, 255)
    red = (200,50,50)

    x_pos = 5
    y_pos = 5
    margin = 5
    width = 38
    height = 38


    for y in range(9):

        for i in range(7):

            if matrix[y][i] == 1:
                pg.draw.rect(display, white, (x_pos, y_pos, width, height))
            else:
                pg.draw.rect(display, red, (x_pos, y_pos, width, height))

            x_pos += width + margin
        y_pos += height + margin
        x_pos = 5