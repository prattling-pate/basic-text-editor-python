from utility.logger import Logger
from logic.text_editor import TextEditor
import curses

def run(stdscr) -> None:
    """Entry point into application"""

    logger = Logger("log.txt")

    stdscr.clear()

    running = True

    text_editor = TextEditor("pis2.txt")

    logger.log("Text editor launched")

    while running:

        for i, line in enumerate(text_editor.get_current_document_contents(), 1):
            stdscr.addstr(f"{i}:{line}")

        stdscr.move(*(text_editor.get_cursor_position()))

        user_input = stdscr.getch()

        logger.log("key pressed: " + str(user_input))

        if user_input == curses.KEY_UP:
            text_editor.move_cursor(-1, 0)
        elif user_input == curses.KEY_DOWN:
            text_editor.move_cursor(1, 0)
        elif user_input == curses.KEY_LEFT:
            text_editor.move_cursor(0, -1)
        elif user_input == curses.KEY_RIGHT:
            text_editor.move_cursor(0, 1)
        elif user_input == curses.KEY_HOME:
            running = False
        # enter key is equal to 10
        elif user_input == 10:
            text_editor.insert_new_line()
            logger.log(str(text_editor.get_current_document_contents()))

        
        stdscr.clear()
        stdscr.refresh()

    logger.log("Closing text editor")
    logger.write_log()

def start_editor():
    curses.wrapper(run)
