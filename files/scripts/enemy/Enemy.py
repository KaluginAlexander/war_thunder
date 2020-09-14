from pygame.image import load
import files.scripts.bullets.bullet as Bullet 
import random
import files.scripts.map.Explosion as Explosion

enemys = []

surface = None

counter = 0
delay = 120

class Enemy:

    def __init__(self, surface):

        self.__surface = surface
        self.__load()

    def __load(self):
        self.__load_sprite()
        self.__get_start_config()


    def __get_start_config(self):

        self._surface_width = self.__surface.get_width()
        self._surface_center_x = self._surface_width // 2

        self._surface_height = self.__surface.get_height()
        self._surface_center_y = self._surface_height // 2

        self.x = random.randint(0, self._surface_width // 10) * 10  
        self.y = -10

        self.__steps_for_animate = 100

        self._x_step_size = 0
        self._y_step_size = 0
        self._steps_footed = 0
        self._Random_Place_Animate = False

        self._max_allowed_Y = self._surface_center_y - self.height
        self._max_allowed_X = self._surface_width

        self.type = 'ENEMY'

        self.__cooldown_counter = 0
        self.__cooldown_ticks = 120


    def __set_cooldown(self):

        self.__cooldown_counter = self.__cooldown_ticks


    def __cooldown_delay(self):

        if self.__cooldown_counter > 0:
            self.__cooldown_counter -= 1
            
        else:
            self._shoot()
            self.__set_cooldown()

    
    def _shoot(self):
        Bullet.add(self.__surface, self)

    
    def __load_sprite(self):
        self._default = load('files/textures/enemy/enemy.png').convert_alpha()
        self._sprite = self._default

        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()
        
    
    def _go_to_random_place(self):

        if self._Random_Place_Animate:

            if self._steps_footed <= self.__steps_for_animate:

                self.x += self._x_step_size
                self.y += self._y_step_size

                self._steps_footed += 1

            else:

                self._Random_Place_Animate = False

        else:
            self._Random_Place_Animate = True

            self._x_step_size = (random.randint(0, self._max_allowed_X) - self.x) // self.__steps_for_animate
            self._y_step_size = (random.randint(0, self._max_allowed_Y) - self.y) // self.__steps_for_animate

            self._steps_footed = 0
        


    def _draw(self):
        self.__surface.blit(self._sprite, (self.x, self.y))


    def update(self):
        self._draw()
        self._go_to_random_place()
        self.__cooldown_delay()

    
    def __delete(self):
        global delete_enemy
        delete_enemy(self)


    def _die(self):
        Explosion.add(self.__surface, self.x, self.y)
        self.__delete()

def delete_enemy(enemy):
    del enemys[enemys.index(enemy)]


def add(surface):
    enemys.append(Enemy(surface))


def update(surf):

    global surface

    surface = surf

    counter_for_add_planes()
    check_collide()

    for enemy in enemys:
        enemy.update()
        

def counter_for_add_planes():

    global counter

    if counter < 1:

        global surface

        add(surface)

        counter = delay

    counter -= 1


def delete_enemy(en):
    del enemys[enemys.index(en)]

def check_collide():

    global enemys

    for en in enemys:

        bullets = Bullet.bullets

        for bullet in bullets:

            if bullet._shooter.type == 'PLAYER':
                
                if bullet.x in range(en.x, en.x + en.width) and bullet.y in range(en.y + en.height):

                    try:
                        en._die()
                        bullet._delete()
                    except:
                        pass