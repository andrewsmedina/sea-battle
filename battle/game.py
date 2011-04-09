from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.director import director
from cocos.layer import Layer

import string

class EventLayer(Layer):

    is_event_handler = True

    def __init__(self, matrix):
        super(EventLayer, self).__init__()
        self.matrix = matrix

    def on_mouse_press(self, x, y, *args):
        for line in self.matrix:
            for sprite in line:
                if (x > sprite.position[0]-25) and (x < sprite.position[0]+25) and (y > sprite.position[1]-25) and (y < sprite.position[1]+25):
                    sprite.visible = False

class Ship(Sprite):

    def __init__(self):
        super(Ship, self).__init__('ship.png')

class Game(Scene):

    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__()

        self.build_game_board()

        self.add(EventLayer(self.matrix))

        ship = Ship()
        ship.position = (100, 75)
        self.add(ship, z=100)

    def build_game_board(self):
        self.matrix = []
        for x in range(10):
            line = []

            for y in range(10):
                square = Sprite('square.png')
                square.position = (75 + (50 * x), 75 + (50 * y))
                self.add(square)

                line.append(square)

            self.matrix.append(line)

        self.line_labels()
        self.column_labels()

    def line_labels(self):
        for x in range(10):
            label = Label(str(10-x), font_size=12)
            label.position = (30, 70 + (50 * x))
            self.add(label)

    def column_labels(self):
        for x in range(10):
            label = Label(string.letters[x].upper(), font_size=12)
            label.position = (70 + (50 * x), 30)
            self.add(label)

if __name__ == '__main__':
    director.init(resizable=False, width=800, height=600)
    director.run(Game())
