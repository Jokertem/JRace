import pygame
from const import *
background_color = (128,128,128)
lines_color=(255,255,255)
lines_size = 10
def draw_car_park(screen):
    screen.fill(background_color) #Background
    pygame.draw.rect(screen,lines_color,pygame.Rect(0,0,screnn_size[0],lines_size)) #Top Line
    pygame.draw.rect(screen,lines_color,pygame.Rect(0,screnn_size[1]-lines_size,screnn_size[0],lines_size)) #Bottom Line
    pygame.draw.rect(screen,lines_color,pygame.Rect(0,0,lines_size,screnn_size[1])) #Left Line
    pygame.draw.rect(screen,lines_color,pygame.Rect(screnn_size[0]-lines_size,0,lines_size,screnn_size[1])) #Right Line

    