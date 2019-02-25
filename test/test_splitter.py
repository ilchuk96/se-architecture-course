from unittest import TestCase

from models import TextQuote
from splitter import Splitter


class TestSplitter(TestCase):
    def test_empty_line(self):
        request = ""
        result = []
        self.assertEqual(Splitter().run(request), result)

    def test_one_word(self):
        request = "echo"
        result = [TextQuote(request, '')]
        self.assertEqual(Splitter().run(request), result)

    def test_one_word_with_pipe(self):
        request = "exit | exit"
        result = [TextQuote(request, '')]
        self.assertEqual(Splitter().run(request), result)

    def test_separate_by_pipe(self):
        additional_delimiters = '|'
        request = "exit | exit"
        result = [TextQuote('exit ', '|'), TextQuote(' exit', '')]
        self.assertEqual(Splitter().run(request, additional_delimiters), result)

    def test_echo_with_quote(self):
        request = "echo 'Hello, world!'"
        result = [TextQuote('echo ', ''), TextQuote('Hello, world!', "'")]
        self.assertEqual(Splitter().run(request), result)

    def test_echo_with_double_quote(self):
        request = 'echo "Hello, world!"'
        result = [TextQuote('echo ', ''), TextQuote('Hello, world!', '"')]
        self.assertEqual(Splitter().run(request), result)


