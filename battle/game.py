from cocos.scene import Scene
from cocos.sprite import Sprite

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
