
from rapid import bad_hit_respawn,gameOver
import pygame as pg
import sys
from player import Player
from game_layout import Brick,HeartIcon
from platforms import Tile,Spike,HeartTile
from settings import Settings

from pygame.sprite import Group
def check_events(ai_set,ball,pause,intro):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            if event.key == pg.K_a:
                ball.moving_left = True
            if event.key == pg.K_d:
                ball.moving_right = True
            if event.key == pg.K_t:
                ai_set.platform_gravity = 0
            if event.key == pg.K_p:
                pause()
            if event.key == pg.K_i:
                intro()
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                ball.moving_left = False
            if event.key == pg.K_d:
                ball.moving_right = False
                
#(1) see if you can refactor this here
# def check_pause_events(paused):
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             sys.exit()
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_ESCAPE:
#                 sys.exit()
#             if event.key == pg.K_c:
#                 print(paused,0)
#                 paused = False
              
                  

def ball_respawn(ai_set,tiles,spikes,ball):
    btwn2n5= []
    [btwn2n5.append(i) for i in range(int(ai_set.action_h*.4),int(ai_set.action_h*.8))]
    for tile in tiles:
        if tile.rect.y in  btwn2n5:
            ball.rect.y = tile.rect.y + 15
            ball.rect.x = tile.rect.x + ai_set.tile_w//2
            return
    for spike in spikes: 
        if spike.rect.y in btwn2n5:
            if spike.rect.x + ai_set.tile_w + 50 > ai_set.action_w:
                ball.rect.y = spike.rect.y
                ball.rect.x = spike.rect.x + ai_set.tile_w + 20
                return
            ball.rect.y = spike.rect.y
            ball.rect.x = spike.rect.x - 100
            return 

    
            

            






def update(ai_set,screen,ball,layout_objs,tiles,spikes):
    score=0
    screen.fill(ai_set.brick_color)
    # iterates brick columns
    for cls in layout_objs:
        if cls.__class__ == Brick:
            cls.brick_col(ai_set,0)
            cls.brick_col(ai_set,ai_set.brick_w)
    layout_objs.draw(screen)
    tiles.draw(screen)
    spikes.draw(screen)
    #  Player score,collision, and movement
    ball.move(ai_set)
    ball.tile_collide(ai_set,tiles)
    ball.spike_collide(spikes)
    [ball.heart_collide(ai_set,obj) for obj in tiles if obj.__class__==HeartTile]
    # [print(obj.rect.x,obj.rect.y) for obj in layout_objs if obj.__class__ == HeartIcon]
    #objs gravity
    for obj in tiles: obj.gravity(ai_set)
    for obj in spikes: obj.gravity(ai_set)
    #  linking player score and rendering it
    score=ball.score
    font = pg.font.Font(None,30)
    scrtext = font.render(str(score),1, (0,255,0))
    lives = ball.lives
    lives_txt = font.render(f'x {ball.lives}',True,(ai_set.RED))
    screen.blit(scrtext, (int(ai_set.scr_txt_w),int(ai_set.scr_txt_h)))
    screen.blit(lives_txt, (int(ai_set.lives_txt_x),int(ai_set.lives_txt_y)))
    screen.blit(ball.image,ball.rect)
    if ball.bad_collide:
        ball.lives -=1
        ball.moving_right = False
        ball.moving_left = False
        bad_hit_respawn()
    if ball.lives<0:
        gameOver()
    # increase speed at certain 
    # if ball.score >= ball.speed_flag:
    #     ai_set.platform_gravity +=.5
    #     ai_set.tile_respawn_time -= .005
    #     ball.speed_flag += 100
    #     print(ai_set.platform_gravity, ai_set.tile_respawn_time)
    pg.display.update()
    








    
    




   
   
   
   
