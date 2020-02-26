import pygame

from easyvec import Vec2
from easyvec.geometry import PolyLine, _convert


class Screen(object):
    """Класс для отображения состояния имитационной модели на плоскости. Требует библиотеки pygame ($pip install pygame)
    """
    def __init__(self, display_width, display_height, v0, v1):
        """Конструктор
        
        Arguments:
            display_width {int} -- ширина окна отображения в пикселях
            display_height {int} -- высота окна отображения в пикселях
            v0 {float} -- координаты нижней левой координаты оботбражения
            v1 {float} -- координаты верхней правой координаты оботбражения
        """
        self.v1 = _convert(v1)
        self.v0 = _convert(v0)
        self.display_height = display_height
        self.display_width = display_width
        self.pygame = None

    def to_pixels(self, vec):
        """Метод перевода координат имитационной модели в пиксели на экране отображения
        
        Arguments:
            vec {Vec2d} -- координата для перевода
        
        Returns:
            tuple(int, int) -- пиксельные координаты, соответствующие координате для перевода
        """
        masht_x = self.display_width / (self.v1.x - self.v0.x)
        masht_y = self.display_height / (self.v1.y - self.v0.y)

        x = int((vec.x - self.v0.x)*masht_x)
        y = int((self.v1.y - vec.y)*masht_y)
        return x, y

    def to_vec(self, x, y):
        """Метод перевода пиксельных координат в координаты имитационной модели
        
        Arguments:
            x {int} -- пиксельная координата по оси абсцисс
            y {int} -- пиксельная координата по оси ординат
        
        Returns:
            Vec2d -- соответствующая координата имитационной модели
        """
        masht_x = self.display_width / (self.v1.x - self.v0.x)
        masht_y = self.display_height / (self.v1.y - self.v0.y)

        res = Vec2(self.v0.x + x/masht_x, self.v1.y - y/masht_y)
        return res

    def update(self, clock_tick=None):
        """Обновить экран отображения
        
        Keyword Arguments:
            clock_tick {int} -- максимальное количество кадров в секунду (default: {None})
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        if clock_tick is not None:
            self.clock.tick(clock_tick)

    def draw(self, who):
        self._initpygame()
        if isinstance(who, PolyLine):
            self.draw_poly_line(who)

    def draw_poly_line(self, pl: PolyLine):
        self.pygame.draw.aalines(
            self.screen_main, 
            (255,0,0), 
            pl.enclosed, 
            [self.to_pixels(v) for v in pl.vecs], 
            2)

    def fill(self, color=None):
        """Заполнить экран сплошным цветом
        
        Keyword Arguments:
            color {tuple} -- код цвета (по-умолчанию белый (255,255,255)) (default: {None})
        """

        self.screen_main.fill(color if color else (255, 255, 255))

    def close(self):
        """Закончить отображение
        """
        pygame.quit()

    def __del__(self):
        """Destructor
        """
        self.close()

    def _initpygame(self):
        if self.pygame:
            return
        self.pygame = pygame
        self.pygame.init()
        self.screen_main = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()