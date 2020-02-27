from easyvec import Vec2
from easyvec.geometry import _convert
from screen import Screen

class Unit(object):
    def __init__(self, pos, alpha, brain_foo, thetta, r, v_max, d_alpha_max):
        self.pos = _convert(pos)
        self.alpha = alpha
        self.brain_foo = brain_foo
        self.thetta = thetta
        self.r = r
        self.v_max = v_max
        self.d_alpha_max = d_alpha_max

    def draw(self, screen: Screen):
        p = screen.to_pixels(self.pos)
        

    def update(self, units):
        pass


    