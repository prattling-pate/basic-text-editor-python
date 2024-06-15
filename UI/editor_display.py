from logic.text_editor import TextEditor
from utility.logger import Logger
import curses

def run(stdscr) -> None:
    """Entry point into application"""
    stdscr.clear()

    running = True

    text_editor = TextEditor("piss.txt")
    logger = Logger("log.txt")

    curses.curs_set(1)
    curses.setsyx(1,1)

    while running:

        for line in text_editor.get_current_document_contents():
            stdscr.addstr(line)

        stdscr.move(*(text_editor.get_cursor_position()))

        user_input = stdscr.getch()

        logger.log(str(stdscr.getyx()))

        if user_input == curses.KEY_UP:
            text_editor.move_cursor(-1, 0)
        elif user_input == curses.KEY_DOWN:
            text_editor.move_cursor(1, 0)
        elif user_input == curses.KEY_LEFT:
            text_editor.move_cursor(0, -1)
        elif user_input == curses.KEY_RIGHT:
            text_editor.move_cursor(0, 1)
        elif user_input == ord('x'):
            running = False
        
        stdscr.clear()
        stdscr.refresh()
    
    print("Exited")
    logger.write_log()
    return

def start_editor():
    curses.wrapper(run)