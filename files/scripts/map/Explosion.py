from pygame.image import load

explosions = []

class Explosion:

    def __init__(self, surface, x, y):
        self._load()

        self.__surface = surface
        self.x = x
        self.y = y

    
    def __load_sprites(self):
        self.__ex1 = load('files/textures/map/explosions/variant1/explosion1.png').convert_alpha()
        self.__ex2 = load('files/textures/map/explosions/variant1/explosion2.png').convert_alpha()
        self.__ex3 = load('files/textures/map/explosions/variant1/explosion3.png').convert_alpha()
        self.__ex4 = load('files/textures/map/explosions/variant1/explosion4.png').convert_alpha()
    
        self._sprite = self.__ex1

    def _load(self):
        self.__load_sprites()
        self.__get_start_config()


    def __get_start_config(self):
        
        self.__animate = True
        self._allTicksOnAnimate = 20
        self.__animate_counter = 0
        self.__per_change_sprite = self._allTicksOnAnimate // 4

    
    def __tick_explosion(self):

        self.__animate_counter += 1
        
        if self.__animate:

            if self.__animate_counter >= self._allTicksOnAnimate:
                self.__animate = False

            if self.__animate_counter in range(0, self.__per_change_sprite * 1 ):
                
                self._sprite = self.__ex1

            elif self.__animate_counter in range(self.__per_change_sprite * 1, self.__per_change_sprite * 2):
                
                self._sprite = self.__ex2

            elif self.__animate_counter in range(self.__per_change_sprite * 2, self.__per_change_sprite * 3):
                
                self._sprite = self.__ex3

            elif self.__animate_counter in range(self.__per_change_sprite * 3, self.__per_change_sprite * 4):
                
                self._sprite = self.__ex4        

        else:
            self.__delete()


    def __delete(self):
        global delete_explosion
        delete_explosion(self)


    def _draw(self):
        self.__surface.blit(self._sprite, (self.x, self.y))


    def update(self):
        self._draw()
        self.__tick_explosion()

def add(surface, x, y):
    explosions.append(Explosion(surface, x, y))

def update():
    for ex in explosions:
        ex.update()

def delete_explosion(explosion):
    del explosions[explosions.index(explosion)]