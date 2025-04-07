import pygame,sys
from const import *
from event import set_events
from car_park import draw_car_park
from player import Player
def get_image(sheet,w,h):
    #Load Sprite Frame
    image = pygame.Surface((w,h))
    image.blit(sheet,(0,0),((w*5,0,w,h)))
    image.set_colorkey((0,0,0))
    return image
class Game():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((screnn_size),pygame.FULLSCREEN)
        self.clock=pygame.time.Clock()
        self.delta=1
        self.player=Player(screnn_size[0]/2,80,24,24)
        self.textures={}
        self.textures["player"] = pygame.image.load("img/Player/Player.png").convert_alpha()
        
        #Load Images 

        self.game()
    def game(self):
        while True:
            self.delta = self.clock.tick(frame_rate) * frame_rate/2
            pygame.display.update()
            set_events(self.player)
            draw_car_park(self.screen)
            self.screen.blit(get_image(self.textures["player"],32,32),(self.player.x,self.player.y))
            
            

Game()        