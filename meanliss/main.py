import curses

from game_state import draw_state, get_init_state
from evolution import evolve

from time import sleep


def main(stdscr: curses.window):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    state = get_init_state("launcher", 5)

    while True:
        draw_state(stdscr, state, '#', '.')
        state = evolve(state)
        sleep(0.3)

        if stdscr.getch() != -1:
            break


if __name__ == "__main__":
    curses.wrapper(main)