from Classes.course import Course
from Interfaces.IOffsiteCourse import IOffsiteCourse


class OffsiteCourse(Course, IOffsiteCourse):
    """
        class describes an offsite course
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
        return f"Offsite course {self.name}, teacher: {result}, program: {self.program}"
