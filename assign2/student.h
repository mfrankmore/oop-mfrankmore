#pragma once
#include <iostream>
#include <string>

class Student{
    std::string DEFAULT_NAME = "John Doe";
    int DEFAULT_GRADE = 100;
    int FAILING_GRADE = 59;
    
    std::string _name;
    int _grade;

    public:
    

    Student(std::string name, int grade) {
        _name = name;
        _grade = grade;
    }

    Student() {
        _name = DEFAULT_NAME;
        _grade = DEFAULT_GRADE;
    }




};
