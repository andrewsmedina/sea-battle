from cocos.layer import Layer


class EventLayer(Layer):

    is_event_handler = True

    def __init__(self, matrix, ship):
        super(EventLayer, self).__init__()
        self.matrix = matrix
        self.ship = ship

    def on_mouse_press(self, x, y, *args):
        for line in self.matrix:
            for sprite in line:
                if sprite.contains(x,y):
                    if sprite.visible:
                        sprite.visible = False
                        if self.ship.contains(x,y):
                            self.ship.shoted()


