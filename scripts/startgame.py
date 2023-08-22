import pygame
from scripts.settings import *
from scripts.scene import Scene
from scripts.menu import Menu

class StartGame:

    def __init__(self):
        # padrão iniciar font, sound, video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        self.scene = "menu"
        self.current_scene = Menu()

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.current_scene.events(event)

            self.display.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()
