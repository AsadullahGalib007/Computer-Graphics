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

# for storing points
xcut = []
ycut = []


def drawing():
    # The plot draws line form a point to another,
    # In order to complete the polygon the first coordinate need to append again
    # green is the viewport
    plt.title("Window to Viewport Mapping")
    Xcoordinates.append(Xcoordinates[0])
    Ycoordinates.append(Ycoordinates[0])
    plt.plot(Xcoordinates, Ycoordinates, color='g')
    for i, j in zip(Xcoordinates, Ycoordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

    # cyan is the window
    x1coordinates.append(x1coordinates[0])
    y1coordinates.append(y1coordinates[0])
    plt.plot(x1coordinates, y1coordinates, color='c')
    for i, j in zip(x1coordinates, y1coordinates):
        plt.text(i, j, '({}, {})'.format(i, j))

    for i, j in zip(xcut, ycut):
        plt.text(i, j, '({}, {})'.format(i, j))
    plt.scatter(xcut, ycut, color = 'r')

    plt.show()


vx_min, vy_min, vx_max, vy_max = 30, 40, 60, 60
vx, vy = 0, 0

wx_min, wy_min, wx_max, wy_max = 20, 40, 80, 80
wx, wy = 30, 70

def mapping():
    sx = (vx_max - vx_min) / (wx_max - wx_min)
    sy = (vy_max - vy_min) / (wy_max - wy_min)

    # calculating the point on viewport
    vx = vx_min + ((wx - wx_min) * sx)
    vy = vy_min + ((wy - wy_min) * sy)
    print(vx, vy)

    xcut.append(wx)
    ycut.append(wy)

    xcut.append(vx)
    ycut.append(vy)
    drawing()


def generate_viewport():
    # Generating viewport
    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_min)

    Xcoordinates.append(vx_max)
    Ycoordinates.append(vy_max)

    Xcoordinates.append(vx_min)
    Ycoordinates.append(vy_max)

    # Generating window
    x1coordinates.append(wx_min)
    y1coordinates.append(wy_min)

    x1coordinates.append(wx_max)
    y1coordinates.append(wy_min)

    x1coordinates.append(wx_max)
    y1coordinates.append(wy_max)

    x1coordinates.append(wx_min)
    y1coordinates.append(wy_max)


generate_viewport()
mapping()
