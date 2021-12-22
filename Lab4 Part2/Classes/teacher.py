import json

from jsonschema import validate

from Classes.course_iterator import CoursesIterator
from Constants import TEACHER_FILE, TEACHER_SCHEMA_FILE
from Interfaces.ITeacher import ITeacher


class Teacher(ITeacher):
    """
        class describes a teacher
        Attributes:
        ----------
        name : str
            name of the teacher
        course: list
            list with courses
        """
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
        from Classes.offsite_course import OffsiteCourse
        from Classes.local_course import LocalCourse
        if not all(isinstance(cours, (OffsiteCourse, LocalCourse)) for cours in course):
            raise TypeError("Wrong type of course")
        self.__course = course

    def add_course(self, cour):
        from Classes.offsite_course import OffsiteCourse
        from Classes.local_course import LocalCourse
        if not isinstance(cour, (OffsiteCourse, LocalCourse)):
            raise TypeError("Wrong type of course!")
        with open(TEACHER_FILE) as file_teacher:
            teachers = json.load(file_teacher)
        with open(TEACHER_SCHEMA_FILE) as file_teacher_schema:
            teacher_schema = json.load(file_teacher_schema)
        for teach in teachers:
            if self.name == teach["name"] and cour.name not in teach["course"]:
                teach["course"].append(cour.name)
        validate(teachers, teacher_schema)
        with open(TEACHER_FILE, "w") as file_teacher_to_json:
            json.dump(teachers, file_teacher_to_json, indent=4)
        self.course.append(cour)

    def __str__(self):
        result = ""
        for cour in self.course:
            result += cour.name + " "
        return f"Teacher {self.name}, course: {result}"

    def __iter__(self):
        return CoursesIterator(self.course)
