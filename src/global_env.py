from cmds.cmd import *
from cmds.grep import Grep
from cmds.internal_cmd import _nothing, _assignment_operator

DICT_OF_CMDS = {
    'cat': cat,
    'exit': exit,
    'echo': echo,
    'wc': wc,
    'pwd': pwd,
    'grep': Grep(),
    '_assignment_operator': _assignment_operator,
    '_nothing': _nothing
}

DICT_OF_VARS = {
    'NEED_EXIT': False,
    'print_prefix': ">> "
    #'test_file': "/home/raf/tmp/code.hs" # need for debug. delete in release
}

