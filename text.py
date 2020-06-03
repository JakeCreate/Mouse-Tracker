from graphics import *


class DrawText:
    def __init__(self, xcord, ycord, String, size, colorString):

        self.text = String
        self.size = size
        self.color = colorString
        self.xcord = xcord
        self.ycord = ycord

    def draw(self, window):
        hello = Text(Point(self.xcord, self.ycord), self.text)
        hello.setTextColor(self.color)
        hello.setSize(self.size)
        hello.draw(window)

