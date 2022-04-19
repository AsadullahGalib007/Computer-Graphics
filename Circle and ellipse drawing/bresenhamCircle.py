# Thanks to MADAM🖤
# Asadullah Al Galib, CSE-17
#!/usr/bin/env python3
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')
plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
xticks_ = []
yticks_ = []
for i in range(100):
    xticks_.append(i)
    xticks_.append(i*-1)
    yticks_.append(i)
    yticks_.append(i*-1)

plt.xticks(xticks_)
plt.yticks(yticks_)

# for storing coordinates of first octant
xcoordinates = []
ycoordinates = []

# for storing all coordinates after translation
Xcoordinates = []
Ycoordinates = []


def translation(a, b):
    # But the center is not always at (0,0), so we have to translate the whole object
    Xcoordinates.append(a)
    Ycoordinates.append(b)
    for i in range(len(xcoordinates)):
        x = a + xcoordinates[i]
        y = b + ycoordinates[i]
        Xcoordinates.append(x)
        Ycoordinates.append(y)


def eightWaySymmetry():
    x_coordinates = xcoordinates.copy()
    y_coordinates = ycoordinates.copy()

    # Points for second octant
    for i in range(len(x_coordinates)):
        x = y_coordinates[i]
        y = x_coordinates[i]
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for third octant
    for i in range(len(x_coordinates)):
        x = y_coordinates[i]
        y = x_coordinates[i] * -1
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for fourth octant
    for i in range(len(x_coordinates)):
        x = x_coordinates[i]
        y = y_coordinates[i] * -1
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for fifth octant
    for i in range(len(x_coordinates)):
        x = x_coordinates[i] * - 1
        y = y_coordinates[i] * -1
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for sixth octant
    for i in range(len(x_coordinates)):
        x = y_coordinates[i] * - 1
        y = x_coordinates[i] * -1
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for seventh octant
    for i in range(len(x_coordinates)):
        x = y_coordinates[i] * - 1
        y = x_coordinates[i]
        xcoordinates.append(x)
        ycoordinates.append(y)

    # Points for eight octant
    for i in range(len(x_coordinates)):
        x = x_coordinates[i] * - 1
        y = y_coordinates[i]
        xcoordinates.append(x)
        ycoordinates.append(y)


def midPoint(r):
    # It will just provide points of first octant
    x0, y0 = 0, r
    xcoordinates.append(x0)
    ycoordinates.append(y0)

    p = 3 - 2*r

    while x0 <= y0:
        if p < 0:
            p = p + 4 * x0 + 6
            x0 = x0 + 1

        else:
            p = p + 4 * (x0-y0) + 10
            x0 = x0 + 1
            y0 = y0 - 1

        if x0 <= y0:
            xcoordinates.append(x0)
            ycoordinates.append(y0)


x, y, r = -11, -10, 6
midPoint(r)
eightWaySymmetry()
translation(x, y)


plt.scatter(Xcoordinates, Ycoordinates, color='g')
for i, j in zip(Xcoordinates, Ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))
plt.show()
