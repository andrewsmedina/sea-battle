from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.director import director

class Game(Scene):

    def __init__(self):
        super(Game, self).__init__()

        self.build_game_board()

    def build_game_board(self):

        for x in range(10):
            for y in range(10):
                square = Sprite('square.png')
                square.position = (75 + (50 * x), 75 + (50 * y))
                self.add(square)

        self.line_labels()

    def line_labels(self):
        for x in range(10):
            label = Label(str(10-x), font_size=12)
            label.position = (30, 70 + (50 * x))
            self.add(label)

if __name__ == '__main__':
    director.init(resizable=False, width=800, height=600)
    director.run(Game())
