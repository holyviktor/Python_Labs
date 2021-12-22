import json

from jsonschema import validate

from Classes.local_course import LocalCourse
from Classes.offsite_course import OffsiteCourse
from Classes.teacher import Teacher
from Constants import COURSE_FILE, COURSE_SCHEMA_FILE, TEACHER_FILE
from Interfaces.ICourseFactory import ICourseFactory


class CourseFactory(ICourseFactory):
    """
    class describes a factory of course
    Methods:
    -------
    course_factory:
        @:param: name_course: str
        @:returns: new instance of class OffsiteCourse or LocalCourse
    teacher_factory:
        @:param: name_course: str
        @:returns: new instance of class Teacher
    """
    def course_factory(self, name_course):
        with open(COURSE_FILE) as file_course:
            courses = json.load(file_course)
        with open(COURSE_SCHEMA_FILE) as file_course_schema:
            course_schema = json.load(file_course_schema)
        validate(courses, course_schema)
        selected_course = None
        for course in courses:
            if name_course == course["name"]:
                selected_course = course
        if selected_course is None:
            raise ValueError("No courses with such name!")
        course_dict = {
            "OffsiteCourse": OffsiteCourse,
            "LocalCourse": LocalCourse
        }
        return course_dict[selected_course["type"]](selected_course["name"], selected_course["program"])

    def teacher_factory(self, name_teacher):
        with open(TEACHER_FILE) as file_teacher:
            teachers = json.load(file_teacher)
        with open(COURSE_SCHEMA_FILE) as file_teacher_schema:
            teacher_schema = json.load(file_teacher_schema)
        validate(teachers, teacher_schema)
        selected_teacher = None
        for teacher in teachers:
            if name_teacher == teacher["name"]:
                selected_teacher = teacher
        if selected_teacher is None:
            raise ValueError("No teacher with such name!")
        return Teacher(selected_teacher["name"])

