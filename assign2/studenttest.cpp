#include <iostream>
#include "student.h"

using namespace std;

void testConst();

int main() {
    //Test Calls
    testConst();

    return 0;
}

void testConst() {
    int defGradeTest = 100;
    string defNameTest = "John Doe";
    Student stud1 = Student();
    if (stud1.getName() == defNameTest)
        cout << "Default Name Test Passed." << endl;
    else 
        cout << "Default Name Test Failed." << endl;

    if (stud1.getGrade() == defGradeTest) 
        cout << "Defult Grade Test Passed." << endl;
    else
        cout << "Default Grade Test Failed." << endl;
    
    defGradeTest = 80;
    defNameTest = "Jack Smith";

    Student stud2 = Student(defNameTest, defGradeTest);
    if (stud2.getName() == defNameTest)
        cout << "Name Test Passed." << endl;
    else 
        cout << "Name Test Failed." << endl;

    if (stud2.getGrade() == defGradeTest) 
        cout << "Grade Test Passed." << endl;
    else
        cout << "Grade Test Failed." << endl;


    return;
}