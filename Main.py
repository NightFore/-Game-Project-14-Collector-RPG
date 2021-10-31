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

    def new_game(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


def init_menu(main, menu, clear=True):
    menu_dict = main.main_dict["menu"][menu]
    if clear:
        clear_menu(main)

    main.update_music(main.music_dict[menu_dict["music"]])
    main.update_background(main.background_dict[menu_dict["background"]])

    for button in main.button_dict[menu]:
        Button(main, main.buttons, main.button_dict, data=menu, item=button)

def clear_menu(main):
    for sprite in main.all_sprites:
        sprite.kill()

def main_menu(main, menu):
    init_menu(main, menu)
    main.game.new_game()

def pause_menu(main):
    main.paused = not main.paused

MAIN_DICT = {
    "background": {
        "default": {
            "color": DARK_SKY_BLUE,
            "image": None,
        },
    },
    "music": {
        "default": None,
    },
    "sound": {
    },
    "font": {
        "LiberationSerif": {"ttf": "LiberationSerif-Regular.ttf", "size": 40}
    },
    "menu": {
        "main_menu": {
            "call": main_menu,
            "background": "default",
            "music": "default",
            "ui": {},
            "button": {},
        },
        "pause_menu": {
            "call": pause_menu,
        },
    },
    "button": {
        "settings": {
            "default": {
                "align": "nw", "size": (280, 50),
                "border": True, "border_size": (5, 5), "border_color": BLACK,
                "text_align": "center", "font": "LiberationSerif", "font_color": WHITE,
                "inactive_color": LIGHT_SKY_BLUE, "active_color": DARK_SKY_BLUE,
                "sound_action": None, "sound_active": None, "sound_inactive": None},
            "icon": {
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
    },
    "game": {
        "settings": {
        },
    },
}
