from cocos.layer import Layer

import score


class EventLayer(Layer):

    is_event_handler = True

    def __init__(self, matrix, ship, ship2):
        super(EventLayer, self).__init__()
        self.matrix = matrix
        self.ship = ship
        self.ship2 = ship2

    def on_mouse_press(self, x, y, *args):
        for line in self.matrix:
            for sprite in line:
                if sprite.contains(x,y):
                    if sprite.visible:
                        sprite.visible = False
                        if self.ship.contains(x,y):
                            self.ship.shoted()
                        elif self.ship2.contains(x, y):
                            self.ship2.shoted()
                        else:
                            score.score_points -= 1


