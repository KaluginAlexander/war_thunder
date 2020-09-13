class Background:

    def __init__(self, color, surface):

        self.__load()

        self.__color = color
        self.__surface = surface


    def __load(self):
        pass


    def _draw(self):
        self.__surface.fill(self.__color)


    def update(self):
        self._draw()


def get(color, surface):
    return Background(color, surface)