from easyvec import Vec2, Mat2
from easyvec.geometry import _convert
from screen import Screen
from math import pi, sqrt
import numpy as np

class Unit(object):
    def __init__(self, pos, alpha, brain_foo, thetta, r, v_max, d_alpha_max, n_rays, s_vis):
        self.pos = _convert(pos)
        self.alpha = alpha
        self.brain_foo = brain_foo
        self.thetta = thetta
        self.r = r
        self.v_max = v_max
        self.d_alpha_max = d_alpha_max
        self.n_rays = n_rays
        self.s_vis = s_vis

    def set_thetta(self, thetta):
        self.thetta = thetta
        r = sqrt(s_vis/thetta * 180 / pi)
        angles = np.linspace(-self.thetta, self.thetta, self.n_rays)
        self.rays = [Vec2(r,0).rotate(angle, degrees=True) for angle in angles]

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.M_rot = Mat2.from_angle(alpha, degrees=True)
        self.M_rot_1 = self.M_rot._1

    def to_world(self, local: Vec2, is_dir_vector=False) -> Vec2:
        if is_dir_vector:
            return self.M_rot_1 * local
        return self.M_rot_1 * local + self.pos

    def to_local(self, world: Vec2, is_dir_vector=False) -> Vec2:
        if is_dir_vector:
            return self.M_rot * world
        return self.M_rot * (world - self.pos)

    def get_rays_world(self):
        return [(self.pos.copy(), self.to_world(ray_p)) for ray_p in self.rays]        

    def update(self, units):
        pass


if __name__ == "__main__":
    m = Mat2.from_angle(90, True)
    print(m._1 * Vec2(1,0))

    