import argparse
import re

class GrepRun:
    def __call__(self, input_stream, output_stream):
        if not self.word:
            raise RuntimeError("grep doesn't have a word")
        result = ""
        if self.file:
            with open(self.file, 'r') as file_in:
                text = file_in.read()
                result = self.search(text)
        else:
            text = input_stream.read()
            result = self.search(text)
        print(result, file=output_stream)


    def search(self, text):
        result = []
        count = 0
        for line in text.split('\n'):
            count = max(count - 1, 0)
            if count > 0:
                result.append(line)
                continue

            flags = re.I if self.case_letters_important else 0
            pattern = self.word
            if self.whole_word:
                pattern = " {} ".format(pattern)
            success = re.search(self.word, line, flags=flags)
            if success:
                result.append(line)
                count = self.num_of_print_lines

        return "\n".join(result)



class Grep:
    def __init__(self):
        parser = argparse.ArgumentParser()
        self.parser = parser
        parser.add_argument('word', nargs='?', type=str, default=None)
        parser.add_argument('file', nargs='?', default=None)
        parser.add_argument('-i', action='store_false', dest='case_letters_important')
        parser.add_argument('-w', action='store_true', dest='whole_word')
        parser.add_argument('-A', nargs='?', type=int, dest='num_of_print_lines', default=1)

    def __call__(self, parameters, input_stream, output_stream, env):
        parameters = [text for text, quote in parameters]
        grep_run = GrepRun()
        self.parser.parse_args(parameters, namespace=grep_run)
        grep_run(input_stream, output_stream)

