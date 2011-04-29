from cocos.sprite import Sprite

import score

class Ship(Sprite):

    def __init__(self):
        super(Ship, self).__init__('ship.png')
        self.shots_received = 0
        self.visible = False

    def shoted(self):
        score.score_points += 10

        self.shots_received += 1

        if self.shots_received == 2:
            self.visible = True


