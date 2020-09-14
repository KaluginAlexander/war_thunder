from pygame.image import load 

bonuses = []

class Protect_bonus:

    def __init__(self, surface, x, y):
        
        self.__surface = surface
        self.x = x
        self.y = y
        self.__load()


    def __load(self):
        self.__load_sprite()
        self.__get_start_config()

    
    def __load_sprite(self):
        self.__bonus = load('files/textures/icons/protect.png').convert_alpha()
        self._sprite = self.__bonus

        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()

    
    def allow(self):
            
        global delete_bonus

        delete_bonus(self)


    def __get_start_config(self):

        pass
    

    def _draw(self):
        
        self.__surface.blit(self._sprite, (self.x, self.y))


    def update(self):

        self._draw()

def add(sc, x , y):

    global bonuses

    bonuses.append(Protect_bonus(sc, x, y))


def delete_bonus(bonus):

    global bonuses

    del bonuses[bonuses.index(bonus)]


def update():

    global bonuses

    for bonus in bonuses:

        bonus.update()