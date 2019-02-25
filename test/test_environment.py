from unittest import TestCase

from environment import Environment


class TestEnvironment(TestCase):
    def test_get_cmd(self):
        env = Environment(dict_of_cmds={'key': 'value'})
        self.assertEqual('value', env.get_cmd('key'))

    def test_get_cmd_with_no_existing_key(self):
        env = Environment()
        self.assertRaises(KeyError, lambda x: env.get_cmd(x), 'key')

    def test_get_var(self):
        env = Environment(dict_of_vars={'key': 'value'})
        self.assertEqual('value', env.get_var('key'))

    def test_get_var_with_no_existing_key(self):
        env = Environment()
        self.assertRaises(KeyError, lambda x: env.get_var(x), 'key')


    def test_set_var(self):
        env = Environment()
        env.set_var('key', 'value')
        self.assertEqual('value', env.get_var('key'))
