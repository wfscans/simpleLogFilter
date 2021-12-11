import sys
from colorama import Fore, init
init()

class codeblock:
    def __init__(self):
        self.diff = []
        self.plus = 0
        self.minus = 0

def colorDiff(diff):
    for line in diff:
        if line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        elif line.startswith('@'):
            yield Fore.CYAN + line + Fore.RESET
        else:
            yield line

def diff(f):
    block = codeblock()
    for line in f:
        if line.startswith("@@"):
            if block.plus != block.minus:
                if (len(sys.argv) == 3) and (sys.argv[2] == "nocolor"):
                    try:
                        print(''.join(block.diff))
                    except BrokenPipeError:
                        pass
                else:
                    block.diff = colorDiff(block.diff)
                    try:
                        print(''.join(block.diff))
                    except BrokenPipeError:
                        pass
            block = codeblock()
            block.diff.append(line)
        elif line.startswith("+ "):
            block.diff.append(line)
            block.plus += len(line)
        elif line.startswith("- "):
            block.diff.append(line)
            block.minus += len(line)
        else:
            block.diff.append(line)


if __name__ == "__main__":
    helptext = "usage:\n  read diff from file: main.py <filename>\n  read diff from pipe: main.py -\n  pipe to 'less -R' for scrolling\n  print without color add 'nocolor' after filename/pipe"
    if len(sys.argv) < 2:
        print(helptext)
        exit()

    if sys.argv[1] == "-":
        diff(sys.stdin)
    elif sys.argv[1] == "-h":
        print(helptext)
        exit()
    else:
        with open(sys.argv[1], 'r') as f:
            diff(f)

    sys.stderr.close()
