import pygame
from const import *
from event import set_events
from car_park import draw_car_park
from player import Player
from car import Car

class Game():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((screnn_size),pygame.FULLSCREEN)
        self.clock=pygame.time.Clock()
        self.delta=1
        self.player=Player(screnn_size[0]/2-32/2,80,24,24)
        Car.load()
        Car.render_car_park_cars()
        #Load Images 
        self.textures={}
        self.textures["player"] = pygame.image.load("img/Player/Player.png").convert_alpha()
        
        self.game()
    def game(self):
        while True:
            self.delta=self.clock.tick(frame_rate) * frame_rate/1000
            pygame.display.update()
            set_events(self.player)
            if self.player.place =="car_park":
                draw_car_park(self.screen)
                self.player.animation(self.screen,self.textures["player"])
                self.player.colisons()
            
            

Game()        