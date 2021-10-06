import re


class Text:
    def __init__(self):
        self.characters = 0
        self.words = 0
        self.sentences = 0
        try:
            self.file = open('text.txt', encoding='utf-8')
        except IOError:
            print("No such file!")
            exit(1)

    def counting(self):
        data = self.file.read()
        self.characters = len(data)
        self.sentences = len(re.split('\. |\? |! |\... ', data)) - 1
        self.words = len(data.split())

    def show_on_console(self):
        print("Characters: ", self.characters)
        print("Words: ", self.words)
        print("Sentences: ", self.sentences)

    def closing(self):
        try:
            self.file.close()
        except IOError:
            raise IOError("Failed to close!")


text = Text()
text.counting()
text.show_on_console()
text.closing()
