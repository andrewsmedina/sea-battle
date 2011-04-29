from cocos.text import Label
from cocos.layer import Layer

score_points = 0

class Score(Layer):
    def __init__(self):
        super(Score, self).__init__()
        self.score = Label('score:', font_size=20, color=(255,255,255,255))
        self.position = (580, 530)
        self.score.position = (0,0)
        self.add(self.score)

    def draw(self):
        super(Score, self).draw()
        self.score.element.text = 'Score: %d' % score_points


