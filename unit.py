from easyvec import Vec2, Mat2, PolyLine
from easyvec.geometry import _convert
from screen import Screen
from math import pi, sqrt
import numpy as np

class Unit(object):
    def __init__(self, pos, alpha, brain_foo, thetta, r, v_max, d_alpha_max, n_rays, s_vis, dmg, round_vel, hp, shot_delta):
        self.pos = _convert(pos)
        self.alpha = alpha
        self.brain_foo = brain_foo
        self.thetta = thetta
        self.r = r
        self.v_max = v_max
        self.d_alpha_max = d_alpha_max
        self.n_rays = n_rays
        self.s_vis = s_vis
        self.polygon_local = PolyLine([Vec2(1,0), Vec2(-0.25,-0.5), Vec2(-0.25,0.5)], enclosed=True)
        self.dmg = dmg
        self.round_vel = round_vel
        self.hp = hp
        self.time = 0
        self.time_last_shot = -999
        self.shot_delta = shot_delta

    @property
    def can_shoot(self):
        return self.time - self.shot_delta > self.time_last_shot

    def get_move_segment(self, vel_portion: float, dalpha_portion: float, dt: float):
        if abs(vel_portion) < 1e-8:
            return None
        vel_portion = 1 if vel_portion > 1 else -1 if vel_portion < -1 else vel_portion
        dalpha_portion = 1 if dalpha_portion > 1 else -1 if dalpha_portion < -1 else dalpha_portion
        vel = Vec2(self.v_max*vel_portion * dt, 0).rotate(self.alpha + dalpha_portion*self.d_alpha_max*dt/2, degrees=True)
        return (self.pos.copy(), self.pos + vel)

    def rotate(self, rotate_signal, dt):
        self.set_alpha(self.alpha + dt * rotate_signal * self.d_alpha_max)

    def change_vision(self, d_vision, dt):
        thetta_new = self.thetta + dt * d_vision
        thetta_new = 360 if thetta_new > 360 else 2 if thetta_new < 2 else thetta_new
        self.set_thetta(thetta_new)

    @property
    def polygon_world(self):
        return self.polygon_local.transform(self.self.M_rot_1).add_vec(self.pos)

    def set_thetta(self, thetta):
        self.thetta = thetta
        r = sqrt(s_vis/thetta * 180 / pi)
        self.angles = np.linspace(-self.thetta, self.thetta, self.n_rays)
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

    def get_comand(self, signals: dict):
        if self.brain_foo:
            return self.brain_foo(signals)
        return {}

    def shoot(self) -> Round:
        if not self.can_shoot:
            return None
        angle = np.random.normal(self.alpha, self.thetta/3)
        vel = Vec2(self.round_vel, 0).rotate(angle, degrees=True)
        self.time_last_shot = self.time
        return Round(self.pos, vel, self.dmg)

    



class Round(object):
    def __init__(self, pos, vel, dmg):
        self.pos = _convert(pos).copy()
        self.vel = _convert(vel).copy()
        self.dmg = dmg
        self.alive = True

    def get_move_segment(self, dt: float):
        return (self.pos.copy(), self.pos + dt * self.vel)



if __name__ == "__main__":
    m = Mat2.from_angle(90, True)
    print(m._1 * Vec2(1,0))

    