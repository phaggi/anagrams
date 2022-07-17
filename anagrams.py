from itertools import permutations
from pathlib import Path
from configs import NounsConfig


class Nouns:
    def __init__(self, nouns_file=None):
        if nouns_file is None:
            self.nouns_file = Path(NounsConfig().load()[NounsConfig().nouns_file_path_key])
        else:
            self.nouns_file = nouns_file
        self.full_nouns = None
        self.set_full_nouns()

    def set_full_nouns(self):
        try:
            with open(self.nouns_file, 'rb') as nouns_obj:
                target = nouns_obj.read().decode("UTF-8").splitlines()
                self.full_nouns = set(target)
        except FileNotFoundError:
            print(f'Файл {self.nouns_file} не найден.')


class Vocabulary:
    word = None
    input_text = 'Введите русское слово существительное:'
    nouns = None

    def __init__(self, full_nouns):
        self.full_nouns = full_nouns

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
    nouns = Nouns().full_nouns
    voc = Vocabulary(nouns)
    print('\n'.join(sorted(list(voc.find_anagrams()))))
