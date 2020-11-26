from tkinter import *

from model.Point import Point
from model.Polygone import Polygon

class Window:
    # Constructeur (bon y'a mieux a faire que de mettre en attribut tous les composants
    # graphiques (idealement que window et accéder aux sous composants par là genre
    # window.getChild(canvas) mais je sais pas trop comment faire et j'ai la flemme de chercher)
    def __init__(self, title):
        self.window = Tk()
        self.window.title = title
        self.canvas = Canvas(self.window, bg='lightgrey', height=600, width=1280)
        self.canvas.create_rectangle(0, 0, 2, 2, width=2, fill='red')
        self.canvas.pack(side=TOP)
        self.labelCoord = Label(self.window)
        self.labelCoord.pack(side=BOTTOM)
        self.labelPerimeter = Label(self.window)
        self.labelPerimeter.pack(side=BOTTOM)
        self.labelSurface = Label(self.window)
        self.labelSurface.pack(side=BOTTOM)
        self.labelCenterOfGravity = Label(self.window)
        self.labelCenterOfGravity.pack(side=BOTTOM)
        # Our polygon to study
        self.polygon = Polygon()

    # Tk Mainloop
    def show(self):
        self.canvas.mainloop()
        self.canvas.destroy()

    def onClick(self, event):
        self.polygon.addSummit(Point(event.x, event.y))
        self.redraw()

    def redraw(self):
        self.drawPolygon()
        self.showPolygonInformation()

    def addMouseClickListener(self, functionToCallOnClick):
        self.canvas.bind("<Button-1>", functionToCallOnClick)

    def showPolygonInformation(self):
        # Put here polygon information to UI
        self.labelCoord.configure(text="Coordonnées : " + str(self.polygon.getCoordonnees()))
        self.labelPerimeter.configure(text="Périmètre : " + str(self.polygon.getPerimeter()))
        self.labelSurface.configure(text="Surface : " + str(self.polygon.getSurface()))
        self.labelCenterOfGravity.configure(text="Centre de gravité : " + str(self.polygon.getCenterOfGravity()))
        print(self.polygon)

    # Draw polygon with points
    def drawPolygon(self):
        self.canvas.delete("all")
        nbSummits=len(self.polygon.points)
        i = 0

        if (nbSummits>1) :
            while (i<nbSummits-1) :
                p1 = self.polygon.points[i]
                p2 = self.polygon.points[i+1]
                self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="midnightblue")
                i = i+1

            self.canvas.create_line(self.polygon.points[0].x, self.polygon.points[0].y,
                                    self.polygon.points[nbSummits-1].x, self.polygon.points[nbSummits-1].y,
                                    fill="midnightblue")
