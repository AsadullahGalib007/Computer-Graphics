# Asadullah Al Galib, HSTU, CSE-17

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.title("Digital Differential Analyzer (DDA) Line Drawing Algorithm")
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


def dda(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    m = dy/dx

    if m < 1:

        while x <= x2:
            xcoordinates.append(round(x))
            ycoordinates.append(round(y))
            x = x + 1
            y = y + m

    elif m > 1:
        while y <= y2:
            print(x, y)
            xcoordinates.append(round(x))
            ycoordinates.append(round(y))
            x = x + 1/m
            y = y + 1

    else:  # m = 1
        while x <= x2 or y <= y2:
            xcoordinates.append(round(x))
            ycoordinates.append(round(y))
            x = x + 1
            y = y + 1


# (x1, y1) = (20, 10), (x2, y2) = (30, 18)
x1 = int(input("Enter the x-coordinate of starting point: "))
y1 = int(input("Enter the y-coordinate of starting point: "))
x2 = int(input("Enter the x-coordinate of end point: "))
y2 = int(input("Enter the y-coordinate of starting point: "))
dda(x1, y1, x2, y2)
plt.scatter(xcoordinates, ycoordinates, color='g')
for i, j in zip(xcoordinates, ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))

# Graph title
plt.title("DDA Line Drawing Algorithm")
# Show the plot
plt.show()
