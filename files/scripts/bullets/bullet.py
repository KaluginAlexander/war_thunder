from pygame.image import load

bullets = []

class Bullet:

    def __init__(self, surface, shooter):

        self.__surface = surface
        self._shooter = shooter

        self.__load()


    def __load(self):
        self.__load_sprite()
        self.__get_start_config()


    def __get_start_config(self):

        self.x = self._shooter.x + self._shooter.width // 2
        

        if self._shooter.type == 'PLAYER':
            self._speed = -6
            self.__barrier = -20
            self.y = self._shooter.y

        else:
            self._speed = 6
            self.__barrier = self.__surface.get_height() + 20
            self.y = self._shooter.y + self._shooter.width

        self.damage = 25

    
    def _draw(self):
        self.__surface.blit(self._sprite, (self.x, self.y))


    def _check_barrier(self):

        if self._shooter.type == 'PLAYER':
            if self.y < self.__barrier:
                return False
            return True 

        else:
            if self.y > self.__barrier:
                return False
            return True 


    def __move(self):
        
        if self._check_barrier():
            self.y += self._speed

        else:
            self._delete()


    def _delete(self):
        global delete_bullet
        delete_bullet(self)


    def update(self):
        self._draw()
        self.__move()

    
    def __load_sprite(self):
        self.__bullet = load('files/textures/bullets/bullet.png')
        self._sprite = self.__bullet

        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()


def delete_bullet(bullet):
    del bullets[bullets.index(bullet)]


def add(surface, shooter):
    bullets.append(Bullet(surface, shooter))


def update():
    for bullet in bullets:
        bullet.update()