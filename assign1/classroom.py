from typing import Sequence
from student import Student

class Classroom:
    def __init__(self, subject : str, capacity : int):
        self._subject : str = subject
        self._capacity : int = capacity

    
    @property
    def subject(self):
        return self._subject

    @property
    def capacity(self):
        return self._capacity