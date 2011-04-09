from cocos.director import director
from cocos.scene import Scene
from cocos.menu import Menu, MenuItem

import game
import pyglet

class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__('sea battle')

        items = []
        items.append(MenuItem('Start', self.start))
        items.append(MenuItem('Quit', self.quit))

        self.create_menu(items)

    def start(self):
        game_scene = game.Game()
        director.push(game_scene)

    def quit(self):
        pyglet.app.exit()

if __name__ == "__main__":
    director.init(resizable=False, width=800, height=600)

    scene = Scene()
    scene.add(MainMenu())

    director.run(scene)
