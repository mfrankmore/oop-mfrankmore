class Student:
    DEFAULT_NAME : str = "John Doe"
    DEFAULT_GRADE : int = 100
    FAILING_GRADE : int = 59

    def __init__(self, name : str = DEFAULT_NAME, grade : int = DEFAULT_GRADE):
        self._name = name
        self._grade = grade
        self._failing : bool = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def grade(self) -> int:
        return self._grade

    @grade.setter
    def grade(self, value : int) -> None:
        if abs(value) > 100:
            raise ValueError(f"Grade change must be -100 to 100")
        elif value < 0:
            if self.grade - abs(value) < 0:
                raise ValueError(f"Grade must be great than 0")
            else:
                self.grade -= value
        elif value > 0:
            if self.grade + value > 100:
                raise ValueError(f"Grade must be less than 100")
            else:
                self.grade += value

    @property
    def fail(self) -> bool:
        return self._failing