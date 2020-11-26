from UI.Window import Window


class PolygonApplication:
    def __init__(self):
        self.window = Window("Détermination des périmètre, surface et centre de gravité d'un polygone")
        self.window.addMouseClickListener(self.window.onClick)

    def start(self):
        self.window.show()
