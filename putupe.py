import argh
import blessed


def go(filename, resume_line=0):
    term = blessed.Terminal()

    lines = [line.strip() for line in open(filename).readlines() if line.strip()]
    line_num = resume_line
    userline = list()

    while True:
        print(term.home + term.clear)
        line = lines[line_num]
        with term.location(term.width // 2 - len(line) // 2, term.height // 2 - 1):
            print(line)
        with term.location(term.width // 2 - len(line) // 2 - 2, term.height // 2 + 1):
            print("> " + "".join(userline) + "_")
        with term.cbreak(), term.hidden_cursor():
            inp = term.inkey()

        if inp.name == "KEY_BACKSPACE":
            if userline:
                userline.pop()
        elif inp.name == "KEY_ENTER":
            if "".join(userline) == line:
                userline = list()
                line_num += 1
            if line_num >= len(lines):
                print(term.clear)
                print(f"finished with file!")
                break
        elif inp.name == "KEY_ESCAPE":
            print(term.clear)
            print(
                f"last line index: {line_num}. use -r {line_num} to resume at this line"
            )
            break
        elif inp in line:
            userline.append(inp)


if __name__ == "__main__":
    argh.dispatch_command(go)
