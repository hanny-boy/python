import pygame
import random

pygame.init()

# Custom Events
spritecolourchangeevent = pygame.USEREVENT + 1
backgroundcolourevent = pygame.USEREVENT + 2

# Colours
BLUE = pygame.Color('blue')
RED = pygame.Color('red')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
YELLOW = pygame.Color('yellow')
WHITE = pygame.Color('white')

# Sprite Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        # Bounce horizontally
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        # Bounce vertically
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(spritecolourchangeevent))
            pygame.event.post(pygame.event.Event(backgroundcolourevent))

    def change_colour(self):
        self.image.fill(random.choice([BLUE, RED, LIGHTBLUE, DARKBLUE, MAGENTA, ORANGE, YELLOW, WHITE]))

    @staticmethod
    def change_background_colour():
        global bg_colour
        bg_colour = random.choice([BLUE, RED, LIGHTBLUE, DARKBLUE, MAGENTA, ORANGE, YELLOW, WHITE])


# Setup
all_Sprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 570)
all_Sprites.add(sp1)

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Sprite Colour Change')

bg_colour = BLUE
clock = pygame.time.Clock()
running = True

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spritecolourchangeevent:
            sp1.change_colour()
        elif event.type == backgroundcolourevent:
            Sprite.change_background_colour()

    all_Sprites.update()
    screen.fill(bg_colour)
    all_Sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
