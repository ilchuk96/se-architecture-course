from environment import Environment
from parser import *


class App:
    '''
        App
    '''

    def __init__(self):
        self.env = Environment()

    def run(self):
        while not self.need_exit():
            self.before()
            line = input()
            root_cmd = Parser(self.env).run(line)
            root_cmd.run()

    def need_exit(self):
        return self.env.get_var('NEED_EXIT')

    def before(self):
        print(self.env.get_var('print_prefix'), end='')


if __name__ ==  "__main__":
    try:
        App().run()
    except:
        print("Something wrong")