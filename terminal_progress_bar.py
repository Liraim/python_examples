import fcntl, termios, struct, sys, time

def print_step(percent):
    ### simple version (doesn't work for Windows)
    # import curses
    #
    # curses.setupterm()
    # terminal_size = (curses.tigetnum('lines'), curses.tigetnum('cols'))
    terminal_size = struct.unpack('hh', fcntl.ioctl(sys.stdout,termios.TIOCGWINSZ, '1234'))
    template = "[%-" + str(terminal_size[1] - 7) + "s]%4d%%" # used 7 = 2 for "[" and "]" and 5 for percents
    print("\r" + template % ("=" * int(terminal_size[1] * percent), int(percent * 100)), end="")

for i in range(0, 101):
    print_step(i / 100.0)
    time.sleep(0.1)