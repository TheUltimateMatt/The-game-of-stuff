import pygame
pygame.init()

background = pygame.image.load("assets/bg.jpg")


pygame.display.set_caption("The game of stuff")
pygame.display.set_mode((1064, 640))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()




