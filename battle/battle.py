from cocos.director import director
from cocos.scene import Scene
from cocos.menu import Menu, MenuItem
from pyglet import font
from score import Score
from cocos.layer import Layer
from cocos.text import *
from cocos.menu import *

import os
import game
import pyglet


class Background(Layer):
    def __init__(self):
        super(Background, self).__init__()
        self.img = pyglet.resource.image('bg.jpg')

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()


class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__('sea battle')

        self.font_title['font_name'] = "Operating instructions"
        self.font_item['font_name'] = "Operating instructions"
        self.font_item_selected['font_name'] = "Operating instructions"

        self.font_title['font_size'] = 70
        self.font_title['color'] = (255, 255, 255, 255)
        self.font_title['anchor_y'] = "top"

        self.font_item['font_size'] = 46
        self.font_item['color'] = (0xf6, 0xef, 0x8f, 255)

        self.font_item_selected['font_size'] = 50
        self.font_item_selected['color'] = (255, 255, 255, 255)

        self.menu_valign = BOTTOM


        items = []
        items.append(MenuItem('Start', self.on_start))
        items.append(MenuItem('Quit', self.on_quit))

        self.create_menu(items)

    def on_start(self):
        game_scene = game.Game()
        game_scene.add(Score(), z=2)
        director.push(game_scene)

    def on_quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    font_path = os.path.join(os.path.dirname(__file__), 'media/font')
    font.add_directory(font_path)

    director.init(resizable=False, width=800, height=600)

    scene = Scene(Background())
    scene.add(MainMenu())

    director.run(scene)
