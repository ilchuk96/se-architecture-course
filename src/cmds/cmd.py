def cat(parameters, input_stream, output_stream, env):
    for text, qoute in parameters:
        with open(text, 'r') as file_in:
            print(file_in.read(), file=output_stream, end='')

def echo(parameters, input_stream, output_stream, env):
    print(*[e.text for e in parameters], file=output_stream)

def exit(parameters, input_stream, output_stream, env):
    env.set_var('NEED_EXIT', True)

def wc(parameters, input_stream, output_stream, env):

    def print_info(text):
        print("{} {} {}".format(
                                len(text.split('\n')) - 1,
                                len(text.split(' ')),
                                len(text) - 1),
              file=output_stream
        )

    if parameters:
        for name_file, quote in parameters:
            with open(name_file, 'r') as file_in:
                text = file_in.read()
                print_info(text)
    else:
        text = input_stream.read()
        print_info(text)


def pwd(parameters, input_stream, output_stream, env):
    import os
    print(os.getcwd(), file=output_stream)
