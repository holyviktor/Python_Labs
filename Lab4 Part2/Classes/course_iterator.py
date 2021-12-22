class CoursesIterator:
    """Class describes an iterator
    Attributes:
    ----------
    wrapped: list
        list to iterate
    index: int
        index of list
    """
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.wrapped):
            raise StopIteration()
        self.index += 1
        return self.wrapped[self.index - 1]