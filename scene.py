from easyvec import Vec2
from easyvec.geometry import PolyLine, intersect, is_in_polygon 
import numpy as np


def rnd_vec(mx, my, dx, dy):
    x = np.random.uniform(mx-dx, mx+dx)
    y = np.random.uniform(my-dy, my+dy)
    return Vec2(x, y)

def rnd_polygon(x, y, r, n, dx, dy, angle0=None):
    v = Vec2(r, 0)
    v.rotate_( angle0 if angle0 else np.random.uniform(0,360) , degrees=True)
    vs = [v.rotate(i * (360/n), degrees=True) + rnd_vec(x, y, dx, dy) 
        for i in range(n)]
    return PolyLine(vs, enclosed=True)

class Scene(object):
    def __init__(self, screen, tank, enemy, obstacles):
        self.screen = screen
        self.units = [tank, enemy]
        self.obstacles = obstacles

    

if __name__ == "__main__":
    from screen import Screen
    sc = Screen(1000, 500, (0,0), (500, 250))
    pl = rnd_polygon(200, 100, 50, 3, 20, 20)
    sc.draw(pl)
    sc.update()
    input()
    
