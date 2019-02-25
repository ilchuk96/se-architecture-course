from unittest import TestCase

from environment import Environment
from expander import Expander
from models import TextQuote


class TestExpander(TestCase):

    def test_empty(self):
        env = Environment()
        expander = Expander(env)
        request = ""
        expected = []
        self.assertEqual(expected, expander.run(request))

    def test_without_expand(self):
        env = Environment()
        expander = Expander(env)
        request = "echo"
        expected = [TextQuote(request, '')]
        self.assertEqual(expected, expander.run(request))


    def test_only_a_var(self):
        env = Environment(dict_of_vars={'var': '1'})
        expander = Expander(env)
        request = "$var"
        expected = [TextQuote('1', '')]
        self.assertEqual(expected, expander.run(request))

    def test_echo_quote_var(self):
        env = Environment(dict_of_vars={'var': '1'})
        expander = Expander(env)
        request = "echo '$var'"
        expected = [TextQuote('echo ', ''), TextQuote('$var', "'")]
        self.assertEqual(expected, expander.run(request))

    def test_echo_double_quote_var(self):
        env = Environment(dict_of_vars={'var': '1'})
        expander = Expander(env)
        request = 'echo "$var"'
        expected = [TextQuote('echo ', ''), TextQuote('1', '"')]
        self.assertEqual(expected, expander.run(request))

    def test_get_cmd_from_two_var(self):
        env = Environment(dict_of_vars={'x': 'ex', 'y': 'it'})
        expander = Expander(env)
        request = '$x$y'
        expected = [TextQuote('exit', '')]
        self.assertEqual(expected, expander.run(request))
