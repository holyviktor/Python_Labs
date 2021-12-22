from abc import abstractmethod, ABC


class ICourseFactory(ABC):
    @abstractmethod
    def course_factory(self, name_course):
        pass

    @abstractmethod
    def teacher_factory(self, name_teacher):
        pass