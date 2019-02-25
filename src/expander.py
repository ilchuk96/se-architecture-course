from models import TextQuote
from splitter import Splitter


class Expander:
    '''
        Expander
    '''

    def __init__(self, env):
        self.env = env

    def run(self, line):
        list_of_textquote = Splitter().run(line)
        result = list()
        for text, quote in list_of_textquote:
            if quote != "'":
                result.append(TextQuote(self.expansion(text), quote))
            else:
                result.append(TextQuote(text, quote))
        return result


    def expansion(self, text):
        result = list()
        for word in text.split(' '):
            if word and word[0] == '$':
                empty, *vars = word.split('$')
                word = "".join([self.env.get_var(var) for var in vars])
            result.append(word)
        return " ".join(result)


