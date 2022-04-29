
import pygame as pg
from settings import Settings

from pygame.sprite import Group,Sprite


# this class is the surface with the player's score and lives
class DataScreen(Sprite):
    def __init__(self,ai_set):
        super().__init__()
        self.width = ai_set.data_w
        self.height = ai_set.data_h
        self.image = pg.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, ai_set.BLACK, [0,0, self.width,self.height])
        pg.draw.rect(self.image, ai_set.data_color, [0,0, self.width,self.height],5)
 




# this class is the surface that will have the gameplay
class ActionScreen(Sprite):
    def __init__(self,ai_set):
        super().__init__()
        self.width = ai_set.action_w
        self.height = ai_set.action_h
        self.x = ai_set.action_x
        self.y = ai_set.action_y
        self.image = pg.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, ai_set.action_color, [self.x,self.y, self.width,self.height])



# W H   X  Y
# 27 30 0 150

class Brick(Sprite):
    def __init__(self,ai_set,x,y):
        super().__init__()
        self.width= ai_set.action_x
        self.height= ai_set.brick_fill_h #int(ai_set.screen_h)
        self.x = x
        self.y = y
        self.image = pg.Surface([self.width,self.height])
        self.image.set_colorkey(ai_set.BLACK)
        self.rect = self.image.get_rect(topleft=(x,y))
        pg.draw.rect(self.image,ai_set.brick_inside_color, [0,0,self.width,self.height])
        # print(f'({self.rect.x},{self.rect.y}) data_h={ai_set.data_h}')
       
    def brick_col(self,ai_set,x):
        for b in range(ai_set.num_of_bricks): #int(self.height/ai_set.num_of_bricks
            pg.draw.rect(self.image,ai_set.brick_color,[x,0+ai_set.brick_h*b,ai_set.brick_w,ai_set.brick_h],3)

# 
class HeartIcon(Sprite):
    def __init__(self,ai_set,pos):
        super().__init__()
        self.image = pg.Surface([ai_set.heart_icon_w,ai_set.heart_icon_h])
        self.image.fill(ai_set.action_color)
        self.image.set_colorkey(ai_set.action_color)
        self.width = ai_set.heart_icon_w
        self.height = ai_set.heart_icon_h
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.center = pos
        self.color = ai_set.RED
        pg.draw.polygon(self.image,self.color, [(self.width/2,self.height),(self.width,self.height/2),(.75*self.width,0),(self.width/2,self.height/4),(self.width/4,0),(0,self.height/2)])

class Text(Sprite):
    def __init__(self,ai_set,bg_color,style,text,size,color,width,height,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.font = pg.font.SysFont(style, size)
        self.textSurf = self.font.render(text,1,color)
        self.image= pg.Surface((int(width),int(height)))
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        self.rect = self.image.get_rect(topleft=(x,y))
     
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [0,0])

class Button(Sprite):
# pause_text.add(Button((ai_set.action_w*.25, ai_set.action_h*.89),[200,50],ai_set.GREEN,'Press R to restart','Arial',20,ai_set.data_color,ai_set.data_color))
    def __init__(self,pos,size,color,text,fstyle,fsize,text_color,rim_color=None):
        super().__init__()
        self.color = color
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect(topleft = pos)
        self.text = text
        self.image.fill(self.color)
        # pg.draw.rect(self.image,color,[0,0,size[0],size[1]],1)
        font = pg.font.SysFont(fstyle, fsize, bold = True)
        self.image.blit(font.render(self.text,True,text_color),(int(size[0]*.25),int(size[1]*.30)))
        if rim_color:
            pg.draw.rect(self.image,rim_color,[0,0,size[0],size[1]],3)
        

        



# creates spikes across the action screen
class CeilingSpikes(Sprite):
    def __init__(self,ai_set,pos):
        super().__init__()
        self.image = pg.Surface([ai_set.ceiling_spike_w,ai_set.ceiling_spike_h])
        self.rect = self.image.get_rect(topleft=(pos))
        self.width = ai_set.ceiling_spike_w
        self.height = ai_set.ceiling_spike_h
        self.x = 0
        self.y = 5
        self.image.set_colorkey(ai_set.BLACK)
        pg.draw.polygon(self.image,ai_set.GRAY,
        [(self.x,self.y),
        (self.x,self.y+self.height),
        (self.x+self.width,self.y+self.height),
        (self.x+self.width,self.y),
        (self.x+(self.width-self.width/20),self.y-self.height/2),
        (self.x+(self.width-self.width/10),self.y),
        (self.x+(self.width-3*self.width/20),self.y-self.height/2),
        (self.x+(self.width-self.width/5),self.y),
        (self.x+(self.width-self.width/4),self.y-self.height/2),
        (self.x+(self.width-3*self.width/10),self.y),
        (self.x+(self.width-7*self.width/20),self.y-self.height/2),
        (self.x+(self.width-2*self.width/5),self.y),
        (self.x+(self.width-9*self.width/20),self.y-self.height/2),
        (self.x+(self.width-self.width/2),self.y),
        (self.x+(self.width-11*self.width/20),self.y-self.height/2),
        (self.x+(self.width-3*self.width/5),self.y),
        (self.x+(self.width-13*self.width/20),self.y-self.height/2),
        (self.x+(self.width-7*self.width/10),self.y),
        (self.x+(self.width-3*self.width/4),self.y-self.height/2),
        (self.x+(self.width-3*self.width/4),self.y),
        (self.x+(self.width-4*self.width/5),self.y-self.height/2),
        (self.x+(self.width-17*self.width/20),self.y),
        (self.x+(self.width-9*self.width/10),self.y-self.height/2),
        (self.x+(self.width-19*self.width/20),self.y),
        (self.x,self.y)])
    # flip the image so the spikes can face down when the spikes are at the top.
    def flip(self,ai_set):
        pg.transform(self.image, 180)




            
            



            
        

