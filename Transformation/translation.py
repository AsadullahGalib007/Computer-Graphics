# Thanks to MADAM🖤
# Asadullah Al Galib, CSE-17
#!/usr/bin/env python3
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')
plt.title("Translation")
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


def translation(tx, ty):

    for i in range(len(xcoordinates)):
        x = tx + xcoordinates[i]
        y = ty + ycoordinates[i]
        print(x, y)
        Xcoordinates.append(x)
        Ycoordinates.append(y)


# assuming a triangle: a(2,2), b(10,2), c(5,5)
n = int(input("Enter the number of points:"))
for i in range(n):
    x = int(input("Enter x-coordinate of the point-{:d}: ".format(i+1)))
    y = int(input("Enter y-coordinate of the point-{:d}: ".format(i+1)))
    xcoordinates.append(x)
    ycoordinates.append(y)


tx = int(input("Enter tx: "))
ty = int(input("Enter ty: "))
translation(tx, ty)

# The plot draws line form a point to another,
# In order to complete the polygon the first coordinate need to append again
#After translation
Xcoordinates.append(Xcoordinates[0])
Ycoordinates.append(Ycoordinates[0])
plt.plot(Xcoordinates, Ycoordinates, color='g')
for i, j in zip(Xcoordinates, Ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))

#Before translation
xcoordinates.append(xcoordinates[0])
ycoordinates.append(ycoordinates[0])
plt.plot(xcoordinates, ycoordinates, color='b')
for i, j in zip(xcoordinates, ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))
plt.show()
