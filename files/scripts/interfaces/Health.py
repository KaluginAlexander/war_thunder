from pygame.font import Font
from pygame.image import load

class Health:

    def __init__(self, surface):
        self.__surface = surface
        self.__load()


    def __load(self):
        self.__load_icon()
        self.__make_font()
        self.__get_start_config()

    
    def __load_icon(self):

        self._sprite = load('files/textures/icons/health.png').convert_alpha() 

        self.icon_width = self._sprite.get_width()
        self.icon_height = self._sprite.get_height()


    def __make_font(self):
        self.font = Font('files/textures/fonts/pixel.ttf', self.icon_height)


    def __get_start_config(self):

        self._surface_width = self.__surface.get_width()
        self._surface_height = self.__surface.get_height()

        self.margin = 10

        self._icon_x = self.margin
        self._icon_y = self._surface_height - self.margin - self.icon_height - self.margin - self.icon_width

        self._font_x = self._icon_x + self.icon_width + self.margin
        self._font_y = self._icon_y


    def __print_text(self, player):
        
        health = player.health

        points_for_interface = self.font.render(f"{health}", 1, (255, 255, 255))

        self.__surface.blit(points_for_interface, (self._font_x, self._font_y))


    def _draw_icon(self):
        self.__surface.blit(self._sprite, (self._icon_x, self._icon_y))


    def _draw(self, player):
        self.__print_text(player)
        self._draw_icon()


    def update(self, player):
        self._draw(player)