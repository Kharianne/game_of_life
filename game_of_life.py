from copy import deepcopy

relative_loc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_neighbours_values(line_num, cell_num, curr):
    global relative_loc
    neighbours_value = 0
    for loc in relative_loc:
        if line_num + loc[0] < 0 or cell_num + loc[1] < 0:
            continue
        try:
            val = curr[line_num + loc[0], cell_num + loc[1]]
            neighbours_value += val
        except IndexError:
            continue
    return neighbours_value


"""
Každá živá buňka s méně než dvěma živými sousedy zemře.
Každá živá buňka se dvěma nebo třemi živými sousedy zůstává žít.
Každá živá buňka s více než třemi živými sousedy zemře.
Každá mrtvá buňka s právě třemi živými sousedy oživne.
"""


def generate_new(current):
    new = deepcopy(current)
    for line_num, line in enumerate(current):
        for cell_num, cell in enumerate(current):
            neighbours_value = get_neighbours_values(line_num, cell_num, current)
            if current[line_num, cell_num] == 1:
                if neighbours_value < 2:
                    new[line_num, cell_num] = 0
                if neighbours_value == 2 or neighbours_value == 3:
                    new[line_num, cell_num] = 1
                if neighbours_value > 3:
                    new[line_num, cell_num] = 0
            if current[line_num, cell_num] == 0:
                if neighbours_value == 3:
                    new[line_num, cell_num] = 1
    return new
