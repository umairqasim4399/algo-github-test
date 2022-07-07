import json
from parse import *
from copy import *
def functional() -> (list,):
    functional_commands = []
    counter = 0

    parse_commands = parse()
    copy_commands = copy()

    for row in parse_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)

    counter = 0
    for row in copy_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    print(f"functional_commands: {functional_commands}")