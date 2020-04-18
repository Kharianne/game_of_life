import matplotlib.pyplot
from matplotlib.animation import FuncAnimation
import numpy as np
from game_of_life import generate_new

current = np.random.randint(2, size=(30, 30))


def update(data):
    global current
    new = generate_new(current)
    current = new
    mat.set_data(generate_new(current))
    return [mat]


fig, ax = matplotlib.pyplot.subplots()
mat = ax.matshow(current, cmap="Greys")
ani = FuncAnimation(fig, update, interval=50, save_count=50)
matplotlib.pyplot.show()

