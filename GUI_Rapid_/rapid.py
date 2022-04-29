import pygame as pg
from settings import Settings
from platforms import Tile,Spike, HeartTile
from player import Player
from game_layout import DataScreen, ActionScreen,Brick, HeartIcon,Text,CeilingSpikes
import game_fxn as gf
from pygame.sprite import Group
from random import randint,choice
import sys
pg.init()

#set framerate
clock = pg.time.Clock()
FPS = 60


#settings instance and setting game screen
ai_set=Settings()
screen = pg.display.set_mode(ai_set.size)

#game title  
pg.display.set_caption  = "Rapid Roll"

#font variable
font = pg.font.SysFont('Comic Sans MS', 20, bold = True)

# group variables 
# action groups
layout_var = Group()
tiles= Group()
spikes= Group()
# text groups
pause_text = Group()
intro_text=Group()
over_text=Group()
bad_hit_text = Group()

# add item instances to groups
layout_var.add(ActionScreen(ai_set))
layout_var.add(DataScreen(ai_set))
# left side brick column
layout_var.add(Brick(ai_set,0,ai_set.data_h))
#right side brick column
layout_var.add(Brick(ai_set,ai_set.action_w,ai_set.data_h))
layout_var.add(CeilingSpikes(ai_set,(ai_set.action_x,ai_set.screen_h-ai_set.ceiling_spike_h)))
layout_var.add(Text(ai_set,ai_set.BLACK,'Arial','SCORE',10,ai_set.data_color,40,15,int(ai_set.data_w*.05),int(ai_set.data_h*.20)))
layout_var.add(HeartIcon(ai_set,(int(ai_set.lives_txt_x*.94),int(ai_set.lives_txt_y*1.2))))
tiles.add(Tile(ai_set,(120,ai_set.screen_h-ai_set.tile_h)))

ball= Player(ai_set)


# def message_to_screen(msg,color,y_displace=0):
#     textSurf, textRect = text_objects(msg,objects)

# fxn for the pause screen
def pause():

    paused = True
    while paused:
        screen.fill(ai_set.WHITE)

        # text objects for pause screen
        # params are self,ai_set,bg_color,style,text,size,color,width,height,x,y
        pause_text.add(Text(ai_set,ai_set.WHITE,'Arial','Paused!',60,ai_set.action_color,200,200,int(ai_set.action_w* .25),int(ai_set.action_h*.30)))
        pause_text.add(Text(ai_set,ai_set.WHITE,'Arial','Press c to continue',20,ai_set.BLACK,200,200,int(ai_set.action_w* .30),int(ai_set.action_h*.73)))
        pause_text.add(Text(ai_set,ai_set.WHITE,'Arial','Press Esc to quit',20,ai_set.BLACK,200,200,int(ai_set.action_w* .30),int(ai_set.action_h*.81)))
        pause_text.add(Text(ai_set,ai_set.WHITE,'Arial','Press r to restart',20,ai_set.BLACK,200,200,int(ai_set.action_w* .30),int(ai_set.action_h*.89)))

        # event logic
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_c:
                    paused = False   
                if event.key == pg.K_r:
                    ball.score =0
                    ball.lives =3
                    main()
                if event.key == pg.K_i:
                    intro()
        pause_text.draw(screen)
        # screen.blit(pause_text.image, (pause_text.rect))    
        # screen.blit(pause_info.image, (pause_info.rect))    
        pg.display.update()       
        clock.tick(60)

def main():
    # tiles.empty()
    # spikes.empty()
    dt=0
    tile_timer = ai_set.tile_respawn_time
    heartSpawned = False
    spikeSpawned = False
    run= True
    while run:
        clock.tick(FPS)
        gf.check_events(ai_set,ball,pause,intro)

        tile_timer-=dt
        #
        if tile_timer <= 0:
            if heartSpawned:
                opt=[0,2,3]
                tile_type = choice(opt)
            elif spikeSpawned:
                tile_type = randint(1,3)
            else:
                tile_type =randint(0,3)
            if tile_type==0:
                tile_x = randint(ai_set.action_x,ai_set.action_w-ai_set.tile_w)
                spikes.add(Spike(ai_set,(tile_x,ai_set.screen_h-ai_set.tile_h)))
                tile_timer = ai_set.tile_respawn_time
                heartSpawned = False
                spikeSpawned = True
            elif tile_type ==1:
                tile_x = randint(ai_set.action_x,ai_set.action_w-ai_set.tile_w)
                tiles.add(Tile(ai_set,(tile_x,ai_set.screen_h-ai_set.tile_h)))
                tiles.add(HeartTile(ai_set,(tile_x+randint(1,8),ai_set.screen_h-ai_set.tile_h-ai_set.heart_h-7)))
                tile_timer = ai_set.tile_respawn_time
                heartSpawned = True
                spikeSpawned=False
            else:
                tile_x = randint(ai_set.action_x,ai_set.action_w-ai_set.tile_w)
                tiles.add(Tile(ai_set,(tile_x,ai_set.screen_h-ai_set.tile_h)))
                tile_timer = ai_set.tile_respawn_time
                heartSpawned = False
                spikeSpawned = False        
        gf.update(ai_set, screen, ball,layout_var,tiles,spikes) 
        dt=clock.tick(60)/1000


def intro():
    intro = True
    intro_text.add(Text(ai_set,ai_set.action_color,'ComicSans','Rapid',60,ai_set.BLACK,200,200,int(ai_set.action_w* .23),int(ai_set.action_h*.25)))
    intro_text.add(Text(ai_set,ai_set.action_color,'ComicSans','Roll',60,ai_set.BLACK,200,200,int(ai_set.action_w* .33),int(ai_set.action_h*.35)))
    intro_text.add(Text(ai_set,ai_set.action_color,'Arial','Press s to start',20,ai_set.RED,200,200,int(ai_set.action_w* .10),int(ai_set.action_h*.70)))
    intro_text.add(Text(ai_set,ai_set.action_color,'Arial','Press esc to exit',20,ai_set.RED,200,200,int(ai_set.action_w* .60),int(ai_set.action_h*.70)))
    while intro:
        for event in pg.event.get():
            screen.fill(ai_set.action_color)
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_s:
                    main()
                    intro= False
            intro_text.draw(screen)
            pg.display.update()

def bad_hit_respawn():
    respawn= True
    ball.bad_collide = False
    # self,ai_set,bg_color,style,text,size,color,width,height,x,y
    bad_hit_text.add(Text(
        ai_set,ai_set.action_color,'ComicSans','press spacebar',40,ai_set.WHITE,ai_set.action_w*7//10,ai_set.action_h//2,
        int(ai_set.action_w* .25),int(ai_set.action_h*.30)))
    while respawn:
        gf.ball_respawn(ai_set,tiles,spikes,ball)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                     sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_SPACE:
                    HeartIcon.color = ai_set.RED
                    main()
                    respawn = False
                # if event.type == pg.K_d:
                #     ball.moving_right = False
                # if event.type == pg.K_a:
                #     ball.moving_left = False
        
        bad_hit_text.draw(screen)
        pg.display.update()


def gameOver():
    over = True
    while over:
        screen.fill(ai_set.WHITE)
        over_text.add(Text(ai_set,ai_set.WHITE,'Arial','Game Over..',60,ai_set.RED,400,200,int(ai_set.action_w* .05),int(ai_set.action_h*.30)))
        over_text.add(Text(ai_set,ai_set.WHITE,'Arial','Press Esc to quit',20,ai_set.BLACK,200,200,int(ai_set.action_w* .30),int(ai_set.action_h*.81)))
        over_text.add(Text(ai_set,ai_set.WHITE,'Arial','Press r to restart',20,ai_set.BLACK,200,200,int(ai_set.action_w* .30),int(ai_set.action_h*.89)))

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_r:
                    over = False   
                    ball.score =0
                    ball.lives =3
                    main()
        over_text.draw(screen)
        pg.display.update()       
        clock.tick(60)                
                

if __name__ == '__main__':
    intro()
