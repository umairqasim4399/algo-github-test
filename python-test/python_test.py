import json
from RandomCommads import *
from functonal import *
from parse import *
from copy import *


def main() -> (dict, dict, dict, dict,):
    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list

    copy_commands = copy()
    parse_commands = parse()
    functional_commands = functional()
    random_commands = RandomCommands()

    return parse_commands, copy_commands, functional_commands, random_commands


if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
