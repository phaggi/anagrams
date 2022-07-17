from itertools import *
from pprint import pformat


class Vocabulary:
    word = None
    input_text = 'Введите русское слово существительное:'
    nouns = None
    full_nouns = None

    def __init__(self, nouns_file=None):
        if nouns_file is None:
            self.nouns_file = 'russian_nouns.txt'
        self.get_full_nouns()

    def get_full_nouns(self):
        with open(self.nouns_file, 'rb') as rusnouns:
            target = rusnouns.read().decode("UTF-8")
            target = target.splitlines()
            self.full_nouns = set(target)

    def set_word(self):
        while self.word not in self.full_nouns:
            self.word = input(self.input_text).lower()

    def set_nouns(self):
        self.nouns = {item for item in self.full_nouns if len(item) == len(self.word)}

    def find_anagrams(self) -> set:
        self.set_word()
        self.set_nouns()
        return {''.join(i) for i in permutations(list(self.word))} & self.nouns


if __name__ == '__main__':
    voc = Vocabulary()
    print('\n'.join(sorted(list(voc.find_anagrams()))))
