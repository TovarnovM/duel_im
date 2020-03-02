from unit import Unit
from screen import Screen
from scene import Scene
from easyvec import Vec2

class Engine(object):
    def __init__(self, scene: Scene, screen: Screen, tank: Unit, enemy: Unit, **kwargs):
        self.scene = scene
        self.screen = screen
        self.units = [tank, enemy]
        self.rounds = set()
        self.time = 0
        self.dt = kwargs.get('dt', 0.1)


    def render(self):
        if self.screen is None:
            return


    def step(self):
        signals = [self.get_signals(u) for u in self.units]
        comands = [u.get_comand(s) for u, s in zip(self.units, signals)]



    def round_step(self, round: Round, dt: float):
        pass

    def _validate(self, comands: dict, name: str, vmin, vmax):
        try:
            v = comands.get(name, 0)
            v = vmax if v > vmax else vmin if v < vmin else v
            return v
        except:
            return 0

    def unit_step(self, unit: Unit, comands: dict, dt: float):
        move = self._validate('move', comands, -1, 1)
        rotate = self._validate('rotate', comands, -1, 1)
        vision = self._validate('vision', -1, 1)
        fire = self._validate('fire', comands, 0, 1)
        if abs(move) > 1e-8:
            p1, p2 = unit.get_move_segment(move, rotate, dt)
            p3 = self.scene.intersect_segment(p1, p2)
            pos_new = p3 if p3 else p2
            unit.pos = pos_new
        unit.rotate(rotate, dt)
        unit.change_vision(vision, dt)
        if fire > 1e-8:
            round_new = unit.shoot()
            if round_new:
                self.rounds.add(round_new)



    def get_signals(self, unit: Unit):
        res = {}
        self.add_ray_signals(unit, res)
        self.add_pos_signals(unit, res)
        self.add_vis_signals(unit, res)
        return res

    def add_vis_signals(self, unit: Unit, signals: dict):
        vis_ploygon = self.scene.get_vis_polygon(unit.pos, unit.r, unit.alpha, unit.thetta)
        signals['enemies'] = []
        signals['rounds'] = []
        for u in self.units:
            if u is not unit:
                upos = u.pos
                if vis_ploygon.is_in(upos):
                    vis_line = upos - unit.pos
                    unit_ox = unit.to_world(Vec2(1,0), is_dir_vector=True)
                    angle = unit_ox.angle_to(vis_line, degrees=True)
                    signals['enemies'].append((angle, vis_line.len()))
        for u in self.units:
            upos = u.pos
            if vis_ploygon.is_in(upos):
                vis_line = upos - unit.pos
                unit_ox = unit.to_world(Vec2(1,0), is_dir_vector=True)
                angle = unit_ox.angle_to(vis_line, degrees=True)
                signals['rounds'].append((angle, vis_line.len()))


    def add_pos_signals(self, unit: Unit, signals: dict):
        signals['pos'] = unit.pos.as_tuple()
        signals['alpha'] = unit.alpha


    def add_ray_signals(self, unit: Unit, signals: dict):
        rays = unit.get_rays_world()
        intersected = [self.scene.intersect_ray(p1, p2) for p1, p2 in rays]
        signals['rays_max'] = [(p1-p2).len() for p1, p2 in rays],
        signals['rays_intersected'] = [(p1-p2).len() for p1, p2 in intersected]
        