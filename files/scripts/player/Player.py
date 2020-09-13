from pygame.image import load
from pygame.key import get_pressed
from pygame import K_w, K_a, K_s, K_d, K_SPACE
import files.scripts.bullets.bullet as Bullet 

class Player:

    def __init__(self, surface):

        self.__surface = surface
        self.__load()


    def __load(self):

        self.__load_sprite()
        self.__get_start_config()


    def __load_sprite(self):
        self.__default = load('files/textures/players/player.png').convert_alpha()
        self._sprite = self.__default

        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()

    
    def __get_start_config(self):

        self._surface_width = self.__surface.get_width()
        self._surface_center_x = self._surface_width // 2

        self._surface_height = self.__surface.get_height()
        self._surface_center_y = self._surface_height // 2

        self.x = self._surface_center_x - self.width // 2 
        self.y = self._surface_center_y - self.height // 2 

        self._speedOther = 3
        self._speedUp = 5

        self.type = 'PLAYER'

        self.__cooldown = False
        self.__cooldown_counter = 0 
        self.__cooldown_ticks = 10
    
    def _draw(self):
        self.__surface.blit(self._sprite, (self.x, self.y))


    def _cooldown_check(self):
        
        if not self.__cooldown:
            self._shoot()
            self.__set_cooldown()

    def __set_cooldown(self):

        self.__cooldown = True
        self.__cooldown_counter = self.__cooldown_ticks


    def __cooldown_delay(self):

        if self.__cooldown:

            if self.__cooldown_counter > 0:
                self.__cooldown_counter -= 1
            
            else:
                self.__cooldown = False


    def _check_left_border(self):

        if self.x < 0:
            return False

        return True

    
    def _check_right_border(self):

        if self.x > self._surface_width - self.width:
            return False

        return True

    
    def _check_up_border(self):

        if self.y < 0:
            return False

        return True

    
    def _check_down_border(self):

        if self.y > self._surface_height - self.height:
            return False

        return True

    def update(self):

        self.__check_keys()
        self.__cooldown_delay()
        self._draw()


    def __check_keys(self):
        
        keys = get_pressed()

        if keys[K_w] and self._check_up_border():
            self._go_to_up()

        if keys[K_a] and self._check_left_border():
            self._go_to_left()

        if keys[K_s] and self._check_down_border():
            self._go_to_down()

        if keys[K_d] and self._check_right_border():
            self._go_to_right()

        if keys[K_SPACE]:
            self._cooldown_check()

    
    def _shoot(self):
        Bullet.add(self.__surface, self)


    def _go_to_left(self):
        self.x -= self._speedOther


    def _go_to_right(self):
        self.x += self._speedOther


    def _go_to_down(self):
        self.y += self._speedOther


    def _go_to_up(self):
        self.y -= self._speedUp


def get(surface):
    return Player(surface = surface)