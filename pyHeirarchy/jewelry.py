class Jewelry:
    def __init__ (self, polished : bool = True):
        self._polished : bool = polished
    @property
    def polished(self) -> bool:
        return self._polished

    def polish(self) -> None:
        self._polished = True

    def wear(self) -> None:
        self._polished = False

    