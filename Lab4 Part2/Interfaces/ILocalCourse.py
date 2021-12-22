from abc import ABC, abstractmethod


class ILocalCourse(ABC):
    @abstractmethod
    def __str__(self): pass