import json

from jsonschema import validate

from Classes.teacher import Teacher
from Constants import COURSE_FILE, COURSE_SCHEMA_FILE
from Interfaces.ICourse import ICourse


class Course(ICourse):
    """
    class describes a course
    Attributes:
    ----------
    name : str
        name of a course
    program: list
        program of the course
    """
    def __init__(self, name, program):
        self.name = name
        self.program = program
        self.teacher = []

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
        if not all(isinstance(teache, Teacher) for teache in teacher):
            raise TypeError("Wrong type of teacher!")
        self.__teacher = teacher

    def add_teacher(self, teach):
        if not isinstance(teach, Teacher):
            raise TypeError("Wrong type of teacher!")
        with open(COURSE_FILE) as file_course:
            courses = json.load(file_course)
        with open(COURSE_SCHEMA_FILE) as file_course_schema:
            course_schema = json.load(file_course_schema)
        for course in courses:
            if self.name == course["name"] and teach.name not in course["teacher"]:
                course["teacher"].append(teach.name)
        validate(courses, course_schema)
        with open(COURSE_FILE, "w") as file_course_to_json:
            json.dump(courses, file_course_to_json, indent=4)
        self.teacher.append(teach)

