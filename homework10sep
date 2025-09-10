import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
while not done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            done = True
    pygame.draw.rect(screen, (250, 160, 0), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()