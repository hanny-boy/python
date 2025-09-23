import pygame
import random
width,height = 500,700
speed = 5
size = 72
pygame.init()
bimage = pygame.transform.scale(pygame.image.load("https://www.istockphoto.com/illustrations/video-game-background"),(width,height))
class sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color)