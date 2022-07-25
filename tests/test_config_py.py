import pathlib
import unittest


class TestGettingFileName(unittest.TestCase):

    def test_import_func(self):
        try:
            from src.anagrams.config import get_in_file_name
        except ModuleNotFoundError:
            raise AssertionError
        except ImportError:
            raise AssertionError

    def test_right_select_file(self):
        from src.anagrams.config import get_in_file_name
        result = get_in_file_name(filetypes=(
                ('Text files', '*.TXT'),
                ('All files', '*.*'),
            ))

        self.assertIsInstance(result, pathlib.Path)
        self.assertNotEqual(result, pathlib.Path(''))

    def test_cancel_select_file(self):
        from src.anagrams.config import get_in_file_name
        result = get_in_file_name(filetypes=(
                ('Text files', '*.TXT'),
                ('All files', '*.*'),
            ))
        self.assertIsInstance(result, pathlib.Path)
        self.assertEqual(result, pathlib.Path(''))


if __name__ == '__main__':
    unittest.main()
