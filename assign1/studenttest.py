import unittest

from student import Student

class StudentTest(unittest.TestCase):

    def testDefaults(self):
        student = Student()
        self.assertEqual(student.name, Student.DEFAULT_NAME)
        self.assertEqual(student.grade, Student.DEFAULT_GRADE)
        self.assertEqual(student.fail, False)
        
    def testSpecific(self):
        testName : str = "John Smith"
        testGrade : int = Student.FAILING_GRADE - 10
        student = Student(name = testName, grade = testGrade)
        self.assertEqual(student.name, testName)
        self.assertEqual(student.grade, testGrade)
        #self.assertEqual(student.fail, True)

if __name__ == '__main__':
    unittest.main()