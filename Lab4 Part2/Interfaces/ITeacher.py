from abc import ABC, abstractmethod


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

    @abstractmethod
    def add_course(self, course): pass
