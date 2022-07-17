#!/usr/bin/env python
from yaml import dump, load_all


def terminal_size():

    import fcntl
    import termios
    import struct
    try:
        th, tw, hp, wp = struct.unpack('HHHH',
                                    fcntl.ioctl(0, termios.TIOCGWINSZ,
                                                struct.pack('HHHH', 0, 0, 0, 0)))
    except OSError:
        th, tw, hp, wp = 25, 80, 0, 0
    return tw, th


def terminal_width():
    width = terminal_size()[0]
    return width


def terminal_height():
    height = terminal_size()[1]
    return height


def header_line():
    print("=" * terminal_width())


def center_text(s):
    print(s.upper().center(terminal_width(), " "))


header_line()
center_text("nexus gitops agent")
header_line()

d = {"m":12345}
print(dump(d, default_flow_style=False))
