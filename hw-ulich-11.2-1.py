from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def prepare_floor(self):
        pass

    @abstractmethod
    def lay_tiles(self):
        pass

    @abstractmethod
    def apply_plaster(self):
        pass

    @abstractmethod
    def apply_putty(self):
        pass

    @abstractmethod
    def prime_wall(self):
        pass

    @abstractmethod
    def paint_wall(self):
        pass

class TileLayer(Builder):
    def prepare_floor(self):
        print("Подготовка пола")

    def lay_tiles(self):
        print("Укладка плитки")

    def apply_plaster(self):
        pass

    def apply_putty(self):
        pass

    def prime_wall(self):
        pass

    def paint_wall(self):
        pass

class Finisher(Builder):
    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_plaster(self):
        print("Нанесение шпаклевки")

    def apply_putty(self):
        print("Оштукатуривание стен")

    def prime_wall(self):
        pass

    def paint_wall(self):
        pass

class Painter(Builder):
    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_plaster(self):
        pass

    def apply_putty(self):
        pass

    def prime_wall(self):
        print("Грунтование стен")

    def paint_wall(self):
        print("Покраска стен")

class Foreman:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def make_floors(self):
        self.builder.prepare_floor()
        self.builder.lay_tiles()

    def make_walls(self):
        self.builder.apply_plaster()
        self.builder.apply_putty()
        self.builder.prime_wall()
        self.builder.paint_wall()

    def make_all(self):
        self.make_floors()
        self.make_walls()

if __name__ == "__main__" :
    tile_layer = TileLayer()
    finisher = Finisher()
    painter = Painter()

    foreman = Foreman()

    foreman.set_builder(tile_layer)
    foreman.make_floors()

    foreman.set_builder(finisher)
    foreman.make_walls()

    foreman.set_builder(painter)
    foreman.make_walls()

    foreman.set_builder(tile_layer)
    foreman.set_builder(finisher)
    foreman.set_builder(painter)
    foreman.make_all()
