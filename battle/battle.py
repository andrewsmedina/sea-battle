from cocos.director import director
from cocos.scene import Scene
from cocos.menu import Menu, MenuItem

from score import Score

import game
import pyglet

class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__('sea battle')

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
    director.init(resizable=False, width=800, height=600)

    scene = Scene()
    scene.add(MainMenu())

    director.run(scene)
