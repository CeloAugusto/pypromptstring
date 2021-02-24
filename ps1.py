import sys
from dataclasses import dataclass

commands_to_eval = []


@dataclass
class Color:
    ALIAS: str
    ANSI: str


COLORS = [
    Color("%W", "\033[1\\;0m"),
    Color("%B", "\033[1\\;30m"),
    Color("%R", "\033[1\\;31m"),
    Color("%G", "\033[1\\;32m"),
    Color("%Y", "\033[1\\;33m"),
    Color("%P", "\033[1\\;34m"),
    Color("%I", "\033[1\\;35m"),
    Color("%C", "\033[1\\;36m"),
    Color("WHITE", "\033[1\\;0m"),
    Color("BLACK", "\033[1\\;30m"),
    Color("RED", "\033[1\\;31m"),
    Color("GREEN", "\033[1\\;32m"),
    Color("YELLOW", "\033[1\\;33m"),
    Color("PURPLE", "\033[1\\;34m"),
    Color("PINK", "\033[1\\;35m"),
    Color("CIAN", "\033[1\\;36m"),
]


def validate(args=[]):
    if not args:
        apply_default()
    else:
        apply_ps_command(generate_ps(*args))
    _eval()


def generate_ps(*args):
    ps = " ".join(args) + " "
    for c in COLORS:
        ps = ps.replace(c.ALIAS, c.ANSI)
    ps += "\033[0m"
    return ps


def apply_default():
    add('[ "$PSX" ] && PS1=$PSX')
    add("unset PSX")


def apply_ps_command(ps: str):
    add('\\[ \\"$PSX\\" \\] || PSX=$PS1')
    add(f"PS1=\\'{ps}\\'")


def _eval():
    for i in commands_to_eval:
        print("eval ", end="")
        print(i, end=" ;\n")
    sys.stdout.flush()
    exit()


def add(command: str):
    commands_to_eval.append(command)


def _print(args):
    add(f"echo '{args}'")


if __name__ == "__main__":
    validate(sys.argv[1:])
