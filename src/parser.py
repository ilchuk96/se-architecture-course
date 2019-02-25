from expander import Expander
from models import TextQuote
from models.cmd import Cmd, MetaCmd
from splitter import Splitter


class Parser:
    '''
        Parser
    '''

    def __init__(self, env):
        self.env = env

    def run(self, line):
        list_of_textquote = Expander(self.env).run(line)
        list_of_tokens = list()

        for text, quote in list_of_textquote:
            if quote != '':
                list_of_tokens.append(TextQuote(text, quote))
            else:
                for text in text.split('|'):
                    for element in text.split():
                        list_of_tokens.append(TextQuote(element, ""))
                    list_of_tokens.append(TextQuote("", "|"))
                else:
                    del list_of_tokens[-1]

        tokens_group_by_pipe = []
        one_group = []
        for token in list_of_tokens:
            if token.quote != '|':
                one_group.append(token)
            else:
                tokens_group_by_pipe.append(one_group)
                one_group = []

        if one_group:
            tokens_group_by_pipe.append(one_group)

        root_cmd = None
        for group in tokens_group_by_pipe:
            name_of_cmd, *parameters = group
            if name_of_cmd.quote == "'" or name_of_cmd.quote == '"':
                raise RuntimeError("Cmd is in quotes")
            if '=' in name_of_cmd.text:
                var, value = name_of_cmd.text.split('=', 1)
                if value:
                   parameters = [TextQuote(var, name_of_cmd.quote),
                                 TextQuote(value, name_of_cmd.quote)] + parameters
                else:
                    parameters = [TextQuote(var, name_of_cmd.quote)] + parameters
                cmd = Cmd('_assignment_operator', parameters, self.env)
            else:
                cmd = Cmd(name_of_cmd.text, parameters, self.env)

            root_cmd = cmd if root_cmd is None else MetaCmd(root_cmd, cmd)

        root_cmd = root_cmd if root_cmd else Cmd('_nothing', [], self.env)
        return root_cmd

