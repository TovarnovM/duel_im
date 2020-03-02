from easyvec import Vec2, Rect
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

def get_obstacles(w, h):
    r1 = Rect(0,0, w/4, h/4)
    r2 = Rect(w,h, w-w/4, h-h/4)
    

class Scene(object):
    def __init__(self, obstacles):
        self.obstacles = obstacles

    def intersect_ray(self, p1, p2) -> Vec2:
        pass

    def get_vis_polygon(self, pos: Vec2, r: float, alpha: float, thetta: float) -> PolyLine:
        pass

    def intersect_segment(self, p1, p2) -> Vec2:
        pass



if __name__ == "__main__":
    pl = rnd_polygon(200, 100, 50, 3, 20, 20)
    
