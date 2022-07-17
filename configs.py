import toml
from pathlib import Path
from pprint import pformat
import tkinter as tk
from tkinter import filedialog


def get_in_file_name(filetypes=None) -> Path:
    """

    :param filetypes: tuple, default value = (
            ('Text files', '*.TXT'),
            ('All files', '*.*'),
            )
    :return:
    """
    if filetypes is None:
        filetypes = (
            ('Text files', '*.TXT'),
            ('All files', '*.*'),
        )
    root = tk.Tk()
    root.withdraw()
    filename = Path(tk.filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,
    ))
    root.destroy()
    return filename

class Config:
    def __init__(self):
        self.config_name = 'config.toml'
        self.config_path = Path(self.config_name)

    def load(self):
        with open(self.config_path, 'r') as in_file:
            return toml.loads(in_file.read())

    def save(self, raw_config):
        with open(self.config_path, 'w') as out_file:
            toml.dump(raw_config, out_file)

    def add(self, raw_config: dict):
        old_config = self.load()
        old_config.update(raw_config)
        self.save(old_config)

    def __repr__(self):
        return pformat(self.load())


class NounsConfig(Config):
    def __init__(self):
        super().__init__()
        if not self.config_path.exists():
            self.save({'nouns_file_path': "../russian_nouns.txt"})
        self.nouns_config = self.config_path
        self.nouns_file_path_key = 'nouns_file_path'
        self.nouns_file_path = self.load()[self.nouns_file_path_key]
        self.test_nouns_file_path()

    def test_nouns_file_path(self):
        if not Path(self.nouns_file_path).is_file():
            self.save({self.nouns_file_path_key: str(get_in_file_name())})




if __name__ == '__main__':
    config = NounsConfig()
    print(Path(config.nouns_file_path).is_file())
