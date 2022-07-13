# CASTING CONSTANTS
from game.casting.color import Color


# GAME
GAME_NAME = "Air Hockey"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1035
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 50
FIELD_BOTTOM = SCREEN_HEIGHT-15
FIELD_LEFT = 15
FIELD_RIGHT = SCREEN_WIDTH-15

# STATS
STATS_GROUP = "stats"

# SURFACE
SURFACE_GROUP = "surface"
SURFACE_IMAGE = "AirHockey/assets/images/surface.png"
SURFACE_WIDTH = 1040
SURFACE_HEIGHT = 669

#SOUND
BOUNCE_SOUND = "AirHockey/assets/sounds/boing.wav"
WELCOME_SOUND = "AirHockey/assets/sounds/start.wav"
OVER_SOUND = "AirHockey/assets/sounds/over.wav"
GOAL = "AirHockey/assets/sounds/goal.wav"
SLIDE_HIT = "AirHockey/assets/sounds/slide_hit.wav"

# PUCK
PUCK_GROUP = "pucks"
PUCK_IMAGE = "AirHockey/assets/images/puck.png"
PUCK_WIDTH = 50
PUCK_HEIGHT = 50
PUCK_VELOCITY = 0

# paddle
PADDLE_ONE_GROUP = "paddle"
PADDLE_TWO_GROUP = "paddle2"
PADDLE_IMAGE_1 = "AirHockey/assets/images/paddle.png"
PADDLE_IMAGE_2 = "AirHockey/assets/images/paddle2.png"
PADDLE_WIDTH = 60  
PADDLE_HEIGHT = 60
PADDLE_RATE = 6
PADDLE_VELOCITY = 8

# FONT
FONT_FILE = "AirHockey/assets/fonts/zorque.otf"
FONT_SMALL = 30
FONT_LARGE = 48

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
W_KEY = "w"
A_KEY = "a"
S_KEY = "s"
D_KEY = "d"
I_KEY = "i"
J_KEY = "j"
K_KEY = "k"
L_KEY = "l"

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WINNER1 = "PLAYER 1 WINS"
WINNER2 = "PLAYER 2 WINS"

# HUD
HUD_MARGIN = 3
SCORE_1_GROUP = "score1"
SCORE_2_GROUP = "score2"
SCORE_FORMAT = "SCORE: {}"
PLAYER_A= "Player 1: {}"
PLAYER_B= "Player 2: {}"