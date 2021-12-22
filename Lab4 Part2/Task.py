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

from Classes.course_factory import CourseFactory


def add(teacher, course):
    """
    :param teacher: teacher to add to the course
    :param course: course to add to the teacher
    adds teacher to the course and course to the teacher
    """
    course.add_teacher(teacher)
    teacher.add_course(course)


def main():
    factory = CourseFactory()
    teacher1 = factory.teacher_factory("Ivanov Ivan")
    course = factory.course_factory("Python")
    course2 = factory.course_factory("Java")
    add(teacher1, course)
    add(teacher1, course2)
    print(teacher1)
    for t in teacher1:
        print(t)


if __name__ == '__main__':
    main()

