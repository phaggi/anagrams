from itertools import permutations
from pathlib import Path
from src.anagrams.config import NounsConfig


class Nouns:
    def __init__(self, nouns_file=None):
        if nouns_file is None:
            self.nouns_file = Path(NounsConfig().load()[NounsConfig().nouns_file_path_key])
        else:
            self.nouns_file = nouns_file
        self.full_nouns = None
        self.set_full_nouns()

    def set_full_nouns(self):
        """
        make self.full_nouns set from TXT (self.nouns_file)
        :return:
        """
        try:
            with open(self.nouns_file, 'rb') as nouns_obj:
                target = nouns_obj.read().decode("UTF-8").splitlines()
                self.full_nouns = set(target)
        except FileNotFoundError:
            print(f'Файл {self.nouns_file} не найден.')


class Vocabulary:
    input_text = 'Введите русское слово существительное:'

    def __init__(self, full_nouns=None):
        self.nouns = None
        self.word = None
        if full_nouns is None:
            self.full_nouns = Nouns().full_nouns
        else:
            self.full_nouns = full_nouns

    def set_word(self):
        """
        make correct self.word from parameter or input
        :return:
        """
        while self.word not in self.full_nouns and self.word != '':
            self.word = input(self.input_text).lower()

    def set_nouns(self):
        """
        make self.nouns from words with length as a word length
        :return:
        """
        self.nouns = {item for item in self.full_nouns if len(item) == len(self.word)}

    def find_anagrams(self, word: str = None) -> set:
        """
        find an anagrams to the 'word' in the dictionary (self.nouns)
        :param word:
        :return:
        """
        if word is None and self.word != '':
            self.set_word()
        elif word.isalpha() and word.lower() in self.full_nouns:
            self.word = word.lower()
        if self.word == '':
            raise Exception('Конец работы.')
        self.set_nouns()
        anagrams = {''.join(i) for i in permutations(list(self.word))} & self.nouns
        self.word = None
        return anagrams


def print_anagrams(anagrams: set):
    """
    print sorted set of anagrams by row
    :param anagrams:
    :return:
    """
    print('\n'.join(sorted(list(anagrams))))


def find_anagrams(word: str = None, cycle: bool = False):
    """

    :param word: str russian noun word.
    :param cycle: bool if True, anagrams will work until operator send empty string.
    If empty string, will raise exception.
    :return: print anagrams for word.
    """
    voc = Vocabulary()
    if word is not None:
        print_anagrams(voc.find_anagrams(word))
    else:
        print_anagrams(voc.find_anagrams())
        while cycle:
            print_anagrams(voc.find_anagrams())


if __name__ == '__main__':
    find_anagrams('столик')
    find_anagrams()
    find_anagrams(cycle=True)
