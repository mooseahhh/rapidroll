
class Settings():
    def __init__(self):
        
        self.BLACK = (0,0,0)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.CRIMSON_RED = (60,0,0)
        self.GRAY = (169,169,169)
        self.WHITE = (255,255,255)

        # Game Screen
        self.screen_h = 600
        self.screen_w= int(self.screen_h * .6)
        self.size = (self.screen_w, self.screen_h)
        
        
        #Game layout--------------------

        # DataScreen specs
        self.data_h= int(self.screen_h/4)
        self.data_w= self.screen_w
        self.data_color = (255,255,0)# yellow
        
        # ActionScreen specs------------
        self.action_h = self.screen_h
        self.action_w = self.screen_w * .85
        
        self.action_x = int(self.screen_w * .15)
        self.action_y = self.data_h
       
        self.action_color = (173,216,230)# light blue

        # brick specs--------------
        self.brick_fill_h = int(self.screen_h - self.data_h)
        self.brick_fill_w = int(self.action_x)
        self.brick_inside_color =(252, 106, 3) # Tiger Orange  
        self.num_of_bricks= 44
        self.brick_h =int(self.screen_h/self.num_of_bricks)
        self.brick_w = int(self.brick_fill_w/2)
        self.brick_color = (122,56,3) #spice

        # Lives Icon-------------
        self.heart_icon_w = 18
        self.heart_icon_h = 18
        self.lives_txt_x = self.data_w*.77
        self.lives_txt_y = self.data_h*.35

        # Ceiling Spikes
        self.ceiling_spike_w = self.action_w-int(self.screen_w-self.action_w)
        self.ceiling_spike_h = 10
    
        # Score Icon ----------------------------
        self.scr_icon_x = self.data_w*.05
        self.scr_icon_y = self.data_h*.20


        self.scr_txt_w= int(self.scr_icon_x)
        self.scr_txt_h = int(self.data_h*.31 ) 
     
        # universal var

        self.GRAVITY = 1

        # Game Objects-----------------------------
        
        # player ball specs
        self.ball_w=15
        self.ball_h=15
        self.ball_rad=5
        self.ball_pos=(self.action_w/2,self.data_h + 30) #centered
        self.ball_speed = 5
        self.point = 1
        # Tile specs------------------
        self.tile_w = 40
        self.tile_h = 10
        self.platform_gravity = 3
        self.tile_respawn_time = .3
        #Heart Specs------------------
        self.heart_w = 8
        self.heart_h = 8



        



       





