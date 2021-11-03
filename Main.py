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
        self.player = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.weapons = pygame.sprite.Group()

    def draw(self):
        pass

    def update(self):
        pass

    def new_game(self):
        self.main.update_menu("battle_menu")
        self.player = Player(self.main, self.player, self.game_dict, data="character", item="player")
        self.enemy = Enemy(self.main, self.enemy, self.game_dict, data="enemy", item="magician")

    def use_weapon(self):
        print(self.weapons)


class Player(pygame.sprite.Sprite):
    def __init__(self, main, group, dict, data, item, parent=None, variable=None, action=None):
        # Initialization -------------- #
        init_sprite(self, main, group, dict, data, item, parent, variable, action)

    def init(self):
        init_sprite_image_animated(self)
        init_sprite_text(self)

    def load(self):
        self.max_health = self.object["max_health"]
        self.current_health = self.max_health
        self.max_bp = self.object["max_bp"]
        self.bp = self.max_bp
        self.strength = self.object["strength"]
        self.speed = self.object["speed"]

    def new(self):
        self.check = {"weapon_1": True}

    def get_keys(self):
        # Initialization
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LEFT]:
            self.check["weapon_1"] = True
        elif self.check["weapon_1"]:
            self.check["weapon_1"] = False
            Weapon(self.main, self.game.weapons, self.dict, data="weapon", item="sword_001", parent=self)

    def draw(self):
        # Surface
        self.main.gameDisplay.blit(self.image, self.rect)

        # Text
        self.text_health = "HP %i / %i" % (self.current_health, self.max_health)
        self.main.draw_text(self.text_health, self.font, self.font_color, self.text_pos, self.text_align)

    def update(self):
        self.get_keys()
        update_time_dependent(self)
        self.main.align_rect(self.surface, self.pos, self.align)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, main, group, dict, data, item, parent=None, variable=None, action=None):
        # Initialization -------------- #
        init_sprite(self, main, group, dict, data, item, parent, variable, action)

    def init(self):
        init_sprite_image(self, self.main.graphic_folder)

    def load(self):
        self.max_health = self.object["max_health"]
        self.current_health = self.max_health
        self.max_bp = self.object["max_bp"]
        self.bp = self.max_bp
        self.strength = self.object["strength"]
        self.speed = self.object["speed"]

    def new(self):
        pass

    def get_keys(self):
        pass

    def draw(self):
        self.main.gameDisplay.blit(self.image, self.rect)

    def update(self):
        pass


class Weapon(pygame.sprite.Sprite):
    def __init__(self, main, group, dict, data, item, parent=None, variable=None, action=None):
        # Initialization -------------- #
        init_sprite(self, main, group, dict, data, item, parent, variable, action)

    def init(self):
        init_sprite_image(self, self.main.item_folder)

    def load(self):
        self.pos = self.parent.rect[0] + self.parent.rect[2] // 2, self.parent.rect[1] + self.parent.rect[3] // 2
        update_sprite_rect(self, self.pos[0], self.pos[1])

    def new(self):
        pass

    def get_keys(self):
        pass

    def draw(self):
        self.main.gameDisplay.blit(self.image, self.rect)

    def update(self):
        if collide_hit_rect(self, self.game.enemy):
            self.kill()
        self.pos[0] -= 10
        update_sprite_rect(self, self.pos[0], self.pos[1])





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
                "pos": [1130, 590], "align": "s",
                "text_pos": [990, 240], "text_align": "nw",
                "text": None, "font": "LiberationSerif", "font_color": WHITE,
                "animation_time": 0.25, "animation_loop": True, "animation_reverse": True,
            },
            "enemy": {"pos": [200, 590], "align": "s"},
            "sword": {"align": "center"}
        },
        "character": {
            "player": {
                "image": "sprite_Kaduki_Actor63_1.png", "size": [32, 32], "scale_size": [96, 96],
                "max_health": 50, "max_bp": 10, "strength": 5, "speed": 2
            },
        },
        "enemy": {
            "magician": {
                "image": "mon_018_magician_female.bmp", "scale_size": [168, 216], "color_key": (129, 121, 125),
                "max_health": 60, "max_bp": 12, "strength": 3, "speed": 1
            }
        },
        "weapon": {
            "sword_001": {
                "type": "sword",
                "image": "item_WhiteCat_we_sword002.png", "color_key": (50, 201, 196), "scale_size": [48, 48]
            }
        }
    },
}
