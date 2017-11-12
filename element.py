import numpy as np
import mouse

class Element:
    element1 = np.matrix([[0, 1], [0, 1], [1, 1]])
    element2 = np.matrix([[1], [1], [1], [1]])
    element3 = np.matrix([[1, 1], [1, 1]])
    element4 = np.matrix([[0, 1], [1, 1], [0, 1]])
    element_arr = [element1, element2, element3, element4]
    def check_if_touching(self,grid,under_el):
        if any(grid[under_el]):
            return 3
    def rotate(self,element):
        if mouse.is_pressed("space"):
            return zip(element[::-1])
    def check_if_b_pressed(self):
        if mouse.is_pressed("a"):
            return True
    def check_if_b_pressed(self):
        if mouse.is_pressed("b"):
            return True


