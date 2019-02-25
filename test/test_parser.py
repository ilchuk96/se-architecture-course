from unittest import TestCase

from environment import Environment
from models import TextQuote
from models.cmd import Cmd, MetaCmd
from parser import Parser


class TestParser(TestCase):
    def test_empty(self):
        env = Environment()
        request = ""
        expected = Cmd('_nothing', [], env)
        self.assertEqual(expected, Parser(env).run(request))

    def test_assignment_operator(self):
        env = Environment()
        request = 'x=1'
        expected = Cmd('_assignment_operator', [TextQuote('1', '')], env)
        self.assertEqual(expected, Parser(env).run(request))

    def test_assignment_operator_for_value_in_quotes(self):
        env = Environment()
        request = "x='1'"
        expected = Cmd('_assignment_operator', [TextQuote('1', "'")], env)
        self.assertEqual(expected, Parser(env).run(request))

    def test_assignment_operator_for_value_in_double_quotes(self):
        env = Environment()
        request = 'x="1"'
        expected = Cmd('_assignment_operator', [TextQuote('1', '"')], env)
        self.assertEqual(expected, Parser(env).run(request))

    def test_exit(self):
        env = Environment()
        request = 'exit'
        expected = Cmd('exit', [], env)
        self.assertEqual(expected, Parser(env).run(request))

    def test_echo(self):
        env = Environment()
        request = 'echo Hello, world!'
        expected = Cmd('echo', [TextQuote("Hello,", ""), TextQuote("world!", "")], env)
        self.assertEqual(expected, Parser(env).run(request))


    def test_pip(self):
        env = Environment()
        request = 'exit | exit'
        first_cmd = Cmd('exit', [], env)
        second_cmd = Cmd('exit', [], env)
        expected = MetaCmd(first_cmd, second_cmd)
        self.assertEqual(expected, Parser(env).run(request))


