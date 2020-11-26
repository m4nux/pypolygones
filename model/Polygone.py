from model.Point import Point


class Polygon:
    # Constructeur du polygone avec une liste de points
    def __init__(self, *listOfPoints):
        self.points = list()
        for p in listOfPoints:
            self.points.append(p)

    # Representation de l'objet human readable (toString)
    def __repr__(self):
        return 'Polygon(' + ', '.join(map(lambda p: str(p), self.points)) + ')'

    # Ajouter un commet au polygone
    def addSummit(self, point):
        # Add x,y points to our polygon
        print("addSummit : " + str(point))
        self.points.append(point)

    def getSurface(self):
        # TODO Calculate polygon surface
        return 0

    def getPerimeter(self):
        # TODO Calculate polygon perimeter
        return 0

    def getCenterOfGravity(self):
        # TODO Calculate polygon center of gravity
        return Point(0, 0)

    def getCoordonnees(self):
        # TODO Calculate polygon coordonnee
        return Point(0, 0)
