import pygame
from const import *
def show_car_name(screen,player):
    font = pygame.font.SysFont('Arial', 26)

    if player.car and player.place=="car_park":
        text = font.render("Enter to Start",False,(124,252,0))
        text_rect = text.get_rect(center=(screnn_size[0]/2, screnn_size[1]/2-25))
        screen.blit(text, text_rect)
        text2 = font.render("F to Leave the car ",False,(124,252,0))
        text_rect2 = text2.get_rect(center=(screnn_size[0]/2, screnn_size[1]/2+25))
        screen.blit(text2, text_rect2)

    if player.car:
        text = font.render(player.car,False,(124,252,0))
        screen.blit(text,(250,screnn_size[1]-150))    
