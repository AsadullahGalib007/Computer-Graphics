# Asadullah Al Galib, HSTU, CSE-17
#!/usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')
plt.title("Rotation")
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

# for storing all coordinates after reflection
Xcoordinates = []
Ycoordinates = []


def rotation(tht):
    # first let's convert the coordinates into 2D-array
    B = np.vstack((xcoordinates, ycoordinates))

    a = round(math.cos(tht))
    b = round(math.sin(tht))

    A = [[a, -b],
        [b, a]]
    result = np.dot(A, B)

	# 1st dimension of the 2D array are all X-cordinates
    for i in range(len(result[0])):
        Xcoordinates.append(result[0][i])

	# 2nd dimension of the 2D array are all Y-cordinates
    for i in range(len(result[0])):
        Ycoordinates.append(result[1][i])


# assuming a triangle: a(2,2), b(10,2), c(5,5)
n = int(input("Enter the number of points:"))
for i in range(n):
    x = int(input("Enter x-coordinate of the point-{:d}: ".format(i+1)))
    y = int(input("Enter y-coordinate of the point-{:d}: ".format(i+1)))
    xcoordinates.append(x)
    ycoordinates.append(y)

tht = int(input("Enter rotation degree: "))

rotation(tht)

# The plot draws line form a point to another,
# In order to complete the polygon the first coordinate need to append again
#After reflection
Xcoordinates.append(Xcoordinates[0])
Ycoordinates.append(Ycoordinates[0])
plt.plot(Xcoordinates, Ycoordinates, color='g')
for i, j in zip(Xcoordinates, Ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))
    #print('({}, {})'.format(i, j))


#Before reflection
xcoordinates.append(xcoordinates[0])
ycoordinates.append(ycoordinates[0])
plt.plot(xcoordinates, ycoordinates, color='b')
for i, j in zip(xcoordinates, ycoordinates):
    plt.text(i, j, '({}, {})'.format(i, j))
plt.show()
