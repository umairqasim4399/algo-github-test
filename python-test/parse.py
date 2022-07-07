import json

def parse() -> list:
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_commands = [row for row in data if row['function']=='function' and row['function' == parse]]
    # for row in data:
    #     if 'function' in row and row['function'] == 'parse':
    #         parse_commands.append(row.copy())
    # print(f"parse_commands: {parse_commands}")

    return parse_commands