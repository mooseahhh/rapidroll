import pygame as pg
from pygame.sprite import Sprite, collide_rect, spritecollide




class Player(Sprite):
    def __init__(self,ai_set):
        super().__init__()
        # self.space=action_s.image
        self.falling = True
        self.moving_right= False
        self.moving_left = False
        self.image=pg.Surface([ai_set.ball_w,ai_set.ball_h])
        self.image.fill(ai_set.action_color)
        self.image.set_colorkey(ai_set.action_color)
        self.rect = self.image.get_rect(center=ai_set.ball_pos)
        pg.draw.circle(self.image,ai_set.RED,(10,10),ai_set.ball_rad)
        self.vel_y = 0
        self.score = 0
        self.lives = 3
        self.bad_collide = False
        self.collideRect =  pg.rect.Rect((4, 0), (10,20))
        self.collideRect.midbottom = self.rect.midbottom
        # pg.draw.rect(self.image,ai_set.CRIMSON_RED,(4,0,10,20),2)
        self.speed_flag =100

        
 
            
        
        
    def move(self,ai_set):
        dx=0
        dy=0
        if self.moving_right and self.rect.x <ai_set.action_w-18:
            self.rect.x += ai_set.ball_speed
        if self.moving_left and self.rect.x > ai_set.action_x:
            self.rect.x -= ai_set.ball_speed

        if self.vel_y<5:
            self.vel_y += ai_set.GRAVITY
        dy+=self.vel_y
        if self.rect.bottom + dy > ai_set.action_h:
            dy = ai_set.action_h - self.rect.bottom
            self.falling = False
            
        self.rect.y += dy
        if self.falling:
            self.score+=1
        if self.rect.bottom >  ai_set.action_h-10:
            self.bad_collide = True
        if self.rect.top < ai_set.data_h + 10:
            self.bad_collide = True
        
    def tile_collide(self,ai_set,tiles):
        #need collide var to reference when collision isn't occuring
        collide = pg.sprite.spritecollide(self, tiles, False)
        for t in collide:
            self.rect.bottom = t.rect.top + 5
            self.rect.y -=  (ai_set.platform_gravity)
            self.falling = False
        if not collide:
            self.falling  = True
    def heart_collide(self,ai_set,heart):
        collide = self.rect.colliderect(heart.rect)
        if collide:
            heart.kill()
            self.lives+=1
          
    
    def spike_collide(self,spikes):
        collide = pg.sprite.spritecollide(self,spikes,False)
        if collide:
            self.bad_collide = True
           

            


        '''
        		#apply gravity
		self.vel_y += GRAVITY
		if self.vel_y > 10:
			self.vel_y
		dy += self.vel_y

		#check collision with floor
		if self.rect.bottom + dy > 300:
			dy = 300 - self.rect.bottom
			self.in_air = False

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy
        '''


        











# class Player(game.sprite.Sprite):
#     def __init__(self,ai_set,width,height,radius,pos):
#         super().__init__()
      
#         self.ai_set = ai_set
#         self.moving_right = False
#         self.moving_left = False
#         self.on_tile = False
#         self.falling = False
#         self.score = 0
#         self.image = game.Surface([width,height])
#         self.image.fill(ai_set.LIGHT_BLUE)
#         self.image.set_colorkey(ai_set.LIGHT_BLUE)
#         self.radius = radius
#         self.width = width
#         self.height = height
#         self.rect = self.image.get_rect(center = pos)
#         self.speed_x = 5
#         game.draw.circle(self.image, ai_set.RED, pos, self.radius)
#         self.GRAVITY = ai_set.GRAVITY
#     def update(self):
#         if self.moving_right and self.rect.x < self.ai_set.width-self.width:
#             self.rect.x += self.speed_x
#         if self.moving_left and self.rect.x > 0:
#             self.rect.x -= self.speed_x
#     def gravity(self):
#         if self.on_tile == False:    
#             if self.rect.y< self.ai_set.height - self.height:
#                 self.rect.y += self.GRAVITY
#                 self.falling = True
#         else:
#             self.falling= False
            
#     def tile_colision(self,ai_set,tiles):
#         for p in game.sprite.spritecollide(self, tiles, False):
#             if not self.on_tile:
#                 self.rect.bottom = p.rect.top
#                 self.rect.y += - (ai_set.platform_gravity)
#                 self.on_tile = True
#             self.on_tile = False
#     def scored(self,ai_set):
        
#         if self.falling==True:
#             self.score+=1 
#         elif self.falling == False:
#             self.score= self.score
#         return int(self.score/10),self.falling


