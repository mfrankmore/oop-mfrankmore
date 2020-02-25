from typing import Sequence
from student import Student

class Classroom:
    def __init__(self, subject : str, attendance : Student, pupil : str = Student.name, grade : int = Student.DEFAULT_GRADE):
        self._subject : str = subject
        self._attendence : Sequence[Student] = (Student(pupil, grade), Student(pupil, grade), Student(pupil, grade))  


    
    @property
    def subject(self):
        return self._subject

    @property
    def pupil1(self):
        return self._attendence[0]

    @property
    def pupil2(self):
        return self._attendence[1]

    @property
    def pupil3(self):
        return self._attendence[2]