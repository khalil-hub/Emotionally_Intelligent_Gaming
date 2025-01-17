import pygame
import sys
#initialize pygame
pygame.init()
#screen dimensions
WIDTH, HEIGHT=800, 600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

#colors
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

#Game clock
clock=pygame.time.Clock()

#Player settings
player=pygame.Rect(100, 500, 50, 50)
player_speed=5
gravity=1
velocity_y=0
on_ground=False

#platform
platform=pygame.Rect(100, 550, 200, 20)