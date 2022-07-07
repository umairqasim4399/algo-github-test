import json
def copy() -> list:
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    copy_commands = [row for row in data if row['function']=='function' and row['function'] == 'copy']
    # for row in data:
    #     if 'function' in row and row['function'] == 'copy':
    #         copy_commands.append(row.copy())
    # print(f"copy_commands: {copy_commands}")

    return copy_commands