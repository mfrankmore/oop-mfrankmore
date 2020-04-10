from jewelry import Jewelry

class Necklace(Jewelry):
    def __init__(self, metal : str, gem : str):
        super(Necklace,self).__init__(polished = True)
        self._metal = metal
        self._gem = gem

    @property
    def 