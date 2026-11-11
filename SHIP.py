import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 800)
ax.set_ylim(0, 500)
ax.set_title("Ship Moving Across Waves")
ax.set_facecolor("skyblue")

# Draw the water
x = np.linspace(0, 800, 800)
wave, = ax.plot(x, 100 + 10 * np.sin(x / 20), 'b')

# Create ship components
hull = plt.Polygon([[0, 0], [1, 0], [1, 1]], color='brown')
ax.add_patch(hull)

mast, = ax.plot([], [], 'k', linewidth=3)

sail1 = plt.Polygon([[0, 0], [1, 0], [0, 1]], color='white', ec='black')
sail2 = plt.Polygon([[0, 0], [1, 0], [0, 1]], color='white', ec='black')

ax.add_patch(sail1)
ax.add_patch(sail2)


def update(frame):
    # Animate the waves
    wave.set_ydata(100 + 10 * np.sin(x / 20 + frame / 5))

    # Calculate ship position
    sx = frame % 900
    sy = 150 + 5 * np.sin(frame / 5)

    # Draw the ship hull
    hull.set_xy([
        (sx, sy),
        (sx + 120, sy),
        (sx + 100, sy - 30),
        (sx + 20, sy - 30)
    ])

    # Draw the mast
    mast.set_data(
        [sx + 60, sx + 60],
        [sy, sy + 90]
    )

    # Draw the first sail
    sail1.set_xy([
        (sx + 60, sy + 80),
        (sx + 60, sy + 10),
        (sx + 20, sy + 10)
    ])

    # Draw the second sail
    sail2.set_xy([
        (sx + 65, sy + 70),
        (sx + 65, sy + 20),
        (sx + 100, sy + 20)
    ])

    return wave, hull, mast, sail1, sail2


ani = FuncAnimation(
    fig,
    update,
    frames=900,
    interval=30,
    blit=True
)

plt.show()