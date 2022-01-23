import random

import argh
import blessed


def go(filename, resume_line=0, shuffle=True):
    term = blessed.Terminal()

    lines = [
        line.strip()
        for line in open(filename).readlines()
        if line.strip() and len(line) < term.width - 6
    ]
    if shuffle:
        random.shuffle(lines)
    line_num = resume_line
    userline = list()
    userkey = 0

    while True:
        print(term.home + term.clear)
        line = lines[line_num]
        with term.location(term.width // 2 - len(line) // 2, term.height // 2 - 1):
            print(line)
        with term.location(term.width // 2 - len(line) // 2 - 2, term.height // 2 + 1):
            print("> " + "".join(userline) + "_")
        with term.cbreak(), term.hidden_cursor():
            inp = term.inkey()

        if inp.name == "KEY_ENTER":
            if "".join(userline) == line:
                userline = list()
                line_num += 1
            if line_num >= len(lines):
                line_num = 0
            userkey = 0
        elif inp.name == "KEY_ESCAPE":
            print(term.clear)
            print(f"Line index: {line_num}.")
            break
        elif len(line) >= userkey + 1 and inp == line[userkey]:
            userline.append(inp)
            userkey += 1


if __name__ == "__main__":
    argh.dispatch_command(go)
