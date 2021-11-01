import pygame
import random
from pygame.locals import *
from os import path
from Class import *
from Function import *
from Settings import *
from ScaledGame import *

class Game:
    def __init__(self, main):
        self.main = main
        self.game_dict = self.main.main_dict["game"]
        self.settings_dict = self.game_dict["settings"]
        self.init_game()

    def init_game(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def new_game(self):
        self.main.update_menu("battle_menu")
        self.player = Player(self.main, self.main.player, self.game_dict, data="character", item="player")

    def use_weapon(self):
        print("Use Weapon WIP")


class Player(pygame.sprite.Sprite):
    def __init__(self, main, group, dict, data, item, parent=None, variable=None, action=None):
        # Initialization -------------- #
        init_sprite(self, main, group, dict, data, item, parent, variable, action)

    def init(self):
        init_sprite_image(self)

    def load(self):
        pass

    def new(self):
        pass

    def get_keys(self):
        # Initialization
        keys = pygame.key.get_pressed()

    def draw(self):
        self.main.gameDisplay.blit(self.image, self.rect)

    def update(self):
        update_time_dependent(self)
        self.main.align_rect(self.surface, self.pos, self.align)





MAIN_DICT = {
    "background": {
        None: None,
        "default": {
            "color": DARK_SKY_BLUE,
            "image": None,
        },
    },
    "music": {
        None: None,
        "default": "music_WinglessSeraph_battle_TheOath.mp3",
    },
    "sound": {
    },
    "font": {
        "LiberationSerif": {"ttf": "LiberationSerif-Regular.ttf", "size": 40}
    },
    "menu": {
        "main_menu": {
            "background": "default",
            "music": "default",
        },
        "pause_menu": {
            "background": None,
            "music": None,
        },
        "battle_menu": {
            "background": None,
            "music": None,
        }
    },
    "button": {
        "settings": {
            "default": {
                "align": "nw", "size": (280, 50),
                "border": True, "border_size": (5, 5), "border_color": BLACK,
                "text_align": "center", "font": "LiberationSerif", "font_color": WHITE,
                "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
                "sound_action": None, "sound_active": None, "sound_inactive": None},
            "weapon_icon": {
                "align": "nw", "size": (50, 50),
                "border": True, "border_size": (5, 5), "border_color": BLACK,
                "text_align": "center", "font": "LiberationSerif", "font_color": WHITE,
                "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
                "sound_action": None, "sound_active": None, "sound_inactive": None},
        },
        "main_menu": {
            "new_game": {"type": "default", "pos": (20, 20), "text": "New Game", "action": "self.game.new_game"},
            "select_level": {"type": "default", "pos": (20, 90), "text": "Select Level", "action": None},
            "exit": {"type": "default", "pos": (20, 160), "text": "Exit", "action": "self.main.quit_game"},
        },
        "battle_menu": {
            "weapon_button": {"type": "weapon_icon", "pos": (20, 20), "text": None, "action": "self.game.use_weapon"},
        }
    },
    "game": {
        "settings": {
            "character": {
                "pos": [640, 360], "align": "center",
                "animation_time": 0.25, "animation_loop": True, "animation_reverse": True
            }
        },
        "character": {
            "player": {
                "image": "sprite_Kaduki_Actor63.png", "size": [32, 32], "scaled_size": [64, 64]
            }
        }
    },
}
