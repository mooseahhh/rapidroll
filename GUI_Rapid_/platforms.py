import pygame as pg
from pygame.sprite import Sprite





class Tile(Sprite):
    def __init__(self,ai_set,pos):
        # initialize and create surface and give it a rect
        super().__init__()
        self.width = ai_set.tile_w
        self.height = ai_set.tile_h
        self.image = pg.Surface([self.width,self.height])
        # blend to background (only useful when outlining rect)
        self.image.fill(ai_set.action_color)
        self.image.set_colorkey(ai_set.action_color)
        self.rect = self.image.get_rect(topleft = pos)
        # Draw rect onto image surface
        pg.draw.rect(self.image,ai_set.GREEN, [0,0,self.width,self.height])

    def gravity(self,ai_set):
        if self.rect.y >0 :
            self.rect.y -= ai_set.platform_gravity
        if self.rect.y-ai_set.platform_gravity < ai_set.action_y:
            self.kill()


class Spike(Sprite):
    def __init__(self,ai_set,pos):
        super().__init__()
        self.image =pg.Surface([ai_set.tile_w,ai_set.tile_h])
        self.image.fill(ai_set.action_color)
        self.image.set_colorkey(ai_set.action_color)
        self.width = ai_set.tile_w
        self.height = ai_set.tile_h
        self.rect = self.image.get_rect(topleft=pos)
        self.x = 0
        self.y = 5
        # spike tile coordinate
        pg.draw.polygon(self.image,ai_set.GRAY,
        [(self.x,self.y),
        (self.x,self.y+self.height),
        (self.x+self.width,self.y+self.height),
        (self.x+self.width,self.y),
        (self.x+(self.width-self.width/10),self.y-self.height/2),
        (self.x+(self.width-self.width/5),self.y),
        (self.x+(self.width-3*self.width/10),self.y-self.height/2),
        (self.x+(self.width-4*self.width/10),self.y),
        (self.x+(self.width-5*self.width/10),self.y-self.height/2),
        (self.x+(self.width-6*self.width/10),self.y),
        (self.x+(self.width-7*self.width/10),self.y-self.height/2),
        (self.x+(self.width-8*self.width/10),self.y),
        (self.x+(self.width-9*self.width/10),self.y-self.height/2),
        (self.x,self.y)])
    def gravity(self,ai_set):
        if self.rect.y >0 :
            self.rect.y -= ai_set.platform_gravity
        if self.rect.y-ai_set.platform_gravity < ai_set.action_y:
            self.kill()
    # def spike_collide(self,ball):
    #     collide = self.rect.colliderect(ball.rect)
    #     if collide:
    #         ball.kill()
# class Spike(pg.sprite.Sprite):
#     def __init__(self,screen,ai_set,pos):
#         # initialize and create surface and rect
#         super().__init__()
#         self.width = ai_set.tile_width
#         self.height = 20
#         self.image = pg.Surface([self.width,self.height])
#         self.image.fill(ai_set.LIGHT_BLUE)
#         self.image.set_colorkey(ai_set.LIGHT_BLUE)
#         self.rect = self.image.get_rect(topleft = pos)
#         self.screen_rect = screen.get_rect(center=ai_set.size)
#         # Draw spike shape onto rect surface
#         self.x = 0
#         self.y = 15
        
        # # spike tile coordinate
        # pg.draw.polygon(self.image,ai_set.GRAY,
        # [(self.x,self.y),
        # (self.x,self.y+self.height),
        # (self.x+self.width,self.y+self.height),
        # (self.x+self.width,self.y),
        # (self.x+(self.width-self.width/10),self.y-self.height/2),
        # (self.x+(self.width-self.width/5),self.y),
        # (self.x+(self.width-3*self.width/10),self.y-self.height/2),
        # (self.x+(self.width-4*self.width/10),self.y),
        # (self.x+(self.width-5*self.width/10),self.y-self.height/2),
        # (self.x+(self.width-6*self.width/10),self.y),
        # (self.x+(self.width-7*self.width/10),self.y-self.height/2),
        # (self.x+(self.width-8*self.width/10),self.y),
        # (self.x+(self.width-9*self.width/10),self.y-self.height/2),
        # (self.x,self.y)])
    
#         # (self.x+(self.width-11*self.width/10),self.y-self.height/2),
#         # (self.x+(self.width-12*self.width/10),self.y)

#         # pg.draw.rect(self.image,ai_set.WHITE,[0,0,self.width,self.height])
        
#     def gravity(self,ai_set):
#         if self.rect.y >0 :
#             self.rect.y -=ai_set.platform_gravity

    
class HeartTile(pg.sprite.Sprite):
    def __init__(self,ai_set,pos):
        super().__init__()
        self.image = pg.Surface([ai_set.heart_w,ai_set.heart_h])
        self.image.fill(ai_set.action_color)
        self.image.set_colorkey(ai_set.action_color)
        self.width = ai_set.heart_w
        self.height = ai_set.heart_h
        self.rect = self.image.get_rect(topleft=pos)
        pg.draw.polygon(self.image,(255,0,0), [(self.width/2,self.height),(self.width,self.height/2),(.75*self.width,0),(self.width/2,self.height/4),(self.width/4,0),(0,self.height/2)])
        # upside down heart  below
        # pg.draw.polygon(self.image,(255,0,0), [(self.width/2,0),(self.width,self.height/2),(.75*self.width,self.height),(self.width/2,self.height/2),(self.width/4,self.height),(0,self.height/2)])
    def gravity(self,ai_set):
        if self.rect.y >0 :
            self.rect.y -= ai_set.platform_gravity
        if self.rect.y-ai_set.platform_gravity < ai_set.action_y:
            self.kill()