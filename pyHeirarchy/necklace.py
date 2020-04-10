from jewelry import Jewelry

class Necklace(Jewelry):
    DEFAULT_METAL : str = "gold"
    DEFAULT_GEM : str = "diamond"

    def __init__(self, metal : str = DEFAULT_METAL, gem : str = DEFAULT_GEM):
        super(Necklace,self).__init__(polished = True)
        self._metal = metal
        self._gem = gem

    @property
    def metal(self) -> str:
        return self._metal

    @metal.setter
    def metal(self, value : str) -> None:
        self._metal = value

    @property
    def gem(self) -> str:
        return self._gem

    @gem.setter
    def gem(self, value : str) -> None:
        self._gem = value

    