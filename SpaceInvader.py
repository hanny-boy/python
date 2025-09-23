import pygame
import math
import random
screenwidth = 800
screenheight = 500
playerstartx = 370
playerstarty = 380
enemystartymin = 50
enemystartymax = 150
enemyspeedx = 4
enemyspeedy = 40
bulletspeedy = 10
collisiondistance = 27
pygame.init()
screen = pygame.display.set_mode((screenwidth, screenheight))
background = pygame.image.load()
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("")
pygame.display.set_icon(icon)
playerimage = pygame.image.load()
playerx = playerstartx
playery = playerstarty
playerxchange = 0
enemyimage = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []