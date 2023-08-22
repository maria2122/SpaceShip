import pygame

class Scene:
    def __init__(self):
        pygame.display.set_caption("NomeScene")
        self.display = pygame.display.get_surface()
        # um tipo de array com o grupo de objetos
        self.all_sprites = pygame.sprite.Group()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.all_sprites.update()