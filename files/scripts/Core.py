import pygame
import files.scripts.map.Background as Background

pygame.init()

class Core:

    def __init__(self):

        self.__start()

    def __start(self):
        
        self.screen = pygame.display.set_mode((750, 750))

        self.bg = Background.get(color = (255, 255, 255), surface = self.screen)

        self.game = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

        while self.game:

            # place for update
            self.bg.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game = False
                    exit()
            
            pygame.display.update()
            self.clock.tick(self.FPS)

def start():
    Main = Core()