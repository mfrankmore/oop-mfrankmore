from .container import Container

class Package(Container):
    DEFAULT_WEIGHT : float = 0.0
    
    DEFAULT_CONTENTS : str = "Empty"

    def __init__(self, weight : float = DEFAULT_WEIGHT, contents : str = DEFAULT_CONTENTS):
        self._weight = weight
        self._contents = contents

    @property
    def weight(self) -> float:
        return self._weight

    @property
    def contents(self) -> str:
        return self._contents

    

    
