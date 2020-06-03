from graphics import *
from text import DrawText

# window
win = GraphWin("MouseTracker", 600, 600, autoflush=False)
win.setBackground("black")

# initial declarations
coord = 0
xcoord = 0
ycoord = 0

switch = True
dis_switch = True

color = color_rgb(44, 255, 79)

xlist = []
ylist = []
xclist = []
yclist = []

# display x and y:
xSign = DrawText(10, 10, "X:", 12, "white")
xSign.draw(win)
ySign = DrawText(10, 30, "Y:", 12, "white")
ySign.draw(win)

# code
while True:

    # get coordinates
    coord = win.getMouse()
    xcoord = coord.getX()
    ycoord = coord.getY()
    xlist.append(xcoord)
    ylist.append(ycoord)

    # display coordinates
    if dis_switch is False:
        xclist[0].undraw()
        xclist.pop(0)
        yclist[0].undraw()
        yclist.pop(0)

    display_x = Text(Point(35, 10), f'{xcoord}')
    display_y = Text(Point(35, 30), f'{ycoord}')
    display_x.setTextColor("white")
    display_y.setTextColor("white")

    display_x.draw(win)
    display_y.draw(win)

    xclist.append(display_x)
    yclist.append(display_y)

    dis_switch = False

    # display lines
    if switch is True:
        lineV = Line(Point(xcoord, 0), Point(xcoord, 600))
        lineH = Line(Point(0, ycoord), Point(600, ycoord))

        lineV.setFill(color)
        lineH.setFill(color)

        lineV.draw(win)
        lineH.draw(win)

        switch = False
    else:
        # calculate distance and remove
        distX = (xlist[1] - xlist[0])
        distY = (ylist[1] - ylist[0])

        xlist.pop(0)
        ylist.pop(0)

        lineV.move(distX, 0)
        lineH.move(0, distY)

    update()

# -------------#
win.getMouse()
win.close()
