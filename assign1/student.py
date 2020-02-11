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




    @property
    def fail(self) -> bool:
        return self._failing