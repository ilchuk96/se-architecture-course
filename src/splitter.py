from models import TextQuote


class Splitter:
    '''
        Splitter
    '''

    def run(self, line, additional_delimiters=""):
        was_quote = False
        was_double_quote = False
        begin_data = 0
        result = []
        for index, symbol in enumerate(line):

            if not was_double_quote and symbol == "'":
                quote = symbol if was_quote else ""
                result.append(TextQuote(line[begin_data:index], quote))
                begin_data = index + 1
                was_quote = not was_quote

            if not was_quote and symbol == '"':
                quote = symbol if was_double_quote else ""
                result.append(TextQuote(line[begin_data:index], quote))
                begin_data = index + 1
                was_double_quote = not was_double_quote

            if not was_quote and not was_double_quote and \
                    symbol in additional_delimiters:
                result.append(TextQuote(line[begin_data:index], symbol))
                begin_data = index + 1

        if begin_data != len(line):
            result.append(TextQuote(line[begin_data:], ""))
            begin_data = index + 1


        return result

