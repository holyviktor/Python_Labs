from abc import ABC, abstractmethod


class IOffsiteCourse(ABC):
    @abstractmethod
    def __str__(self): pass
