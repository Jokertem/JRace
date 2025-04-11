import pygame,sys
def walk(player,key):
         if key=="Right":
                player.x +=int(round(player.speed))
                player.direcion =2
         elif key =="Left":
                player.x -=int(round(player.speed))
                player.direcion =1
         elif key =="Up":
                  player.y -=int(round(player.speed))
                  player.direcion =3
         elif key =="Down":
                  player.y +=int(round(player.speed))
                  player.direcion =0          
                        
                      
def set_events(player):
   events = pygame.event.get()
   for event in events:
    if event.type == pygame.KEYDOWN:
        #Exit Game
        if event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()
        elif event.key == pygame.K_f:
           if player.car and player.place=="car_park":
                 player.speed=5
                 player.car =None
                 print("Leave Car")
   keys = pygame.key.get_pressed()
   #Movement 
   #Move Right
   if keys[pygame.K_RIGHT]:
           if not player.car:
               walk(player,"Right") 
               
   elif keys[pygame.K_d]:
           if not player.car:
               walk(player,"Right")  
               
   #Move Left
   elif keys[pygame.K_LEFT]:
         if not player.car:
                walk(player,"Left")  
               
   elif keys[pygame.K_a]:
           if not player.car:
                 walk(player,"Left") 
               
    #Move Up           
   elif keys[pygame.K_UP]:
           if not player.car:
               walk(player,"Up")
   elif keys[pygame.K_w]:
            if not player.car:
                walk(player,"Up")
    #Move Down              
   elif keys[pygame.K_DOWN]:
          if not player.car:
               walk(player,"Down")
   elif keys[pygame.K_s]:
           if not player.car:
                walk(player,"Down")          
       
   
             