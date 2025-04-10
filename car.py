import pygame,os
from const import *
from random import randrange
class CarType:
     def __init__(self,name,w,h,texture,speed,acceleration,brakes):
          self.w=w
          self.h=h
          self.name=name
          self.texture=texture
          self.speed=speed
          self.acceleration=acceleration
          self.brakes=brakes
class Car(CarType):
    parked_cars =[]
    cars_types=[]
    cars_textures={}
    def __init__(self, name, w, h, texture, speed, acceleration, brakes,x,y):
         super().__init__(name, w, h, texture, speed, acceleration, brakes)
         self.x=x
         self.y=y

    @staticmethod
    def render_car_park_cars():
         Car.parked_cars.clear()
         parked_cars = 5
         cars_gap=180
         for i in range(5):
            car = Car.cars_types[randrange(len(Car.cars_types))]
            car_y =480
            if car.h > 164:
                 car_y = 350
            #Set car x position
            car_x =screnn_size[0]/2-car.w/2
            if i == 1:
                 car_x -= cars_gap
            elif i == 2:
                 car_x -= cars_gap *2
            elif i == 3:
                 car_x += cars_gap
            elif i == 4:
                 car_x += cars_gap *2          
            #Add Car
            Car.parked_cars.append(Car(car.name,car.w,car.h,car.texture,car.speed,car.acceleration,car.brakes,car_x,car_y))
    @staticmethod    
    def load():
            #Load textures
            for img in os.listdir("img/Cars"):
                 texture = pygame.image.load("img/Cars/"+img)
                 Car.cars_textures[img.replace(".png","")] = texture
            #Load car types     
            for car in Car.cars_textures.keys():
                 texture = Car.cars_textures[car]
                 if car =="Car_Ferrari_F40":
                      Car.cars_types.append(CarType("Ferrari F40",86,145,texture,110,24,12))
                 elif car == "Car_Audi_Sport_Quattro_Rally": 
                      Car.cars_types.append(CarType("Audi Quattro Rally",86,145,texture,110,24,12))  
                 elif car == "Car_BMW_M1": 
                      Car.cars_types.append(CarType("BMW M1",86,145,texture,110,24,12))
                 elif car == "Car_DeLorean_DMC": 
                      Car.cars_types.append(CarType("DeLorean",86,145,texture,110,24,12))
                 elif car == "Car_Audi_Sport_Quattro": 
                      Car.cars_types.append(CarType("Audi Quattro Sport",86,145,texture,110,24,12))                               
                 elif car == "Car_Plymouth_Hemi_Quada": 
                      Car.cars_types.append(CarType("Plymouth Quada",98,164,texture,110,24,12))                                  
                 elif car == "Car_Chevrolet_Camaro_ZL-1": 
                      Car.cars_types.append(CarType("Chevrolet Camaro",86,145,texture,110,24,12))                                   
                 elif car == "Car_Lancia_Delta_Integrale_Yellow": 
                      Car.cars_types.append(CarType("Lancia Integrale",86,145,texture,110,24,12))
                 elif car == "Car_Ford_GT40": 
                      Car.cars_types.append(CarType("Ford GT40",86,145,texture,110,24,12))
                 elif car == "Car_AM_General_Hummer": 
                      Car.cars_types.append(CarType("Hummer",98,164,texture,110,24,12))   
                 elif car == "Car_Lancia_Delta_Integrale_Police": 
                      Car.cars_types.append(CarType("Lancia Integrale Police",86,145,texture,110,24,12)) 
                 elif car == "Truck_A": 
                      Car.cars_types.append(CarType("Truck",139,353,texture,110,24,12))   
                 elif car == "Truck_B": 
                      Car.cars_types.append(CarType("Truck",139,353,texture,110,24,12))                                                             
                 
           