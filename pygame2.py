import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")
screen.fill((0,0,0))
pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)
pygame.draw.circle(screen, (255, 0, 0), (200, 150), 3)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
    pygame.display.flip()
pygame.quit()