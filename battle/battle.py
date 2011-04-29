from cocos.director import director
from cocos.scene import Scene
from cocos.menu import Menu, MenuItem
from pyglet import font
from score import Score

import os
import game
import pyglet

class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__('sea battle')

        self.font_title['font_name'] = "Operating instructions"
        self.font_item['font_name'] = "Operating instructions"
        self.font_item_selected['font_name'] = "Operating instructions"

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

    scene = Scene()
    scene.add(MainMenu())

    director.run(scene)
