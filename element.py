import numpy as np

class Element:
    element1 = np.matrix([[0, 1], [0, 1], [1, 1], [0, 0]])
    element2 = np.matrix([[0, 1], [0, 1], [0, 1], [0, 1]])
    element3 = np.matrix([[1, 1], [1, 1], [0, 0], [0, 0]])
    element4 = np.matrix([[0, 1], [1, 1], [0, 1], [0, 0]])
    element_arr = [element1, element2, element3, element4]
    def check_if_touching(self,grid,under_el):
        if any(grid[under_el]):
            return 3

