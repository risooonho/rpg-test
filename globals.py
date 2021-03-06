import os
from ruamel.yaml import YAML

# Don't change any of these!
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTGREY = (211,211,211)
DIMGREY = (105,105,105)

WIDTH, HEIGHT = 64, 64
HEALTH_BAR_LENGTH = 32

MOVE_STEPS = 8
MOVE_TIME = 0.02

# Initialising settings and config
yaml = YAML(typ='rt')
yaml.default_flow_style = None

config = yaml.load(open('content/config.yml'))
settings = yaml.load(open('settings.yml'))

TITLE = config.get('title')
FONT = config.get('font')
WIN_TEXT = config.get('win text')
LOSE_TEXT = config.get('lose text')
TIE_TEXT = config.get('tie text')
FPS = config.get('fps')
START_SCREEN_SPEED = config.get('start screen speed')

STAT_NAMES = config.get('stat names')

EASY_STAT_SPREAD = config.get('easy stat spread')
EASY_ELITE_STAT_SPREAD = config.get('easy elite stat spread')

NORMAL_STAT_SPREAD = config.get('normal stat spread')
NORMAL_ELITE_STAT_SPREAD = config.get('normal elite stat spread')

HARD_STAT_SPREAD = config.get('hard stat spread')
HARD_ELITE_STAT_SPREAD = config.get('hard elite stat spread')

MAX_HP = config.get('max hp')
MAX_DISTANCE = config.get('max distance')

DISPLAY_WIDTH = settings.get('display width')
DISPLAY_HEIGHT = settings.get('display height')
FULLSCREEN = settings.get('fullscreen')

DIFFICULTY = settings.get('difficulty')

BLUE_PARTY = settings.get('blue party')
RED_PARTY = settings.get('red party')
