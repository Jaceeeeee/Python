import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Choose Your Own Adventure - The Great Jungle!')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #draw all our elements
    print("Hello, World!")
    pygame.display.update()
    clock.tick(60)
