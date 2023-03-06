# Asadullah Al Galib, HSTU, CSE-17

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.title("Bresenham Line Drawing")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
xticks_ = []
yticks_ = []
for i in range(100):
    xticks_.append(i)
    xticks_.append(i*-1)
    yticks_.append(i)
    yticks_.append(i*-1)

plt.xticks(xticks_)
plt.yticks(yticks_)

# Empty list to store coordinates
xcoordinates = []
ycoordinates = []


def bres(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx
    print('x = %s, y = %s' % (x, y))

    while x <= x2 and y <= y2:
        print('x = %s, y = %s, p = %s' % (x, y, p))
        xcoordinates.append(x)
        ycoordinates.append(y)
        if p >= 0:
            y = y + 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1


# (x1, y1) = (20, 10), (x2, y2) = (30, 18)
x1 = int(input("Enter the x coordinate of starting point: "))
y1 = int(input("Enter the y coordinate of starting point: "))
x2 = int(input("Enter the x coordinate of end point: "))
y2 = int(input("Enter the y coordinate of end point: "))
bres(x1, y1, x2, y2)


plt.scatter(xcoordinates, ycoordinates, color='g')
for i, j in zip(xcoordinates, ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))

plt.show()
