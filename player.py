import pygame
from car import Car
from const import *

last_update = pygame.time.get_ticks()
animation_cooldown =75
frame=0
def get_image(sheet,w,h,frame_w,frame_h):
    #Load Sprite Frame
    image = pygame.Surface((w,h))
    image.blit(sheet,(0,0),((w*frame_w,h*frame_h,w,h)))
    image.set_colorkey((0,0,0))
    return image
class Player(pygame.Rect):
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=5
        self.acceleration=None
        self.brakes=None
        self.place = "car_park"
        self.car=None
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown =175
        self.frame=0
        self.direcion =0
        self.frames = [5,4,3]

    def colisons(self):
        #Colisons With Borders
        if (self.x <=0): #Left Border
            self.x =0    
        if (self.x+self.w >= screnn_size[0]): #Right Border
            self.x = screnn_size[0] - self.w  
        if (self.y <=0): #Top Border
            self.y =0    
        if (self.y+self.h >= screnn_size[1]): #Bottom Border
            self.y = screnn_size[1] - self.h

        #Colisons With Parked Cars 
        if self.place =="car_park":
            for car in Car.parked_cars:
                if self.colliderect(car):
                    self.car = car.name
                    self.speed= car.speed
                    self.acceleration=car.acceleration
                    self.brakes=car.brakes
                    self.x = car.x -25
                    self.y = car.y+car.h/2-self.h/2

                  
       
    def animation(self,screen,sprite):
         curent_time = pygame.time.get_ticks()
         if curent_time - self.last_update >=self.animation_cooldown:
                self.frame+=1
                self.last_update = curent_time
                if self.frame >= len(self.frames):
                    self.frame=0
         screen.blit(get_image(sprite,32,32,self.frames[self.frame],self.direcion),(self.x,self.y))     