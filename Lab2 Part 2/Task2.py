import re


class Text:
    def __init__(self):
        self.characters = 0
        self.words = 0
        self.sentences = 0

    def counting_characters(self):
        try:
            file = open('text.txt', "r", encoding='utf-8')
            data = file.read()
            self.characters = len(data)
            file.close()
        except IOError:
            raise IOError("Failed!")
        return self.characters

    def counting_sentences(self):
        try:
            file = open('text.txt', "r", encoding='utf-8')
            file.seek(0)
            data = file.read()
            self.sentences = len(re.split('\. |\? |! |\... ', data)) - 1
            file.close()
        except IOError:
            raise IOError("Failed!")
        return self.sentences

    def counting_words(self):
        try:
            file = open('text.txt', "r", encoding='utf-8')
            file.seek(0)
            data = file.read()
            self.words = len(data.split())
            file.close()
        except IOError:
            raise IOError("Failed!")
        return self.words


text = Text()
print("Characters: ", text.counting_characters())
print("Words: ", text.counting_words())
print("Sentences: ", text.counting_sentences())
