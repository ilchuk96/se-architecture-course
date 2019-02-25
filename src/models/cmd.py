import sys
import io


class Cmd:
    '''
        Cmd
    '''
    def __init__(self, name, parameters, env):
        self.name = name
        self.parameters = parameters
        self.env = env
        self.input_stream = sys.stdin
        self.output_stream = sys.stdout

    def run(self):
        self.env.get_cmd(self.name)(self.parameters,
                                    self.input_stream,
                                    self.output_stream,
                                    self.env)

    def __eq__(self, other):
        result = True
        result &= self.name == other.name
        result &= self.parameters == other.parameters
        result &= self.env == other.env
        result &= self.input_stream == other.input_stream
        result &= self.output_stream == other.output_stream
        return result

    def __repr__(self):
        res = "Cmd: (name: {}, parameters: {}, env: {}, input_stream: {}, output_stream {})".format(
            self.name,
            self.parameters,
            self.env,
            self.input_stream,
            self.output_stream
        )
        return res



class MetaCmd:
    '''
        MetaCmd
    '''

    def __init__(self, first_cmd, second_cmd):
        self.first_cmd = first_cmd
        self.second_cmd = second_cmd
        self.input_stream = sys.stdin
        self.output_stream = sys.stdout

    def run(self):
        stream = io.StringIO()
        self.first_cmd.output_stream = stream
        self.second_cmd.input_stream = stream
        self.first_cmd.run()
        self.second_cmd.run()

    def __eq__(self, other):
        result = True
        result &= self.first_cmd == other.first_cmd
        result &= self.second_cmd == other.second_cmd
        result &= self.input_stream == other.input_stream
        result &= self.output_stream == other.output_stream
        return result
