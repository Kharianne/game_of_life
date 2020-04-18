import pytest as pt
import numpy as np
from game_of_life import get_neighbours_values

matrix = np.array([[1, 0, 1, 0],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 1, 1, 1]])
test_values = [
    (0, 0, matrix, 1),
    (3, 0, matrix, 2),
    (1, 1, matrix, 5),
    (3, 3, matrix, 2)
]


@pt.mark.parametrize("line_num,cell_num,curr,expected", test_values)
def test_get_neighbours_values(line_num, cell_num, curr, expected):
    assert get_neighbours_values(line_num, cell_num, curr) == expected
