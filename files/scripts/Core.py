import pygame
import files.scripts.map.Background as Background
import files.scripts.player.Player as Player
import files.scripts.bullets.bullet as Bullets
import files.scripts.enemy.Enemy as Enemys
import files.scripts.map.Explosion as Explosion
import files.scripts.bonus.protect_bonus as PBonus
from files.scripts.interfaces.Protect import Protect
from files.scripts.interfaces.Health import Health

pygame.init()

class Core:

    def __init__(self):

        self.__start()

    def __start(self):
        
        self.screen = pygame.display.set_mode((750, 750))

        self.bg = Background.get(color = (117, 187, 253), surface = self.screen)
        Player._init(self.screen)
        
        self.pInterface = Protect(self.screen)
        self.hInterface = Health(self.screen)
        self.game = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

        while self.game:

            # place for update
            self.bg.update()
            Player.update()
            Bullets.update()
            Enemys.update(self.screen)
            Explosion.update()
            PBonus.update()

            try:
                self.pInterface.update(Player.player)
                self.hInterface.update(Player.player)
            except:
                pass

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game = False
                    exit()
            
            pygame.display.update()
            self.clock.tick(self.FPS)

def start():
    Main = Core()