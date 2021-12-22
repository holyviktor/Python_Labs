from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, name): pass

    @property
    @abstractmethod
    def program(self): pass

    @program.setter
    @abstractmethod
    def program(self, program): pass

    @abstractmethod
    def add_teacher(self, teacher): pass