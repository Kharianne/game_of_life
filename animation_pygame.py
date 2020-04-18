import pygame as pg
import numpy as np
from game_of_life import generate_new
from copy import deepcopy

starting = np.random.randint(2, size=(10, 10))

white = (255, 255, 255)
black = (0, 0, 0)
grey = (220, 220, 220)
size = 30
square_height = 30


def draw_matrix(surface, matrix):
    global white, black, square_height
    height = square_height
    for line_in, line in enumerate(matrix):
        for column_in, column in enumerate(line):
            if matrix[line_in, column_in] == 1:
                pg.draw.rect(surface, white,
                             pg.Rect(line_in * height, column_in * height,
                                     height, height))
            if matrix[line_in, column_in] == 0:
                pg.draw.rect(surface, black,
                             pg.Rect(line_in * height, column_in * height,
                                     height, height))

            # Drawing grid lines over squares
            pg.draw.line(surface, grey,
                         (line_in * height, column_in * height),
                         (height * len(matrix), column_in * height))
            pg.draw.line(surface, grey,
                         (line_in * height, column_in * height),
                         (height * line_in, height * len(line)))


def redraw_window(surface, matrix):
    surface.fill((0, 0, 0))
    draw_matrix(surface, matrix)
    pg.display.update()


def main():
    global size, square_height
    pg.init()
    matrix = np.random.randint(2, size=(size, size))
    width = size * square_height
    win = pg.display.set_mode((width, width))
    clock = pg.time.Clock()
    flag = True
    while flag:
        pg.time.delay(60)
        clock.tick(10)
        redraw_window(win, matrix)
        prev_matrix = deepcopy(matrix)
        matrix = generate_new(matrix)
        if np.array_equal(prev_matrix, matrix):
            flag = False
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONUP:
                pass
            if event.type == pg.QUIT:
                flag = False
    pg.quit()


if __name__=="__main__":
    main()