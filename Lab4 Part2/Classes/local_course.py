from Classes.course import Course
from Interfaces.ILocalCourse import ILocalCourse


class LocalCourse(Course, ILocalCourse):
    """
        class describes a local course
        Attributes:
        ----------
        name : str
            name of a course
        program: list
            program of the course
        """
    def __init__(self, name, program):
        super().__init__(name, program)

    def __str__(self):
        result = ""
        for t in self.teacher:
            result += t.name + " "
        return f"Local course {self.name}, teacher: {result}, program: {self.program}"

