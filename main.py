import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


background = pygame.image.load("assets/bg.jpg")


pygame.display.set_caption("The game of stuff")
screen = pygame.display.set_mode((1024, 720))

running = True

while running:
    screen.blit(background, (0, -200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
