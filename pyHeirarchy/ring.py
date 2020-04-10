from jewelry import Jewelry

class Ring(Jewelry):
    DEFAULT_METAL : str = "gold"
    DEFAULT_GEM : str = "none"
    DEFAULT_SIZE : int = 6

    def __init__(self, metal : str = DEFAULT_METAL, gem : str = DEFAULT_GEM, size : int = DEFAULT_SIZE):
        super(Ring,self).__init__(polished = True)
        self._metal = metal
        self._gem = gem
        if size < 3 or size > 12:
            raise ValueError(f"size {size} must be between 3 & 12")
        self._size = size

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

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value : int) -> None:
        if value < 3 or value > 12:
            raise ValueError(f"size {value} must be between 3 & 12")
        self._size = value