

def _assignment_operator(parameters, input_stream, output_stream, env):
    env.set_var(parameters[0].text, parameters[1].text)


def _nothing(parameters, input_stream, output_stream, env):
    return