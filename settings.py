# game options/settings
TITLE = "JUMP STREET"
WIDTH = 600
HEIGHT = 600
FPS = 70
FONT_NAME="PressStart2P"
HS_FILE="highscore.txt"

#playerProperties
player_acc=0.5
player_friction=-0.12
player_gravity=1
player_jump=24

#platforms
platform_list=[(WIDTH/2 -90,HEIGHT - 90),
			   (WIDTH / 2 - 50, HEIGHT - 250),
               (125, HEIGHT - 400),
               (350, 200),
               (175, 100)]

#powerups
powerup_freq=6
boost_power=40
mob_freq=5000		   #in milliseconds so this means 5 seconds
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POWERUP_LAYER = 1
MOB_LAYER = 2	   
CLOUD_LAYER=0


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREEN=(0,200,0)
BLUISH=(43,140,221)
BRICK=(230,30,30)
