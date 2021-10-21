class Student:
    """
    class describes a student.
    Attributes:
    -----------
    name : str
        name of student
    surname : str
        surname of student
    num_of_book : int
        number of student's book
    grades : int[]
        massive of student's grades
    Methods:
    -------
    find_average_score(self):
        finds average score of student's grades
    """
    def __init__(self, name, surname, num_of_book, grades):
        """
        Sets all required attributes for the student object.
        Options
        ---------
        name : str
            name of student
        surname : str
            surname of student
        num_of_book : int
            number of student's book
        grades : int[]
            massive of student's grades
        """
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError("Wrong type of full name!")
        if not isinstance(num_of_book, int):
            raise TypeError("Wrong type of number of book!")
        if num_of_book <= 0:
            raise ValueError("Wrong value of book!")
        if not all([isinstance(grade, int) for grade in grades]):
            raise TypeError("Wrong type of grades!")
        if not all([60 <= grade <= 100 for grade in grades]):
            raise ValueError("Wrong value of grades!")
        self.name = name
        self.surname = surname
        self.num_of_book = num_of_book
        self.grades = grades

    def find_average_score(self):
        """finds average score of student by division summa of grades by the number
        returns average score of student"""
        return sum(self.grades) / len(self.grades)

    def __lt__(self, other):
        """
        implement a "less than" check for instances
        returns boolean value as a result of check
        """
        return self.find_average_score() < other.find_average_score()


class Group:
    """class describes a group of students.
        Attributes:
        -----------
        students : tuple
            all students in a group
        Methods:
        -------
        find_highest(self):
            finds 5 highest students for their score
        """
    def __init__(self, *students):
        """Sets all required attributes for the group object.
        Options:
        -------
        students : tuple
            all students in a group
        """
        if not all([isinstance(stud, Student) for stud in students]):
            raise TypeError("Wrong type of object!")
        if len(students) > 20:
            raise ValueError("Wrong value!")
        self.students = students

    def find_highest(self):
        """finds students with the highest average score
        sorts students by their score and writes 5 students with the biggest score to the massive
        returns 5 students with the highest average score"""
        marks = []
        self.students = sorted(self.students, reverse=True)
        for i in range(5):
            marks.append(self.students[i].surname + ' ' + self.students[i].name)
        return marks


student1 = Student("Victoria", "Lys", 12345, {100, 99, 98, 95})
student2 = Student("Ivan", "Ivanov", 34568, {70, 80, 90, 60})
student3 = Student("Petro", "Petrov", 87654, {81, 94, 76, 65})
student4 = Student("Katya", "Abcde", 26345, {66, 98, 63, 77})
student5 = Student("Denys", "Bas", 25638, {98, 89, 90, 91})
student6 = Student("Volodymyr", "Hello", 67543, {66, 100, 95, 70})
student7 = Student("Arina", "Hi", 45678, {86, 60, 66, 86})
group1 = Group(student1, student2, student3, student4, student5, student6, student7)
print(group1.find_highest())
