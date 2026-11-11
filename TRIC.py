#Triangle inside a Circle using Bresenham's Circle and Line Algorithm
import matplotlib.pyplot as plt

xc, yc, r = 0, 0, 10

x_circle = []
y_circle = []

# Bresenham's Circle Algorithm
def draw_circle(x, y):
    pts = [
        (xc+x, yc+y),
        (xc-x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x)
    ]

    for px, py in pts:
        x_circle.append(px)
        y_circle.append(py)


x = 0
y = r
p = 3 - 2*r

while x <= y:
    draw_circle(x, y)

    if p < 0:
        p += 4*x + 6
    else:
        p += 4*(x-y) + 10
        y -= 1

    x += 1


# Triangle vertices on the circle
A = (0, 10)
B = (-9, -4)
C = (9, -4)

# Bresenham's Line Algorithm
def draw_line(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x, y = x1, y1

    points_x = []
    points_y = []

    if dx >= dy:
        p = 2*dy-dx

        while x != x2:
            points_x.append(x)
            points_y.append(y)

            if p >= 0:
                y += sy
                p += 2*(dy-dx)
            else:
                p += 2*dy

            x += sx

    else:
        p = 2*dx-dy

        while y != y2:
            points_x.append(x)
            points_y.append(y)

            if p >= 0:
                x += sx
                p += 2*(dx-dy)
            else:
                p += 2*dx

            y += sy

    points_x.append(x2)
    points_y.append(y2)

    return points_x, points_y


# Draw all three sides
triangle_sides = [
    (A, B),
    (B, C),
    (C, A)
]

plt.scatter(x_circle, y_circle, color="blue", s=12)

for start, end in triangle_sides:
    lx, ly = draw_line(
        start[0], start[1],
        end[0], end[1]
    )

    plt.scatter(lx, ly, color="red", s=12)

plt.title("Triangle Inside a Circle")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()
