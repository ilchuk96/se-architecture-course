from unittest import TestCase

from src.cmds.cmd import cd
from src.models import TextQuote
import os
from pathlib import Path


class TestCd(TestCase):
    def test_empty(self):
        lst = []
        cd(lst, None, None, None)
        self.assertEqual('/home', os.getcwd())

    def test_one_point(self):
        prev_dir = os.getcwd()
        lst = [TextQuote('.', None)]
        cd(lst, None, None, None)
        self.assertEqual(prev_dir, os.getcwd())

    def test_two_points(self):
        prev_dir = Path(os.getcwd()).parent
        lst = [TextQuote('..', None)]
        cd(lst, None, None, None)
        self.assertEqual(prev_dir, Path(os.getcwd()))

    def test_some_dir(self):
        directories = [directory for directory in os.listdir(os.getcwd())
                       if os.path.isdir(directory)]
        prev_dir = os.getcwd()
        if len(directories) > 0:
            lst = [TextQuote(directories[0], None)]
            cd(lst, None, None, None)
            self.assertEqual(Path(prev_dir), Path(os.getcwd()).parent)

    def test_no_such_dir(self):
        prev_dir = os.getcwd()
        lst = [TextQuote('__NO_SUCH_DIRECTORY__', None)]
        cd(lst, None, None, None)
        self.assertEqual(prev_dir, os.getcwd())
