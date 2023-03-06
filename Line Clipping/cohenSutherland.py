# Asadullah Al Galib, HSTU, CSE-17
#!/usr/bin/env python3
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
    plt.title("Cohen Sutherland Line Clipping")
    Xcoordinates.append(Xcoordinates[0])
    Ycoordinates.append(Ycoordinates[0])
    plt.plot(Xcoordinates, Ycoordinates, color='g')
    for i, j in zip(Xcoordinates, Ycoordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

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
    vx_min, vy_min, vx_max, vy_max = 1, 2, 9, 8
    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_max)

    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_max)


# Defining region codes
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


def compute_code(x, y):
    x_max = Xcoordinates[1]
    y_max = Ycoordinates[2]
    x_min = Xcoordinates[0]
    y_min = Ycoordinates[0]
    code = INSIDE
    if x < x_min:  # to the left of rectangle
        code |= LEFT
    elif x > x_max:  # to the right of rectangle
        code |= RIGHT
    if y < y_min:  # below the rectangle
        code |= BOTTOM
    elif y > y_max:  # above the rectangle
        code |= TOP
    return code


def cohen_sutherland(x1, y1, x2, y2):
    x_max = Xcoordinates[1]
    y_max = Ycoordinates[2]
    x_min = Xcoordinates[0]
    y_min = Ycoordinates[0]
    # Labelling
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    print(code1, code2)
    accept = False

    while True:

        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            xcut.append(x1)
            xcut.append(x2)
            ycut.append(y1)
            ycut.append(y2)
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:

            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

                # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1)
                x = x_min

            # Now intersection point x, y is found
            # We replace point outside clipping rectangle
            # by intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = compute_code(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = compute_code(x2, y2)

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        xcut.append(x1)
        xcut.append(x2)
        ycut.append(y1)
        ycut.append(y2)
        drawing()


    else:
        print("Line rejected")
        drawing()

#(1, 5),(4, 8)
#(2, 3),(2, 8)
#(0, 8),(4, 12)
#(1, 9),(3, 15)
#(5, 0),(5, 11)
#(6, 0),(10, 8)
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
        cohen_sutherland(x1, y1, x2, y2)


generate_viewport()
user_input()

