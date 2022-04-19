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


def ellipse(rx, ry, xc, yc):
    # REGION 1
    x = 0
    y = ry
    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +
          (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    while dx <= dy:
        # 4-way symmetry
        xcoordinates.append(x+xc)
        ycoordinates.append(y+yc)

        xcoordinates.append(-x+xc)
        ycoordinates.append(y+yc)

        xcoordinates.append(x+xc)
        ycoordinates.append(-y+yc)

        xcoordinates.append(-x+xc)
        ycoordinates.append(-y+yc)

        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

        # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))
    # Plotting points of region 2
    while (y >= 0):
        # 4-way symmetry
        xcoordinates.append(x+xc)
        ycoordinates.append(y+yc)

        xcoordinates.append(-x+xc)
        ycoordinates.append(y+yc)

        xcoordinates.append(x+xc)
        ycoordinates.append(-y+yc)

        xcoordinates.append(-x+xc)
        ycoordinates.append(-y+yc)

        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)


# a = horizontal length, b = vertical length
x, y, a, b = 50, 50, 10, 15
ellipse(a, b, x, y)


plt.scatter(xcoordinates, ycoordinates, color='g')
for i, j in zip(xcoordinates, ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))
plt.show()
