import pygame,sys
def set_events(player):
   events = pygame.event.get()
   for event in events:
    if event.type == pygame.KEYDOWN:
        #Exit Game
        if event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()
   keys = pygame.key.get_pressed()
   #Movement 
   #Move Right
   if keys[pygame.K_RIGHT]:
           player.x +=int(round(player.speed))
           player.direcion =2
   elif keys[pygame.K_d]:
           player.x +=int(round(player.speed))
           player.direcion =2
   #Move Left
   elif keys[pygame.K_LEFT]:
           player.x -=int(round(player.speed))
           player.direcion =1
   elif keys[pygame.K_a]:
           player.x -=int(round(player.speed)) 
           player.direcion =1    
    #Move Up           
   elif keys[pygame.K_UP]:
           player.y -=int(round(player.speed))
           player.direcion =3
   elif keys[pygame.K_w]:
           player.y -=int(round(player.speed))
           player.direcion =3  
    #Move Down              
   elif keys[pygame.K_DOWN]:
           player.y +=int(round(player.speed))
           player.direcion =0        
   elif keys[pygame.K_s]:
           player.y +=int(round(player.speed))   
           player.direcion =0         
       