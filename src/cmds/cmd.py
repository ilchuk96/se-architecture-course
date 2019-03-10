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


def cd(parameters, input_stream, output_stream, env):
    import os
    if len(parameters) > 1:
        print("cd: too many arguments", file=output_stream)
        return
    if len(parameters) == 0:
        # should do to /home/CUR_USER actually
        os.chdir('/home')
        return
    try:
        os.chdir(parameters[0].text)
    except Exception as e:
        print(e, file=output_stream)


def ls(parameters, input_stream, output_stream, env):
    import os

    def print_dir(path):
        answer = [file for file in os.listdir(path)]
        print(" ".join(answer), file=output_stream)

    if len(parameters) == 0:
        ans = [file for file in os.listdir(os.getcwd())]
        print(" ".join(ans), file=output_stream)
        return
    if len(parameters) == 1:
        try:
            print_dir(parameters[0].text)
        except Exception as e:
            print(e, file=output_stream)
        return
    for i, directory in enumerate(parameters):
        try:
            print(directory.text + ":", file=output_stream)
            print_dir(directory.text)
            if i != len(parameters) - 1:
                print("", file=output_stream)
        except Exception as e:
            print(e, file=output_stream)
