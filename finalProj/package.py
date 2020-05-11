from container import Container

class Package(Container):
    DEFAULT_WEIGHT : float = 0.0
    DEFAULT_CONTENTS : str = "Empty"

    def __init__(self, weight : float = DEFAULT_WEIGHT, contents : str = DEFAULT_CONTENTS, packageType : Container = Container.DEFAULT_CONTAINER_TYPE):
        super(Package, self).__init__(containerType = packageType)
        self._weight = weight
        self._contents = contents
        self._packageType = packageType


    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value : float) -> None:
        if value >= 0:
            self._weight = value
        else:
            raise ValueError(f"Weight must be a non-negative number")

    @property
    def contents(self) -> str:
        return self._contents

    @contents.setter
    def contents(self, value : str) -> None:
        self._contents = value
