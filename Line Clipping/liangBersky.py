# Asadullah Al Galib, HSTU, CSE-17
# !/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib import style


style.use('ggplot')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
xticks_ = []
yticks_ = []
for i in range(100):
    xticks_.append(i)
    xticks_.append(i * -1)
    yticks_.append(i)
    yticks_.append(i * -1)
plt.xticks(xticks_)
plt.yticks(yticks_)


# for storing coordinates of first points
x1coordinates = []
y1coordinates = []

# for storing coordinates last points
x2coordinates = []
y2coordinates = []

# for storing coordinates of the viewport
Xcoordinates = []
Ycoordinates = []

# for storing cut points
xcut = []
ycut = []

def drawing():
    # The plot draws line form a point to another,
    # In order to complete the polygon the first coordinate need to append again
    plt.title("Liang Bersky Line Clipping")
    Xcoordinates.append(Xcoordinates[0])
    Ycoordinates.append(Ycoordinates[0])
    plt.plot(Xcoordinates, Ycoordinates, color='g')
    for i, j in zip(Xcoordinates, Ycoordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

    # xcoordinates.append(xcoordinates[0])
    # ycoordinates.append(ycoordinates[0])
    c = ['b', 'c', 'r', 'm', 'y', 'k', 'w', 'b', 'c', 'r', 'm', 'y', 'k', 'w']
    # plt.plot([6,8], [6,9], color='b')
    for i in range(len(x1coordinates)):
        plt.plot([x1coordinates[i], x2coordinates[i]], [y1coordinates[i], y2coordinates[i]], color=c[i])
    for i, j in zip(x1coordinates, y1coordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

    for i, j in zip(x2coordinates, y2coordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

    for i, j in zip(xcut, ycut):
        plt.text(i, j, '({}, {})'.format(i, j))
    plt.scatter(xcut, ycut, color = 'r')
    plt.show()



def generate_viewport():
    # Generating viewport
    vx_min, vy_min, vx_max, vy_max = 20, 20, 90, 70
    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_max)

    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_max)


def liang_bersky(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    xmin = Xcoordinates[0]
    xmax = Xcoordinates[1]
    ymin = Ycoordinates[0]
    ymax = Ycoordinates[3]
    p = []
    q = []
    p.append(-dx)
    p.append(dx)
    p.append(-dy)
    p.append(dy)

    q.append(x1 - xmin)
    q.append(xmax - x1)
    q.append(y1 - ymin)
    q.append(ymax - y1)
    print(p[0], p[1], p[2], p[3])
    print(q[0], q[1], q[2], q[3])

    for i in range(4):
        if p[i] == 0:
            #print("line ({:d}, {:d}),({:d}, {:d}) is parallel to the boundary.".format(x1, y1, x2, y2))
            # the line is vertical to the boundary
            if q[i]>=0:
                if i<2:
                    if y1 < ymin:
                        y1 = ymin
                    if y2 > ymax:
                        y2 = ymax
                    xcut.append(x1)
                    xcut.append(x2)
                    ycut.append(y1)
                    ycut.append(y2)
                    print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
                    drawing()
                    return
                if i>1:
                    if x1 < xmin:
                        x1 = xmin
                    if x2 > xmax:
                        x2 = xmax
                    xcut.append(x1)
                    xcut.append(x2)
                    ycut.append(y1)
                    ycut.append(y2)
                    print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
                    drawing()
                    return
            else:
                print("Line is rejected")
                drawing()
                return
    t1, t2 = 0,1
    for i in range(4):
        tmp = q[i]/p[i]
        if p[i]<0:
            if t1<=tmp:
                t1 = tmp
        else:
            if t2>tmp:
                t2 = tmp
    if t1 < t2:
        xx1 = x1 + t1 * p[1]
        xx2 = x1 + t2 * p[1]
        yy1 = y1 + t1 * p[3]
        yy2 = y1 + t2 * p[3]
        # plt.scatter([xx1, xx2], [yy1, yy2], color = 'r')
        # plt.text(xx1, yy1, '({}, {})'.format(xx1, yy1))
        # plt.text(xx2, yy2, '({}, {})'.format(xx2, yy2))
        xcut.append(xx1)
        xcut.append(xx2)
        ycut.append(yy1)
        ycut.append(yy2)
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (xx1, yy1, xx2, yy2))
        drawing()
        return
    else:
        print("Line is rejected")
        drawing()
        return
#(10, 30),(80, 90)
#(10, 10),(10, 40)
#(10, 50),(100, 50)
#(10, 50),(40, 80)
#(10, 60),(30, 90)
#(20, 30),(20, 90)
#(10, 30),(80, 90)
#(40, 40),(60, 60)
def user_input():
    n = int(input("Enter the number of lines: "))
    for i in range(n):
        x1 = int(input("Enter x1-coordinate of the line-{:d}: ".format(i + 1)))
        y1 = int(input("Enter y1-coordinate of the line-{:d}: ".format(i + 1)))
        x2 = int(input("Enter x2-coordinate of the line-{:d}: ".format(i + 1)))
        y2 = int(input("Enter y2-coordinate of the line-{:d}: ".format(i + 1)))
        x1coordinates.append(x1)
        y1coordinates.append(y1)
        x2coordinates.append(x2)
        y2coordinates.append(y2)
        liang_bersky(x1, y1, x2, y2)


generate_viewport()
user_input()

