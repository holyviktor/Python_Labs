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
        self.name = name
        self.surname = surname
        self.num_of_book = num_of_book
        self.grades = grades

    @property
    def name(self):
        """Name of student"""
        return self.__name

    @name.setter
    def name(self, name):
        """Sets name of student"""
        if not isinstance(name, str):
            raise TypeError("Wrong type of name!")
        if not name:
            raise ValueError("Wrong value of name!")
        self.__name = name

    @property
    def surname(self):
        """Surname of student"""
        return self.__surname

    @surname.setter
    def surname(self, surname):
        """Sets surname of student"""
        if not isinstance(surname, str):
            raise TypeError("Wrong type of surname!")
        if not surname:
            raise ValueError("Wrong value of surname!")
        self.__surname = surname

    @property
    def num_of_book(self):
        """Number of student's book"""
        return self.__num_of_book

    @num_of_book.setter
    def num_of_book(self, num_of_book):
        """Sets number of student's book"""
        if not isinstance(num_of_book, int):
            raise TypeError("Wrong type of number of book!")
        if num_of_book <= 0:
            raise ValueError("Wrong value of book!")
        self.__num_of_book = num_of_book

    @property
    def grades(self):
        """Massive of student's grades"""
        return self.__grades

    @grades.setter
    def grades(self, grades):
        """Sets a massive of student's grades"""
        if not all([isinstance(grade, int) for grade in grades]):
            raise TypeError("Wrong type of grades!")
        if not grades or not all([60 <= grade <= 100 for grade in grades]):
            raise ValueError("Wrong value of grades!")
        self.__grades = grades

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

    def __str__(self):
        return f"{self.name} {self.surname}"

    def add_grade(self, grade):
        if not isinstance(grade, int):
            raise TypeError("Wrong type of grade!")
        if not grade or not 60 <= grade <= 100:
            raise ValueError("Wrong value of grade!")
        self.grades.add(grade)

    def delete_grade(self, grade):
        if not isinstance(grade, int):
            raise TypeError("Wrong type of grade!")
        if not grade or not 60 <= grade <= 100:
            raise ValueError("Wrong value of grade!")
        self.grades.remove(grade)


class Group:
    """class describes a group of students.
        Attributes:
        -----------
        students : Student[]
            all students in a group
        Methods:
        -------
        find_highest(self):
            finds 5 highest students for their score
        """
    def __init__(self, students):
        """Sets all required attributes for the group object.
        Options:
        -------
        students : Student[]
            all students in a group
        """
        self.students = students

    def find_highest(self):
        """finds students with the highest average score
        sorts students by their score and writes 5 students with the biggest score to the massive
        returns 5 students with the highest average score"""
        self.students = sorted(self.students, reverse=True)
        return self.students[:5]

    def add_student(self, student):
        """Add new student in a group"""
        if not student:
            ValueError("Wrong value of data!")
        if not isinstance(student, Student):
            TypeError("Wrong type of product!")
        self.students.add(student)

    def delete_student(self, student):
        """Delete a student in a group"""
        if not student:
            ValueError("Wrong value of data!")
        if not isinstance(student, Student):
            TypeError("Wrong type of product!")
        self.students.remove(student)

    @property
    def students(self):
        """All students in a group"""
        return self.__students

    @students.setter
    def students(self, students):
        """Sets a massive of students"""
        if not all([isinstance(stud, Student) for stud in students]):
            raise TypeError("Wrong type of object!")
        if len(students) > 20:
            raise ValueError("Wrong value!")
        self.__students = students


student1 = Student("Victoria", "Lys", 12345, {100, 99, 98, 95})
student2 = Student("Ivan", "Ivanov", 34568, {70, 80, 90, 60})
student3 = Student("Petro", "Petrov", 87654, {81, 94, 76, 65})
student4 = Student("Katya", "Abcde", 26345, {66, 98, 63, 77})
student5 = Student("Denys", "Bas", 25638, {98, 89, 90, 91})
student6 = Student("Volodymyr", "Hello", 67543, {66, 100, 95, 70})
student7 = Student("Arina", "Hi", 45678, {86, 60, 66, 86})
group1 = Group({student1, student2, student3, student4, student5, student6, student7})
for stud in group1.find_highest():
    print(stud)

