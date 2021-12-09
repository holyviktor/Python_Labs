"""
A software academy teaches two types of courses: local courses that are held in some of the
academy’s local labs and offsite courses held in some other town outside of the academy’s
headquarters. Each course has a name, a teacher assigned to teach it and a course program
(sequence of topics). Each teacher has a name and knows the courses he or she teaches. Both
courses and teachers could be printed in human-readable text form. All your courses should
implement ICourse. Teachers should implement ITeacher. Local and offsite courses should implement
ILocalCourse and IOffsiteCourse respectively. Courses and teachers should be created only through
the ICourseFactory interface implemented by a class named CourseFactory. Write a program that will
form courses of software academy.
"""

import json
from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, name): pass

    @property
    @abstractmethod
    def program(self): pass

    @program.setter
    @abstractmethod
    def program(self, program): pass


class ILocalCourse(ABC):
    @abstractmethod
    def __str__(self): pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def __str__(self): pass


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, name): pass

    @property
    @abstractmethod
    def course(self): pass

    @course.setter
    @abstractmethod
    def course(self, course): pass


class ICourseFactory:
    @abstractmethod
    def course_factory(self, name_course):
        pass

    @abstractmethod
    def teacher_factory(self, name_teacher):
        pass


class Course(ICourse):
    def __init__(self, name, program):
        self.name = name
        self.program = program

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        if not name:
            raise ValueError("Name can't be empty!")
        self.__name = name

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not all((pr, str) for pr in program):
            raise TypeError("Program must be str!")
        if not program:
            raise ValueError("Program can't be empty!")
        self.__program = program

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Wrong type of teacher!")
        self.__teacher = teacher


class LocalCourse(Course):
    def __init__(self, name, program):
        super().__init__(name, program)

    def __str__(self):
        return f"Local course {self.name}, teacher: {self.teacher}, program: {self.program}"


class OffsiteCourse(Course):
    def __init__(self, name, program):
        super().__init__(name, program)

    def __str__(self):
        return f"Offsite course {self.name}, teacher: {self.teacher}, program: {self.program}"


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name
        self.course = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        if not name:
            raise ValueError("Name can't be empty!")
        self.__name = name

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if not all(isinstance(cours, (OffsiteCourse, LocalCourse)) for cours in course):
            raise TypeError("Wrong type of course")
        self.__course = course

    def add_course(self, cour):
        if not isinstance(cour, (OffsiteCourse, LocalCourse)):
            raise TypeError("Wrong type of course!")
        self.course.append(cour)

    def __str__(self):
        result = ""
        for cour in self.course:
            result += cour.name + " "
        return f"Teacher {self.name}, course: {result}"


class CourseFactory(ICourseFactory):
    def course_factory(self, name_course):
        with open("Course.json") as file_course:
            courses = json.load(file_course)
        selected_course = None
        for course in courses:
            if name_course == course["name"]:
                selected_course = course
        course_dict = {
            "OffsiteCourse": OffsiteCourse,
            "LocalCourse": LocalCourse
        }
        return course_dict[selected_course["type"]](selected_course["name"], selected_course["program"])

    def teacher_factory(self, name_teacher):
        with open("Teacher.json") as file_teacher:
            teachers = json.load(file_teacher)
        selected_teacher = None
        for teacher in teachers:
            if name_teacher == teacher["name"]:
                selected_teacher = teacher
        return Teacher(selected_teacher["name"])


def add(teacher, course):
    course.teacher = teacher
    teacher.add_course(course)


factory = CourseFactory()
teacher1 = factory.teacher_factory("Ivanov Ivan")
course = factory.course_factory("Python")
course2 = factory.course_factory("Java")
add(teacher1, course)
add(teacher1, course2)
print(course)
print(teacher1)
