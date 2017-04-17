import fcntl, termios, struct, sys, time

last_position = 0
length = 10
def print_spinning_line():
    global last_position
    ### Getting terminal size
    terminal_size = struct.unpack('hh', fcntl.ioctl(sys.stdout,termios.TIOCGWINSZ, '1234'))
    ### simple version (doesn't work for Windows)
    # import curses
    #
    # curses.setupterm()
    # terminal_size = (curses.tigetnum('lines'), curses.tigetnum('cols'))

    template = "[%s]" % (" " * last_position + "=" * length + " " * (terminal_size[1] - last_position - length - 3), )
    print("\r" + template, end="")
    last_position += 1
    if last_position > terminal_size[1] - length - 3:
        last_position = 0

while True:
    print_spinning_line()
    time.sleep(0.01)